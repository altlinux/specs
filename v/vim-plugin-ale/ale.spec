# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

%define plugname ale
Name: vim-plugin-%plugname
Version: 3.3.0
Release: alt1
Summary: Check syntax in Vim asynchronously and fix files
License: BSD-2-Clause
Group: Editors
Url: https://github.com/dense-analysis/ale

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-vim

%description
ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax
checking and semantic errors) in Vim 8.0+ while you edit your text files,
and acts as a Vim Language Server Protocol client.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -av ale_linters autoload doc ftplugin plugin rplugin syntax %buildroot%vim_runtime_dir

%files
%doc LICENSE README.md supported-tools.md
%vim_runtime_dir/*/*

%changelog
* Tue Mar 07 2023 Vitaly Chikunov <vt@altlinux.org> 3.3.0-alt1
- First import v3.3.0 (2022-12-25).
