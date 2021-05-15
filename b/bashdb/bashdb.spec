%define bashversion 4.4
%define oversion 1.0.1

Name: bashdb
Version: %{bashversion}_%oversion
Release: alt2

Summary: BASH with Debugger and Improved Debug Support and Error Handling

Url: http://bashdb.sourceforge.net/
License: GPL
Group: Shells

Packager: Alexey Gladkov <legion@altlinux.ru>

# Source-url: http://prdownloads.sf.net/bashdb/%name-%bashversion-%oversion.tar.bz2
Source: %name-%version.tar
Patch0: bashdb-alt-use-mktemp.patch
Patch1: bashdb-alt-fix-builtin.patch

Requires: %_libexecdir/bash

# manually removed: tetex-core
# Automatically added by buildreq on Thu Aug 07 2008
BuildRequires: gcc-c++ bash-devel

BuildRequires: rpm-build-python3

%description
The Bash Debugger Project contains patched sources to BASH that enable
better debugging support as well as improved error reporting. In
addition, this project contains the most comprehensive source-code
debugger for bash that has been written.

%prep
%setup -n %name-%version
%patch0 -p2
%patch1 -p2 -b .fix

%__subst "s|/usr/bin/env python\$|/usr/bin/env python3|" lib/term-highlight.py

%build
export CFLAGS="$CFLAGS %optflags %optflags_shared"

%configure \
	--with-pic \
	--enable-getopt \
	--with-bash \
	--with-bash-src=%_includedir/bash
%make_build

%install
%makeinstall_std

mkdir -p -- %buildroot%_libexecdir/bash
mv -f -- %buildroot/%_datadir/%name/builtin/* %buildroot%_libexecdir/bash

%files
%doc README.md THANKS NEWS TODO
%_bindir/*
%_datadir/%name/
%_libexecdir/bash/*
%_infodir/*
%_man1dir/*

%changelog
* Sat May 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.4_1.0.1-alt2
- add BR: rpm-build-python3

* Tue Feb 11 2020 Vitaly Lipatov <lav@altlinux.ru> 4.4_1.0.1-alt1
- new version (4.4_1.0.1) with rpmgs script

* Thu Jul 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4_0.94-alt1
- Updated to upstream version 4.4_0.94.

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 4.2_0.8-alt1
- new version 4.2_0.8 (with rpmrb script)

* Tue Nov 04 2008 Alexey Gladkov <legion@altlinux.ru> 4.0-alt2
- Fix build for x86_64.
- Fix requires.

* Sat Nov 01 2008 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- New version (4.0)

* Thu Aug 07 2008 Alexey Gladkov <legion@altlinux.ru> 3.1-alt2
- Update BuildRequires.
- Fix $0 for script under debugger.
- Fix tmpdir value and use mktemp.
- Substitution of arguments for a script under debugger is corrected.

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- just rebuild

* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt0.1
- initial build for ALT Linux Sisyphus
