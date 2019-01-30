#
# Sccsid @(#)ex.spec	1.7 (gritter) 1/22/05
#
Summary: A port of the traditional ex/vi editors
Name: vi-traditional
Version: 050325
Release: alt1
License: BSD
Source: ex-%version.tar.bz2
Group: Editors
Vendor: Gunnar Ritter <Gunnar.Ritter@pluto.uni-freiburg.de>
Url: http://ex-vi.sourceforge.net
Patch: ex-traditional.patch

# prefix applies to bindir, libexecdir, and mandir.
%define prefix		/usr
%define preservedir	/var/tmp
%define cflags		-g -Os -fomit-frame-pointer

%define makeflags	PREFIX=%prefix BINDIR=%_bindir LIBEXECDIR=%_prefix/libexec MANDIR=%_mandir PRESERVEDIR=%preservedir INSTALL=install RPMCFLAGS="%cflags" STRIP=""

# Automatically added by buildreq on Wed Jan 30 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libtinfo-devel python-base sh4
BuildRequires: libncursesw-devel

%description
This is a port of the traditional ex and vi editor implementation as
found on 2BSD and 4BSD. It was enhanced to support most of the additions
in System V and POSIX.2, and international character sets like UTF-8 and
many East Asian encodings.

%prep
%setup -n ex-%version
%patch -p1

%build
%make_build %makeflags TERMLIB=ncursesw LARGEF=-DLARGEF

%install
make DESTDIR=%buildroot %makeflags install

%files
%doc Changes LICENSE README TODO
%_bindir/*
%_prefix/libexec/ex*
%_man1dir/*

%changelog
* Wed Jan 30 2019 Fr. Br. George <george@altlinux.ru> 050325-alt1
- Initial build for ALT (at last!)

