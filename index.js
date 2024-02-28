const express = require("express");
const body_parser = require("body-parser");
const axios = require("axios");

const app = express().use(body_parser.json());
const token ="";

app.listen(8000,()=>{
    console.log("webhook is listening");
});

//callback url
app.get("/webhook", (req,res)=>{
    let mode = req.query["hub.mode"];
    let challenge = req.query["hub.challenge"];
    let token = req.query["hub.verify_token"];

    const myToken ="thadevoos";

    if(mode && token){

        if(mode ==="subcribe" && token === myToken){
            res.status(200).send(challenge);
        }
        else{
            res.status(403);
        }

    }
});

app.post("/webhook",(req,res)=>{

    let body_param = req.body;

    console.log(JSON.stringify(body_param,null,2));

    if(body_param.object){
        if(body_param.enty && 
            body_param.enty[0].changes[0].value.message &&
            body_param.enty[0].changes[0].value.message[0]
            ){
                let phon_no_id=body_param.entry[0].challenge[0].value.metadata.phone_number_id;
                let from= body_param.entry[0].changes[0].value.message[0].from;
                let msg_body = body_param.entry[0].changes[0].value.message[0].text.body;


                axios({
                    methord: "POST",
                    url:"https://graph.facebook.com/v17.0/"+phon_no_id+"/messages?access_token="+token,
                    data:{
                        "messaging_product": "whatsapp",
                         "to": from,
                         text:{
                            body:"message"
                         }
                    },
                     
                });
                res.sendStatus(200);
            }else{
                res.sendStatus(404);
                }
            }
        }
);