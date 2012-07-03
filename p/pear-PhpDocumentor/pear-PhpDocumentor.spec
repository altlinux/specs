%define pear_name PhpDocumentor

Name: pear-PhpDocumentor
Version: 1.4.2
Release: alt1

Summary: The phpDocumentor package provides automatic documenting of php api directly from the source.

License: LGPL
Group: Development/Other
URL: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%{version}.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear


%description
The phpDocumentor tool is a standalone auto-documentor similar to
JavaDoc written in PHP.  It differs from PHPDoc in that it is MUCH faster,
parses a much wider range of php files, and comes with many customizations
including 11 HTML templates, windows help file CHM output, PDF output, and
XML DocBook peardoc2 output for use with documenting PEAR.  In addition,
it can do PHPXref source code highlighting and linking.

%prep
%setup -c -n %pear_name-%version
%pear_prepare_module

%install
%pear_install_module

%post
%pear_install

%preun
%pear_uninstall

%files
%doc LICENSE CHANGELOG
%pear_datadir/PhpDocumentor/
%pear_dir/PhpDocumentor/
#%_bindir/scripts/makedoc.sh
%_bindir/phpdoc
%pear_testdir/PhpDocumentor/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Jan 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Linux Sisyphus

