%define pear_name Net_Geo

Name: pear-Net_Geo
Version: 1.0.4
Release: alt3

Summary: Geographical locations based on Internet address

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_Geo

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Geo-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Cache, pear-XML_Serializer

%description
Obtains geographical information based on IP number, domain name,
or AS number. Makes use of CAIDA Net_Geo lookup, HostIP or
localizer extension.

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
%doc LICENSE CHANGELOG
%pear_dir/Net
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus

