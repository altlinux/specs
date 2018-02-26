%define pear_name MIME_Type

Name: pear-MIME_Type
Version: 1.0.0
Release: alt3

Summary: Utility class for dealing with MIME types

License: PHP License 3.0
Group: Development/Other
Url: http://pear.php.net/package/MIME_Type

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/MIME_Type-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provide functionality for dealing with MIME types.
* Parse MIME type.
* Supports full RFC2045 specification.
* Many utility functions for working with and determining info about
types.
* Most functions can be called statically.
* Autodetect a file's mime-type, either with mime_content_type() or the
'file' command.

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
%pear_dir/MIME
%pear_dir/docs
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

