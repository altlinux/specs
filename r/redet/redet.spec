Name: redet
Version: 8.23
Release: alt1

Summary: redet - regular expression development and execution tool

License: GPL
Group: Text tools
Url: http://www.billposer.org/Software/redet.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.billposer.org/Software/Downloads/%name-%version.tar.bz2

%description
Redet allows the user to construct regular expressions and test them
against input data by executing any of a variety of search programs,
editors, and programming languages that make use of regular expressions.

Recommended package: redet-doc

%prep
%setup

%build
%__subst "s|local share Redet|share/doc %name-doc-%version|" redet.tcl

%install

install -m755 -D redet.tcl %buildroot/%_bindir/redet
install -m644 -D redet.1 %buildroot/%_man1dir/redet.1

%files
%doc AUTHORS CREDITS README* Sample*
%_bindir/*
%_man1dir/*


%changelog
* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 8.23-alt1
- new version 8.23 (with rpmrb script)
- cleanup spec, fix Source URL
- fix doc path

* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 8.14-alt0.1
- new version 8.14 (with rpmrb script)

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 8.11-alt0.1
- new version (8.11)

* Fri Mar 17 2006 Vitaly Lipatov <lav@altlinux.ru> 8.9-alt0.1
- new version (8.9)

* Thu Mar 02 2006 Vitaly Lipatov <lav@altlinux.ru> 8.8-alt0.1
- new version 8.8

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 8.6.1-alt0.1
- new version

* Thu Feb 02 2006 Vitaly Lipatov <lav@altlinux.ru> 8.6-alt0.1
- new version

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 8.3-alt0.1
- initial build for ALT Linux Sisyphus

