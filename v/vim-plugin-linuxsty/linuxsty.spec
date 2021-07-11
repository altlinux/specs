# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

%define plugname linuxsty
Name:		vim-plugin-%plugname
Version:	0.4
Release:	alt1
Summary:	Vim plugin to respect the Linux kernel coding style
Group:		Editors
# 'Distributed under the same terms as Vim itself. See :help license.'
License:	Charityware
URL:		https://github.com/vivien/vim-linux-coding-style
Packager:	VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

Source:		%name-%version.tar
BuildArch:	noarch
Requires(pre):	vim-common >= 4:7.0
BuildRequires(pre): rpm-build-vim

%description
This plugin is meant to help you respecting the Linux kernel coding style,
described at:
  https://www.kernel.org/doc/Documentation/process/coding-style.rst

It will automatically apply known rules to kernel related files, such
as .c, .h, Kconfig and patch files. The main rules are about indentation
and syntax error highlighting (like exceeding 80 chars).

%prep
%setup

%install
mkdir -p %buildroot/%vim_plugin_dir
install -p -m644 plugin/linuxsty.vim %buildroot%vim_plugin_dir/

%files
%doc README.md
%vim_plugin_dir/linuxsty.vim

%changelog
* Sun Jul 11 2021 Vitaly Chikunov <vt@altlinux.org> 0.4-alt1
- First import.
