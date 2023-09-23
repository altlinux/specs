# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

%define plugname linuxsty
Name: vim-plugin-%plugname
Version: 0.4
Release: alt2
Summary: Vim plugin to respect the Linux kernel coding style
Group: Editors
# 'Distributed under the same terms as Vim itself. See :help license.'
License: Vim
URL: https://github.com/gregkh/kernel-coding-style
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>
BuildArch: noarch
Requires(pre): vim-common >= 4:7.0

Source: %name-%version.tar
BuildRequires(pre): rpm-build-vim
%{?!_without_check:%{?!_disable_check:
BuildRequires: vim-common
}}

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
install -Dpm644 plugin/linuxsty.vim -t %buildroot%vim_plugin_dir

%check
# Experimental syntax check for .vim
# Will output harmless warnings such as:
#   Vim: Warning: Output is not to a terminal
#   Vim: Warning: Input is not from a terminal
! view -S plugin/linuxsty.vim +:q </dev/null | strings | grep -99 Error || exit 1

%files
%doc README.md
%vim_plugin_dir/linuxsty.vim

%changelog
* Sat Sep 23 2023 Vitaly Chikunov <vt@altlinux.org> 0.4-alt2
- Switch upstream and update to v0.4-20-g8cd1764 (2023-08-20).
- Update License tag.

* Sun Jul 11 2021 Vitaly Chikunov <vt@altlinux.org> 0.4-alt1
- First import.
