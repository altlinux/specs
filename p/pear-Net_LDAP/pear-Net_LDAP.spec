%define pear_name Net_LDAP

Name: pear-Net_LDAP
Version: 1.1.2
Release: alt1

Summary: Object oriented interface for searching and manipulating LDAP-entries

License: GPL License
Group: Development/Other
Url: http://pear.php.net/package/Net_LDAP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_LDAP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Net_LDAP is a clone of Perls Net::LDAP object interface to
directory servers. It does contain most of Net::LDAPs features
but has some own too.

With Net_LDAP you have:
 * A simple object-oriented interface to connections,
   searches entries and filters.
 * Support for tls and ldap v3.
 * Simple modification, deletion and creation of ldap entries.
 * Support for schema handling.

Net_LDAP layers itself on top of PHP's existing ldap extensions.

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
%pear_testdir/Net_LDAP/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

