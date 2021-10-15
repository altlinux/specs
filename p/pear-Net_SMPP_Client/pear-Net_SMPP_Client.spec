# spec file for PEAR PHP package Net_SMPP_Client
#

%define pear_name Net_SMPP_Client

Name: pear-%pear_name
Version: 0.4.1
Release: alt2

Summary: PHP/PEAR class for SMPP v3.4 client

License: PHP License 3.0
Group: Development/Other
Url: http://pear.php.net/package/Net_SMPP_Client
#Url: https://github.com/pear/Net_SMPP_Client

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %pear_name-%version.tar

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear
Requires: pear-core pear-Net_Socket pear-Net_SMPP

%description
Net_SMPP_Client is a package for communicating with SMPP servers,
built with Net_SMPP. It can be used to send SMS messages, among
other things.

Features:
- PDU stack keeps track of which PDUs have crossed the wire
- Keeps track of the connection state, and won't let you send PDUs if
the state is incorrect.
- Supports SMPP vendor extensions.

%prep
%setup -n %pear_name-%version

mkdir %pear_name-%version

mv -- Net docs %pear_name-%version/
cp -a -- README %pear_name-%version/

# Fix md5 sums:
sed -e 's/bad3bc320f68515595d008ddd51a0829/8e26dcc5c1cb6f820b8319be825aab3a/' -i package.xml
sed -e 's/695c519b637cb658ad84f3584cbac78e/be0b5a47576388e51a99b5ccd1fdce99/' -i package.xml

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc README CHANGELOG LICENSE
%pear_xmldir/%pear_name.xml
%exclude %pear_dir/data/*
%pear_dir/Net*
%pear_dir/docs*

%changelog
* Fri Oct 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.4.1-alt2
- Fix build with pear-core 1.10.13

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1-alt1
- New version

* Fri Aug 10 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
