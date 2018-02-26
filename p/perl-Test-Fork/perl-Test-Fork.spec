%define m_distro Test-Fork
Name: perl-%m_distro
Version: 0.02
Release: alt1

Summary: test code which forks
License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/~mschwern/%m_distro

Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %m_distro-%version.tar
BuildArch: noarch

BuildRequires: perl-devel perl-Module-Build

%description
Because each test has a number associated with it, testing code which forks is problematic. Coordinating the test number amongst the parent and child processes is complicated. Test::Fork provides a function to smooth over the complications.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Fork*
%doc Changes

%changelog
* Mon Jul 13 2009 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build

