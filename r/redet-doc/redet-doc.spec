Name: redet-doc
Version: 8.25
Release: alt1

Summary: Documentation for redet

License: GPL
Group: Text tools
Url: http://www.billposer.org/Software/redet.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: http://www.billposer.org/Software/Downloads/redet_manual-%version.tar.gz
Source: %name-%version.tar

%description
Documentation for Redet

%prep
%setup

%install
%makeinstall_std PREFIX=%prefix

%files
%doc %_datadir/Redet

%changelog
* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 8.25-alt1
- new version 8.25 (with rpmrb script)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 8.23-alt1
- new version 8.23 (with rpmrb script)

* Thu Feb 02 2006 Vitaly Lipatov <lav@altlinux.ru> 8.6-alt0.1
- new version

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 8.3-alt0.1
- initial build for ALT Linux Sisyphus

