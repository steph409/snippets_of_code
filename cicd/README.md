## Gitlab ci

```bash
# install gitlab runner
sudo curl --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-darwin-amd64"
sudo chmod +x /usr/local/bin/gitlab-runner

# run the gitlab runner
cd ~
gitlab-runner install
gitlab-runner start

```