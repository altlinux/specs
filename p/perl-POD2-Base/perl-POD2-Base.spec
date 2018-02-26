%define m_distro POD2-Base
Name: perl-POD2-Base
Version: 0.043
Release: alt1
Summary: POD2::Base - Base module for translations of Perl documentation

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~ferreira/POD2-Base/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POD2/Base*
%perl_vendor_privlib/POD2/PT/POD2/Base.pod
%doc Changes README 

%changelog
* Tue Feb 15 2011 Vladimir Lettiev <crux@altlinux.ru> 0.043-alt1
- initial build
