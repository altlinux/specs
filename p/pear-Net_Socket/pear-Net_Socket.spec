%define pear_name Net_Socket

Name: pear-Net_Socket
Version: 1.2.2
Release: alt1

Summary: Network Socket Interface

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

# Source-url: http://pear.php.net/get/%pear_name-%version.tgz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-pear
BuildRequires: pear-core

Requires: pear-core

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%pear_dir/Net/
%pear_xmldir/%pear_name.xml
%pear_docdir/%pear_name/

%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt1
- new version 1.0.14 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1
- new version 1.0.12 (with rpmrb script)

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- new version (1.0.9) import in git (ALT bug #15965)

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.0.8-alt1
- Initial build for ALT Linux

