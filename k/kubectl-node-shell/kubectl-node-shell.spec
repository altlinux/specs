%define _unpackaged_files_terminate_build 1

Name: kubectl-node-shell
Version: 1.11.0
Release: alt1

Summary: Exec into node via kubectl
License: Apache-2.0
Group: Other
Url: https://github.com/kvaps/kubectl-node-shell
Vcs: https://github.com/kvaps/kubectl-node-shell

Source: %name-%version.tar

BuildArch: noarch

%description
Start a root shell in the node's host OS running.
Uses an alpine pod with nsenter for Linux nodes and a HostProcess pod with
PowerShell for Windows nodes.
(formerly known as kubectl-enter)

%prep
%setup

sed -i '1s|#!/usr/bin/env sh|#!/bin/sh|' kubectl-node_shell

%install
install -pD -m0755 kubectl-node_shell %buildroot%_bindir/kubectl-node_shell

%files
%doc README.md
%_bindir/kubectl-node_shell

%changelog
* Tue Dec 02 2025 Alexander Stepchenko <geochip@altlinux.org> 1.11.0-alt1
- Initial build.
