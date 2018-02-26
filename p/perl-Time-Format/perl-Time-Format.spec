%define dist Time-Format
Name: perl-%dist
Version: 1.11
Release: alt2

Summary: Easy-to-use date/time formatting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Time-Format-1.11-alt-test-manip.patch

BuildArch: noarch

# Manually added by Alexey Tourbin!
Requires: perl-Time-Format_XS

# Automatically added by buildreq on Sun Feb 27 2011
BuildRequires: perl-Date-Manip perl-DateTime perl-Module-Build perl-Time-Format_XS

%description
Time::Format provides a very easy way to format dates and times.
The formatting functions are tied to hash variables, so they can be
used inside strings as well as in ordinary expressions.  The formatting
codes used are meant to be easy to remember, use, and read.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README quickref.txt
%perl_vendor_privlib/Time

%changelog
* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt2
- fixed tests for Date::Manip
- added dependency on on perl-Time-Format_XS

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.11-alt1
- New version 1.11

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt1
- New version 1.09

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt0
- Initial build
