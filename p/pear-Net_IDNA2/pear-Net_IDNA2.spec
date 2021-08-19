%define pear_name Net_IDNA2
Name: pear-%pear_name
Version: 0.2.0
Release: alt1

Summary: Punycode encoding and decoding

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package helps you to encode and decode punycode strings easily.

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
#pear_docdir/%pear_name/
%pear_testdir/%pear_name/

%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Sun Nov 22 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus

