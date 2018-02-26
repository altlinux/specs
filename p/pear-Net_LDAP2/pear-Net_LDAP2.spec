%define pear_name Net_LDAP2

Name: pear-Net_LDAP2
Version: 2.0.10
Release: alt1

Summary: Object oriented interface for searching and manipulating LDAP-entries

License: LGPLv3 License
Group: Development/Other
URL: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%{version}.tar.bz2

BuildArch: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear



%description
Net_LDAP2 is the successor of Net_LDAP which is a clone of Perls Net::LDAP
object interface to directory servers. It does contain most of Net::LDAPs
features but has some own too.

With Net_LDAP2 you have:
 * A simple object-oriented interface to connections, searches entries and filters.
 * Support for tls and ldap v3.
 * Simple modification, deletion and creation of ldap entries.
 * Support for schema handling.

Net_LDAP2 layers itself on top of PHP's existing ldap extensions.

%prep
%setup -c
%pear_prepare_module

%install
%pear_install_module

%post
%pear_install

%preun
%pear_uninstall

%files
%doc LICENSE CHANGELOG
%pear_dir/Net/LDAP2/Entry.php
%pear_dir/Net/LDAP2/Filter.php
%pear_dir/Net/LDAP2/RootDSE.php
%pear_dir/Net/LDAP2/Schema.php
%pear_dir/Net/LDAP2/Search.php
%pear_dir/Net/LDAP2/Util.php
%pear_dir/Net/LDAP2/LDIF.php
%pear_dir/Net/LDAP2/SchemaCache.interface.php
%pear_dir/Net/LDAP2/SimpleFileSchemaCache.php
%pear_dir/Net/LDAP2.php
%pear_testdir/Net_LDAP2/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Sep 09 2010 Timur Batyrshin <erthad@altlinux.org> 2.0.10-alt1
- Initial build for sisyphus

