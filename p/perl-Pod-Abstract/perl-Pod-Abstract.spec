%define m_distro Pod-Abstract
Name: perl-Pod-Abstract
Version: 0.20
Release: alt1.1
Summary: Abstract document tree for Perl POD documents

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~blilburne/Pod-Abstract/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Task-Weaken perl-IO-String
BuildRequires: perl-Pod-Parser

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/paf
%_man1dir/paf*
%perl_vendor_privlib/Pod/Abstract*
%doc Changes README 

%changelog
* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1.1
- rebuilt with perl 5.12

* Mon Jan 25 2010 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- initial build
