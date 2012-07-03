%define pear_name Net_URL
Name: pear-%pear_name
Version: 1.0.15
Release: alt2

Summary: Easy parsing of Urls

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>
# git-cvsimport -v -d :pserver:cvsread@cvs.php.net:/repository pear/Net_URL
Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides easy parsing of URLs and their constituent parts.

This package has been superseded,
but is still maintained for bugs and security fixes. Use Net_URL2 instead.

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
%pear_dir/Net/
%pear_xmldir/%pear_name.xml
%pear_docdir/%pear_name/

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt2
- rewrite spec with using rpm-build-pear's macros

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.0.15-alt1
- Initial build for ALT Linux

