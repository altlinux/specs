%define pear_name Auth_SASL
Name: pear-Auth_SASL
Version: 1.0.4
Release: alt1

Summary: Abstraction of various SASL mechanism responses
License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>
# git-cvsimport -v -d :pserver:cvsread@cvs.php.net:/repository pear/Auth_SASL
Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch
Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides code to generate responses to common SASL mechanisms, including:
o Digest-MD5
o CramMD5
o Plain
o Anonymous
o Login (Pseudo mechanism)

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
%doc LICENSE CHANGELOG
%pear_dir/Auth/*
%pear_xmldir/%pear_name.xml

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version (1.0.4) import in git from tarball

* Wed Mar 19 2008 Denis Klimov <zver@altlinux.ru> 1.0.2-alt2
- using pear macros (ALT bug #14999)
- files section was rewrite

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.0.2-alt1
- Initial build for ALT Linux

