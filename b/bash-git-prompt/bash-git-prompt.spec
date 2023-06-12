# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: bash-git-prompt
Version: 2.7.1
Release: alt1
Summary: An informative and fancy bash prompt for Git users
License: BSD-2-Clause
Group: Development/Other
Url: https://github.com/magicmonty/bash-git-prompt

BuildArch: noarch
Source: %name-%version.tar

%description
A bash prompt that displays information about the current git repository. In
particular the branch name, difference with remote branch, number of files
staged, changed, etc.

To enable add these example lines to your ~/.bashrc:

   GIT_PROMPT_ONLY_IN_REPO=1
   GIT_PROMPT_THEME=Single_line
   source %_datadir/%name/gitprompt.sh

List available themes with 'git_prompt_list_themes'.

%prep
%setup

%build
echo *.sh | xargs -tn1 bash -n

%install
install -Dp *sh -t %buildroot%_datadir/%name
cp -pr themes %buildroot%_datadir/%name

%define _customdocdir %_docdir/%name

%files
%doc LICENSE.txt README.md
%_datadir/%name

%changelog
* Mon Jun 12 2023 Vitaly Chikunov <vt@altlinux.org> 2.7.1-alt1
- First import 2.7.1-88-gc2f8ca6 (2023-05-19).
