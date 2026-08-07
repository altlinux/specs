#
# spec file for package moe
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: moe
Version: 1.16
Release: alt1

Summary: A Text Editor
License: GPL-2.0-or-later
Group: Editors

Url: https://www.gnu.org/software/moe/moe.html
Source: https://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.lz

BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: libstdc++-devel
BuildRequires: lzip
BuildRequires: libncurses-devel

%description
GNU Moe is an 8-bit clean, console text editor for ISO-8859 and ASCII
character encodings. It has a modeless interface, online help,
multiple windows, unlimited undo/redo capability, unlimited line length, global
search/replace (on all buffers at once), block operations, automatic
indentation, word wrapping, file name completion, directory browser, duplicate
removal from prompt histories, delimiter matching, text conversion from/to
UTF-8 and romanization.

%prep
%setup

%build
%configure
%make_build CXXFLAGS="%optflags"

%install
%makeinstall_std install-man

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %_sysconfdir/moe.conf
%_bindir/moe
%_infodir/moe.info*
%_man1dir/moe.1*

%changelog
* Fri Aug 07 2026 Michael Shigorin <mike@altlinux.org> 1.16-alt1
- initial build for ALT Sisyphus
- based on openSUSE 1.16 package by Andreas Stieger et al

