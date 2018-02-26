%define pear_name HTTP_Download

Name: pear-HTTP_Download
Version: 1.1.3
Release: alt3

Summary: Send HTTP Downloads

License: BSD, revised
Group: Development/Other
Url: http://pear.php.net/package/HTTP_Download

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTTP_Download-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTTP_Header

%description
Provides an interface to easily send hidden files or any arbitrary data to
HTTP clients.  HTTP_Download can gain its data from variables, files or
stream resources.

It features:
 - Basic caching capabilities
 - Basic throttling mechanism
 - On-the-fly gzip-compression
 - Ranges (partial downloads and resuming)
 - Delivery of on-the-fly generated archives through Archive_Tar and
Archive_Zip
 - Sending of PgSQL LOBs without the need to read all data in prior to
sending

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
%pear_dir/HTTP
%pear_testdir/HTTP_Download/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- initial build for ALT Linux Sisyphus

