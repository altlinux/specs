%define pear_name Text_Diff

Name: pear-Text_Diff
Version: 1.1.1
Release: alt2

Summary: Generate and display difference analysis between files/strings

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Pavel Isopenko <pauli@altlinux.org>

Source: http://download.pear.php.net/package/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core

BuildPreReq: rpm-build-pear
BuildRequires: pear-core php7-xdebug rpm-build-pear


%description
Text_Diff helps you generating difference views between two or three text files
http://pear.php.net/manual/

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
# %doc LICENSE CHANGELOGOD
%pear_dir/Text/Diff/
%pear_dir/Text/Diff.php
%pear_dir/Text/Diff3.php
%pear_docdir/Text_Diff/docs
%pear_testdir/Text_Diff/tests
%pear_xmldir/%pear_name.xml

%changelog
* Sat Mar 09 2019 Pavel isopenko <pauli@altlinux.org> 1.1.1-alt2
- switch to php7

* Thu Apr 11 2013 Pavel Isopenko <pauli@altlinux.org> 1.1.1-alt1
- initial build for ALT Linux Sisyphus


