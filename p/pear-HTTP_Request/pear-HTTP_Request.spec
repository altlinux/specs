%define pear_name HTTP_Request
Name: pear-%pear_name
Version: 1.4.4
Release: alt1

Summary: Provides an easy way to perform HTTP requests

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>
# git-cvsimport -v -d :pserver:cvsread@cvs.php.net:/repository pear/HTTP_Request
Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core
Requires: pear-Net_URL >= 1.0.12
Requires: pear-Net_Socket >= 1.0.9
BuildRequires: pear-core rpm-build-pear

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication, SSL, file uploads etc.

This package has been superseded,
but is still maintained for bugs and security fixes. Use HTTP_Request2 instead.

%prep
%setup -c -n %pear_name-%version

%build
%pear_build

%install
%pear_install_std


%post
%register_pear_module

%preun
%unregister_pear_module


%files
%pear_dir/HTTP/
%pear_xmldir/%pear_name.xml
%pear_docdir/%pear_name/

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version (1.4.4) import in git

* Fri Jul 04 2008 Denis Klimov <zver@altlinux.ru> 1.4.2-alt1
- build with pear macros (ALT bug #14999)

* Mon Oct 08 2007 Denis Klimov <zver@altlinux.ru> 1.4.1-alt2
- fix requires with pear-Net_Socket

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.4.1-alt1
- Initial build for ALT Linux

