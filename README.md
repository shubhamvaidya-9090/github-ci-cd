# Setup to connect GitHub action with GCP

1. Setup WIF (WOrkflow identity Federation) Kind of authenticating technique for GCP with the help of short lived tokens. (This cant be done in sandbox envirnment as you dont have permission to grant policies to service account)

gcloud iam service-accounts add-iam-policy-binding "cli-service-account-1@playground-s-11-9d1e814d.iam.gserviceaccount.com" \
--project="playground-s-11-9d1e814d" \
--role="roles/iam.workloadIdentityUser" \
--member="principalSet://iam.googleapis.com/projects/916179961092/locations/global/workloadIdentityPools/github-pool/attribute.repository/shubhamvaidya-9090/github-ci-cd"


2. use service account json for aunthentication
3. doecker ned to be install on runners and add user in docker group


