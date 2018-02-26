%define pear_name Net_Traceroute

Name: pear-Net_Traceroute
Version: 0.21.1
Release: alt1

Summary: Execute traceroute

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_Traceroute

Packager: Maxim Ivanov <ivanov at altlinux.org>

Source: http://pear.php.net/get/Net_Traceroute-%version.tgz

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
OS independet wrapper class for executing traceroute calls

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
* Sun Jun 08 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.21.1-alt1
- Initial build for Sisyphus 

