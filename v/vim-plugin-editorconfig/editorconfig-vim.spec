# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: vim-plugin-editorconfig
Summary: EditorConfig plugin for Vim
Version: 1.2.1
Release: alt1
License: BSD-2-Clause and Python-2.0
Group: Editors
Url: https://editorconfig.org/
Vcs: https://github.com/editorconfig/editorconfig-vim

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-vim

%description
This is an %summary.

EditorConfig helps maintain consistent coding styles for multiple
developers working on the same project across various editors and
IDEs. The EditorConfig project consists of a file format for defining
coding styles and a collection of text editor plugins that enable editors
to read the file format and adhere to defined styles. EditorConfig files
are easily readable and they work nicely with version control systems.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -av autoload doc ftdetect plugin %buildroot%vim_runtime_dir

%files
%doc LICENSE README.md CONTRIBUTORS
%vim_runtime_dir/*/*

%changelog
* Mon Jan 27 2025 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt1
- Update to v1.2.1 (2024-11-08).

* Thu Nov 11 2021 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt1
- First import of v1.1.1-7-g3078cd1 (2021-07-25).
