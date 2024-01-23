# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: webhook
Version: 2.8.1
Release: alt1
Summary: A lightweight incoming webhook server to run shell commands
License: MIT
Group: System/Servers
Url: https://github.com/adnanh/webhook

Source: %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: curl
}}

%description
webhook is a lightweight configurable tool written in Go, that allows
you to easily create HTTP endpoints (hooks) on your server, which you
can use to execute configured commands. You can also pass data from
the HTTP request (such as headers, payload or query variables) to your
commands. webhook also allows you to specify rules which have to be
satisfied in order for the hook to be triggered.

%prep
%setup

%build
export CGO_ENABLED=0
export GOFLAGS='-buildmode=pie'
go build -v

%install
install -Dp webhook %buildroot%_bindir/webhook
install -Dpm644 .gear/webhook.service -t %buildroot%_unitdir

%check
%buildroot%_bindir/webhook -version |& grep -Fx 'webhook version %version'
go test ./...
cat > hooks.json <<EOF
[{"id": "uname", "include-command-output-in-response": true, "execute-command": "/bin/uname"}]
EOF
%buildroot%_bindir/webhook -verbose & sleep 0.1
# I wish there were a way to wait for service readiness.
curl -sSf http://localhost:9000/hooks/uname | grep -x Linux
kill %%1

%files
%define _customdocdir %_docdir/%name
%doc CONTRIBUTING.md LICENSE README.md hooks.*.example docs/*
%_bindir/webhook
%_unitdir/%name.service

%changelog
* Tue Jan 23 2024 Vitaly Chikunov <vt@altlinux.org> 2.8.1-alt1
- First import 2.8.1-6-gbd1aaab (2023-12-26).
