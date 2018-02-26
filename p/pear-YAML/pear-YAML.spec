%define pear_name YAML

Name: pear-%pear_name
Version: 1.0.4
Release: alt1

Summary: The Symfony YAML Component

License: BSD
Group: Development/Other
Url: http://pear.symfony-project.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.symfony-project.com/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Symfony YAML Component.

%prep
%setup -c
# Hack against Unknown channel
%__subst "s|pear.symfony-project.com|pear.php.net|g" package.xml

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
%pear_dir/SymfonyComponents/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Tue Dec 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus

