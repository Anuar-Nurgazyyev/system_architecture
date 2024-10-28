# Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    participant ps as PubSub
    participant omr as "OMR 5 Star Checklist\nService"
    participant fs as "5 Star\nService"
    participant lm as "LM\nbased on Donut"

    activate ps
    omr->>ps: read the message
    deactivate ps
    activate omr
    omr->>omr: Parsing collections with<br>5Star Document Type
    omr->>omr: downloading PDFs from<br>corresponding collection
    omr->>fs: Find the version of the document by **QR**<br>[ocr_elasticsearch_vl_list_five_star_form_pages<br>_data_view_api_v1_documents_file_id_pages_get]
    activate fs
    fs-->>omr: success

    alt Version ID not found
        fs-->>omr: version ID doesn't found
        omr->>fs: find the __last version__ of the document<br>[api/user-service/v1/fivestar/v2/<br>5star-form/versions/list]
    end
    deactivate fs

    omr->>fs: extraction of ICD codes related<br>to this version of the document<br>api/user-service/v1/<br>fivestar/v3/5star-form
    activate fs
    fs-->>omr: success
    deactivate fs
    omr->>lm: the worker runs the model
    activate lm
    lm->>lm: successfully read ICD codes<br>on the form and determined<br>checkbox statuses
    lm-->>omr: returns the results
    deactivate lm
    omr->>omr: filter the results, supply<br>ICD codes that the API knows.
    omr->>fs: Added recognized code statuses<br>to the version of this document<br>api/user-service/v1/<br>fivestar/v1/5star-form.
    deactivate omr
