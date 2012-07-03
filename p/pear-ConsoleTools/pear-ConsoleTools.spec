%define pear_name ConsoleTools

Name: pear-%pear_name
Version: 1.6.1
Release: alt2

Summary: Set of classes to do different actions with the console

License: New BSD
Group: Development/Other
Url: http://ezcomponents.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://components.ez.no/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
A set of classes to do different actions with the console (also called shell).
It can render a progress bar, tables and a status bar and contains a class for
parsing command line options.

%prep
%setup -c
# Hack
%__subst "s|components.ez.no|pear.php.net|g" package.xml

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
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_dir/ezc
%pear_xmldir/%pear_name.xml

%changelog
* Mon Dec 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt2
- cleanup spec
- build for ALT Linux Sisyphus

* Mon Dec 27 2010 Konstantin Pavlov <thresh@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.

