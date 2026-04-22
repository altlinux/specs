# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: bitchx
Version: 1.2.1
Release: alt2
Summary: Nostalgic IRC client
License: BSD-3-Clause
Group: Networking/Chat
Url: https://bitchx.sourceforge.net/
Vcs: git://git.code.sf.net/p/bitchx/git

Source: %name-%version.tar
BuildRequires: libcrypt-devel
BuildRequires: libncurses-devel
BuildRequires: libssl-devel

%description
BitchX began as a script by Trench and HappyCrappy for the popular UNIX
IRC client ircII. Around Christmas of 1994 the script was patched directly
into the client by Colten Edwards (panasync).

As BitchX was developed over the years it both developed its own large
set of unique features, as well as acquiring many features from EPIC
(another popular ircII offshoot).

%prep
%setup
sed -i '/internal_version\[\] =/s/\(".*\)\("\)/\1+%release\2/' source/irc.c

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS) -std=gnu17
%autoreconf
%configure --enable-ipv6
%make_build

%install
%makeinstall_std

%check
%buildroot%_bindir/BitchX -v | grep -F 'Version (BitchX-1.2.1) -- Date (20141114+%release).'

%files
%define _customdocdir %_docdir/%name
%doc COPYRIGHT README Changelog doc
%_bindir/BitchX
%_bindir/BitchX-1.2.1
%_bindir/scr-bx
%_libdir/bx
%_man1dir/BitchX.1.*

%changelog
* Wed Apr 22 2026 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt2
- Workaround FTPBS with gcc15.

* Tue May 13 2025 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt1
- First import 1.2.1-2019-20-geaf6456 (2019-12-28).
