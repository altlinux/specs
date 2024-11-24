# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: mkcert
Version: 1.4.4
Release: alt1
Summary: A simple zero-config tool to make locally trusted development certificates with any names
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/FiloSottile/mkcert

Source: %name-%version.tar
BuildRequires: golang
BuildRequires: nss-utils
%{?!_without_check:%{?!_disable_check:
BuildRequires: openssl
}}

%description
mkcert is a simple tool for making locally-trusted development
certificates. It requires no configuration.

%prep
%setup

%build
go generate
go build -v -buildmode=pie -ldflags "-X main.Version=%version"

%install
install -Dp mkcert -t %buildroot%_bindir

%check
%buildroot%_bindir/mkcert -version | grep -Fx '%version'
go test . # [no test files]
export CAROOT=ca
%buildroot%_bindir/mkcert example.org
openssl pkey -in ca/rootCA-key.pem -noout -check
openssl verify -CAfile ca/rootCA.pem ca/rootCA.pem
openssl verify -CAfile ca/rootCA.pem example.org.pem
openssl pkey -in example.org-key.pem -noout -check
openssl pkey -in example.org-key.pem -pubout > a
openssl x509 -in example.org.pem -noout -pubkey > b
diff -u a b

%files
%doc AUTHORS LICENSE README.md
%_bindir/mkcert

%changelog
* Sun Nov 24 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.4-alt1
- First import v1.4.4-1-g1c1dc4e (2024-04-18).
