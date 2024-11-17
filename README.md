# Setup to connect GitHub action with GCP

1. Setup WIF (WOrkflow identity Federation) Kind of authenticating technique for GCP with the help of short lived tokens.
    a. create pool and provider
        issuer_uri: https://token.actions.githubusercontent.com
        mappings:
            google.subject assertion.sub
            attribute.actor assertion.act
            attribute.aud assertion.aud
            attribute.repository assertion.repository
        condition:
            assertion.repository=='shubhamvaidya-9090/github-ci-cd'
    b. Add policy Binding
        gcloud iam service-accounts add-iam-policy-binding "cli-service-account-1@playground-s-11-fa1a560e.iam.gserviceaccount.com" \
        --project="playground-s-11-fa1a560e" \
        --role="roles/iam.workloadIdentityUser" \
        --member="principalSet://iam.googleapis.com/projects/616931552405/locations/global/workloadIdentityPools/github-pool/attribute.repository/shubhamvaidya-9090/github-ci-cd"

https://iam.googleapis.com/projects/616931552405/locations/global/workloadIdentityPools/github-pool/providers/github-provider

