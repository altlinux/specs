%define pear_name File_Iterator

Name: pear-File_Iterator
Version: 1.2.3
Release: alt1

Summary: FilterIterator implementation that filters files based on a list of suffixes

License: BSD
Group: Development/Other
Url: http://pear.phpunit.de/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
FilterIterator implementation that filters files based on a list of suffixes.

%prep
%setup -c
# Hack against Unknown channel "pear.phpunit.de"
%__subst "s|pear.phpunit.de|pear.php.net|g" package.xml

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
%pear_dir/File/Iterator/
%pear_dir/File/Iterator.php
%pear_xmldir/%pear_name.xml

%changelog
* Mon Dec 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- initial build for ALT Linux Sisyphus

