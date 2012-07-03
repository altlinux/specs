%define pear_name Net_Socket

Name: pear-Net_Socket
Version: 1.0.9
Release: alt1

Summary: Network Socket Interface
License: PHP
Group: Development/Other

Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>
Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch
Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
%setup -c -n %pear_name-%version

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

%changelog
* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- new version (1.0.9) import in git (ALT bug #15965)

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.0.8-alt1
- Initial build for ALT Linux

