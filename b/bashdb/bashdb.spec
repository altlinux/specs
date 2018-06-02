%define oversion 4.2-0.8

Name: bashdb
Version: 4.2_0.8
Release: alt1

Summary: BASH with Debugger and Improved Debug Support and Error Handling

Url: http://bashdb.sourceforge.net/
License: GPL
Group: Shells

Packager: Alexey Gladkov <legion@altlinux.ru>

# Source-url: http://prdownloads.sf.net/bashdb/%name-%oversion.tar
Source: http://prdownloads.sf.net/bashdb/%name-%version.tar
Patch0: bashdb-alt-use-mktemp.patch
Patch1: bashdb-alt-fix-builtin.patch
Patch2: bashdb-fix-set0.patch

Requires: /usr/lib/bash

# manually removed: tetex-core
# Automatically added by buildreq on Thu Aug 07 2008
BuildRequires: gcc-c++ bash-devel

%description
The Bash Debugger Project contains patched sources to BASH that enable
better debugging support as well as improved error reporting. In
addition, this project contains the most comprehensive source-code
debugger for bash that has been written.

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1 -b .fix
%patch2 -p1

%build
export CFLAGS="$CFLAGS %optflags %optflags_shared"

%configure \
	--with-pic \
	--enable-getopt \
	--with-bash \
	--with-bash-src=/usr/include/bash
%make_build

%install
%makeinstall_std

mkdir -p -- %buildroot/usr/lib/bash
mv -f -- %buildroot/%_datadir/%name/builtin/* %buildroot/usr/lib/bash

%files
%doc README THANKS NEWS TODO
%_bindir/*
%_datadir/%name/
/usr/lib/bash/*
%_infodir/*
%_man1dir/*

%changelog
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
