SCHEMA = {
  "type": "record",
  "name": "Record",
  "fields": [
    {
      "name": "header",
      "type": {
        "type": "record",
        "namespace": "Record",
        "name": "header",
        "fields": [
          {
            "name": "call_start_ts",
            "type": "long"
          },
          {
            "name": "subscriber.imsi",
            "type": "long"
          },
          {
            "name": "icid",
            "type": "string"
          },
          {
            "name": "is_good_call",
            "type": "string"
          }
        ]
      }
    },
    {
      "name": "dimensions",
      "type": {
        "type": "record",
        "namespace": "Record",
        "name": "dimensions",
        "fields": [
          {
            "name": "call_id",
            "type": "string"
          },
          {
            "name": "call_leg_direction",
            "type": "string"
          },
          {
            "name": "status",
            "type": "string"
          },
          {
            "name": "call_duration",
            "type": "long"
          },
          {
            "name": "ims_media_type",
            "type": "string"
          },
          {
            "name": "call_end_ts",
            "type": "long"
          },
          {
            "name": "ims_service.forking",
            "type": "string"
          },
          {
            "name": "ims_service.forwarding",
            "type": "string"
          },
          {
            "name": "ims_service.conference",
            "type": "string"
          },
          {
            "name": "ims_service.3_way",
            "type": "string"
          },
          {
            "name": "ims_service.conference.uri",
            "type": "string"
          },
          {
            "name": "ims_service.emergency",
            "type": "string"
          },
          {
            "name": "ims_service.emergency.name",
            "type": "string"
          },
          {
            "name": "ims_service.call_hold",
            "type": "string"
          },
          {
            "name": "ims_sub_procedures",
            "type": {
              "type": "array",
              "items": "string"
            }
          },
          {
            "name": "ims_media_transcoded",
            "type": "string"
          },
          {
            "name": "ims_bgf_reselection",
            "type": "string"
          },
          {
            "name": "full_visibility",
            "type": "string"
          },
          {
            "name": "subscriber.msisdn",
            "type": "long"
          },
          {
            "name": "subscriber.impu",
            "type": "string"
          },
          {
            "name": "subscriber.mcc",
            "type": "string"
          },
          {
            "name": "subscriber.mnc",
            "type": "string"
          },
          {
            "name": "device.imeitac",
            "type": "long"
          },
          {
            "name": "device.imeisvn",
            "type": "long"
          },
          {
            "name": "user_agent",
            "type": "string"
          },
          {
            "name": "audio_codec_name",
            "type": "string"
          },
          {
            "name": "audio_codec_sampling_rate",
            "type": "long"
          },
          {
            "name": "cscf_addr",
            "type": "string"
          },
          {
            "name": "pcscf_addr",
            "type": "string"
          },
          {
            "name": "pgw_addr",
            "type": "string"
          },
          {
            "name": "sgw_addr",
            "type": "string"
          },
          {
            "name": "mme_addr",
            "type": "string"
          },
          {
            "name": "start_location_identifier",
            "type": "string"
          },
          {
            "name": "start_rat",
            "type": "string"
          },
          {
            "name": "end_location_identifier",
            "type": "string"
          },
          {
            "name": "end_rat",
            "type": "string"
          },
          {
            "name": "visited_rats",
            "type": "string"
          },
          {
            "name": "ims_session_setup_cc",
            "type": "long"
          },
          {
            "name": "ims_session_setup_ts",
            "type": "long"
          },
          {
            "name": "ims_session_setup_cd",
            "type": "string"
          },
          {
            "name": "ims_session_termination_cc",
            "type": "long"
          },
          {
            "name": "ims_session_termination_ts",
            "type": "long"
          },
          {
            "name": "ims_session_termination_cd",
            "type": "string"
          },
          {
            "name": "ims_session_termination_direction",
            "type": "string"
          },
          {
            "name": "ims_csfb_usage",
            "type": "boolean"
          },
          {
            "name": "sgw_relocation_attempt",
            "type": "boolean"
          },
          {
            "name": "n_visited_cells",
            "type": "long"
          },
          {
            "name": "endc_state",
            "type": "string"
          },
          {
            "name": "epdg_addr",
            "type": "string"
          },
          {
            "name": "video_codec_name",
            "type": "string"
          },
          {
            "name": "video_codec_sampling_rate",
            "type": "string"
          },
          {
            "name": "ims_ue_status_call_start",
            "type": "string"
          },
          {
            "name": "ims_session_termination_reason_prot",
            "type": "string"
          },
          {
            "name": "ims_session_termination_reason_cause",
            "type": "string"
          },
          {
            "name": "ims_session_termination_reason_text",
            "type": "string"
          },
          {
            "name": "ims_epsfb_usage",
            "type": "string"
          },
          {
            "name": "ims_registered_contacts",
            "type": "string"
          },
          {
            "name": "ims_user_registered",
            "type": "string"
          },
          {
            "name": "called_party",
            "type": "string"
          },
          {
            "name": "imei",
            "type": "string"
          },
          {
            "name": "pgwu",
            "type": "string"
          },
          {
            "name": "sgwu",
            "type": "string"
          },
          {
            "name": "twan",
            "type": "string"
          },
          {
            "name": "mtas",
            "type": "string"
          },
          {
            "name": "bgf",
            "type": "string"
          },
          {
            "name": "amf",
            "type": "string"
          },
          {
            "name": "smf",
            "type": "string"
          },
          {
            "name": "upf",
            "type": "string"
          },
          {
            "name": "apn",
            "type": "string"
          },
          {
            "name": "dnn",
            "type": "string"
          },
          {
            "name": "sst",
            "type": "string"
          },
          {
            "name": "sd",
            "type": "string"
          }
        ]
      }
    }
  ]
}