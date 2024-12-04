%define _unpackaged_files_terminate_build 1
%global import_path github.com/blacknon/lssh

Name: lssh
Version: 0.6.13
Release: alt1
Summary: TUI list select ssh/scp/sftp client tools.
License: MIT
Group: Networking/Remote access
Url: https://github.com/blacknon/lssh

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A list-based SSH/SCP/SFTP client supporting single and parallel connections,
local bashrc usage on remote machines, and advanced proxying.

%prep
%setup -q

%build
cat >> lssh.conf <<EOF
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

%golang_build cmd/lssh cmd/lscp cmd/lsftp 


%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
 
%golang_install
mkdir -p %buildroot%_datadir/%name/example
mv lssh.conf %buildroot%_datadir/%name/example/libssh-example.conf

%files
%doc README.md
%_bindir/*
%_datadir/%name/example/libssh-example.conf

%changelog
* Thu Sep 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.6.13-alt1
- initial build for Sisyphus
