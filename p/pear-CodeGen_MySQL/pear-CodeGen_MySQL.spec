%define pear_name CodeGen_MySQL

Name: pear-CodeGen_MySQL
Version: 1.0.0RC1
Release: alt1

Summary: Abstract base package for MySQL code generators

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.0b1

%description
This package contains common functionality used by all MySQL
  related code generator packages. It is not functionally by
  itself though, it just serves as an implementation framework
  for MySQL related code generator packages just like CodeGen
  does for code generator packages in general.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_datadir/CodeGen_MySQL/
%pear_dir/CodeGen/MySQL/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0RC1-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

