%define m_distro Test-Strict
Name: perl-Test-Strict
Version: 0.14
Release: alt2
Summary: Check syntax, presence of use strict; and test coverage

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~pdenis/Test-Strict/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Test-Pod-Coverage perl-Test-Pod perl-CGI perl-devel perl-Devel-Cover perl-Storable perl-B-Debug

%description
%summary

%prep
%setup -q -n %m_distro-%version
# fix test 04
mkdir cover_db

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Strict*
%doc Changes README 

%changelog
* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- added perl-B-Debug to buildreq to fix build

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
