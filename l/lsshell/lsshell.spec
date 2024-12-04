%define _unpackaged_files_terminate_build 1
%global import_path github.com/blacknon/lssh

Name: lsshell
Version: 0.1.0
Release: alt1
Summary: lsshell is a Go-based TUI tool that allows parallel command execution across multiple SSH sessions, simplifying remote server management. 
License: MIT
Group: Networking/Remote access
Url: https://github.com/blacknon/lsshell

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
lsshell is a TUI (Text-based User Interface) tool for managing parallel SSH
sessions with an easy-to-use list selection interface.
It allows you to execute commands across multiple remote servers simultaneously,
making it ideal for system administrators and developers managing multiple machines. 

%prep
%setup -q

%build
cat >> lsshell.conf <<EOF
# Copyright (c) 2022 Blacknon. All rights reserved.
# Use of this source code is governed by an MIT license
# that can be found in the LICENSE file.

#
[log]
enable = true
timestamp = true
dirpath = "/path/to/logdir"


#
[common]


#
[server.PasswordAuth_ServerName]
addr = "192.168.100.101"
port = "22"
user = "test"
pass = "Password"
note = "Password Auth Server"


#
[server.KeyAuth_ServerName]
addr = "192.168.100.102"
port = "22"
user = "test"
key  = "/tmp/key.pem"
note = "Key Auth Server"
EOF

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .


%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
 
%golang_install
mkdir -p %buildroot%_datadir/%name/example
mv lsshell.conf %buildroot%_datadir/%name/example/libsshell-example.conf

%files
%doc README.md
%_bindir/*
%_datadir/%name/example/libsshell-example.conf

%changelog
* Thu Sep 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus
