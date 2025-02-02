Name: yabasic
Version: 2.91.1
Release: alt1
Epoch: 1

Summary: Small basic interpreter with printing and graphics

License: MIT
Group: Development/Other
Url: http://www.yabasic.de/
Vcs: https://github.com/marcIhm/yabasic

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://2484.de/yabasic/download/%name-%version.tar

# Automatically added by buildreq on Wed Oct 22 2008
BuildRequires: imake libXt-devel libncurses-devel
BuildRequires: libffi-devel

BuildPreReq: bison flex

%description
Yabasic implements the most common and simple elements of the basic
langugage; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%prep
%setup

%build
%autoreconf
%configure --with-x
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README *.htm
%_bindir/%name
%_man1dir/*

%changelog
* Sun Feb 02 2025 Vitaly Lipatov <lav@altlinux.ru> 1:2.91.1-alt1
- new version, update URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.763-alt3.qa1
- NMU: rebuilt for debuginfo.

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt3
- add autoreconf, migrate to git

* Wed Oct 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt2
- update buildreq

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt1
- "Yabasic has probably reached its final Version 2.763"
- cleanup spec, update buildreqs

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt0.1
- new version

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.751-alt0.1
- new version
- spec from PLD Team <feedback@pld-linux.org>
