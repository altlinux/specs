# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: ssh3
Version: 0.1.4
Release: alt1
Summary: Faster and rich secure shell using HTTP/3
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/francoismichel/ssh3
Requires: %name-server = %EVR
Requires: %name-client = %EVR
# https://github.com/francoismichel/ssh3/issues/53
ExcludeArch: armh %ix86

Source: %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: iproute2
BuildRequires: rpm-build-vm
BuildRequires: /usr/bin/openssl
BuildRequires: /usr/bin/ssh-keygen
}}

%description
SSH3 is a complete revisit of the SSH protocol, mapping its semantics on top of
the HTTP mechanisms. In a nutshell, SSH3 uses QUIC+TLS1.3 for secure channel
establishment and the HTTP Authorization mechanisms for user authentication.
Among others, SSH3 allows the following improvements:

Significantly faster session establishment:

- New HTTP authentication methods such as OAuth 2.0 and OpenID Connect in
  addition to classical SSH authentication

- Robustness to port scanning attacks: your SSH3 server can be made invisible
  to other Internet users

- UDP port forwarding in addition to classical TCP port forwarding

- All the features allowed by the modern QUIC protocol: including connection
  migration (soon) and multipath connections

SSH3 stands for the concatenation of SSH and H3.

%package server
Summary: SSH3 server
Group: Networking/Remote access

%description server
%summary.

%package client
Summary: SSH3 client
Group: Networking/Remote access
%description client
%summary.

%prep
%setup

%build
export CGO_ENABLED=1
export CGO_CPPFLAGS="%optflags"
export CGO_CFLAGS="%optflags"
export CGO_CXXFLAGS="%optflags"
export GOFLAGS="-buildmode=pie"
go build -v -o ssh3 cli/client/main.go
go build -v -o ssh3-server cli/server/main.go

%install
install -Dp ssh3-server -t %buildroot%_sbindir
install -Dp ssh3 -t %buildroot%_bindir
install -Dp generate_openssl_selfsigned_certificate.sh -t %buildroot%_datadir/%name

%check
./ssh3 --help
./ssh3-server --help
## Unit tests.
go run github.com/onsi/ginkgo/v2/ginkgo --no-color -r
## Integration tests.
# ed25519 does not work: https://github.com/francoismichel/ssh3/issues/38
export TESTUSER_USERNAME=builder
export TESTUSER_PRIVKEY=$HOME/.ssh/id_testuser
ssh-keygen -t rsa -N '' -f $TESTUSER_PRIVKEY
cat $TESTUSER_PRIVKEY.pub >> ~/.ssh/authorized_keys
export ATTACKER_PRIVKEY=$HOME/.ssh/id_attacker
ssh-keygen -t rsa -N '' -f $ATTACKER_PRIVKEY
bash ./generate_openssl_selfsigned_certificate.sh
export CERT_PRIV_KEY=$PWD/priv.key
export CERT_PEM=$PWD/cert.pem
export SSH3_INTEGRATION_TESTS_WITH_SERVER_ENABLED=1
vm-run go run github.com/onsi/ginkgo/v2/ginkgo --no-color --flake-attempts=4 ./integration_tests

%files

%files server
%doc LICENSE README.md
%_sbindir/ssh3-server
%_datadir/%name

%files client
%doc LICENSE README.md
%_bindir/ssh3

%changelog
* Sun Dec 17 2023 Vitaly Chikunov <vt@altlinux.org> 0.1.4-alt1
- Experimental build v0.1.4-2-gbe31ba2 (2023-12-17).
