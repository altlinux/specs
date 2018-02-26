%define m_distro Test-Requires
Name: perl-Test-Requires
Version: 0.06
Release: alt1
Summary: Test::Requires checks to see if the module can be loaded

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~tokuhirom/Test-Requires/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel

%description
Test::Requires checks to see if the module can be loaded.
If this fails rather than failing tests this skips all tests.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Requires*
%doc Changes README 

%changelog
* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- New version 0.06

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
