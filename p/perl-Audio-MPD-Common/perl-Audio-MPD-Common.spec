%define dist Audio-MPD-Common
Name: perl-%dist
Version: 2.002
Release: alt1

Summary: Common helper classes for mpd
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JQ/JQUELIN/Audio-MPD-Common-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Module-Build perl-MooseX-Has-Sugar perl-MooseX-Types perl-Readonly perl(String/Formatter.pm)

%description
Depending on whether you're using a POE-aware environment or not,
people wanting to tinker with mpd (Music Player Daemon) will use
either POE::Component::Client::MPD or Audio::MPD.
But even if the run-cores of those two modules differ completely, they
are using the exact same common classes to represent the various mpd
states and information.
Therefore, those common classes have been outsourced to
Audio::MPD::Common.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Audio

%changelog
* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.120881-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 1.110550-alt1
- 0.1.3 -> 1.110550

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.3-alt1
- initial build
