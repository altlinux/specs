%define pear_name HTTP_Client
Name: pear-%pear_name
Version: 1.2.1
Release: alt1

Summary: Easy way to perform multiple HTTP requests and process their results

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>
# git-cvsimport -v -d :pserver:cvsread@cvs.php.net:/repository pear/HTTP_Client
Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core pear-HTTP_Request
BuildRequires: pear-core rpm-build-pear

%description
The HTTP_Client class wraps around HTTP_Request and provides a higher
level interface for performing multiple HTTP requests.

Features:
* Manages cookies and referrers between requests
* Handles HTTP redirection
* Has methods to set default headers and request parameters
* Implements the Subject-Observer design pattern: the base class sends 
events to listeners that do the response processing.

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version (1.2.1) import in git from tarball

* Fri Jul 04 2008 Denis Klimov <zver@altlinux.ru> 1.1.1-alt3
- new version (ALT bug #14999)

* Thu Oct 04 2007 Denis Klimov <zver@altlinux.ru> 1.1.1-alt2
- fix files section
- add requires pear-HTTP_Request

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.1.1-alt1
- Initial build for ALT Linux

