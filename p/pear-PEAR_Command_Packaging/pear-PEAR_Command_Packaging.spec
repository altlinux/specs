%define pear_name PEAR_Command_Packaging
%define oversion 0.1.2

Name: pear-PEAR_Command_Packaging
Version: %{oversion}a
Release: alt2

Summary: make-rpm-spec command for managing RPM .spec files for PEAR packages

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.pear.php.net/package/%pear_name-%version.tar.bz2

BuildArch: noarch
Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This command is an improved implementation of the standard makerpm command,
and contains several enhancements that make it far more flexible. Similar
functions for other external packaging mechanisms may be added at a later date.

Enhanced features over the original PEAR "makerpm" command include:

- Ability to define a release on the command line
- Allows more advanced customisation of the generated package name
- Allows virtual Provides/Requires that differ in format from the package name
format
- tries to intelligently distinguish between PEAR and PECL when generating
packages

This command patched for ALT Policy spec generated (see rpm-build-pear package).

%prep
%setup -c -n %pear_name-%version
# fix version
mv %pear_name-%oversion %pear_name-%version

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%pear_dir/PEAR/Command/Packaging.php
%pear_dir/PEAR/Command/Packaging.xml
%pear_xmldir/%pear_name.xml
%pear_datadir/%pear_name/

%changelog
* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.2a-alt2
- fix php package name
- do no require base pear package as pear-PEAR
- update according to rpm-build-pear 0.3

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.2a-alt1
- patched for ALT Linux spec policy

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- initial build for ALT Linux Sisyphus
