%define dist Devel-Trace
Name: perl-%dist
Version: 0.12
Release: alt1

Summary: Print out each line before it is executed
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MJ/MJD/Devel-Trace-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-devel

%description
If you run your program with "perl -d:Trace program",
this module will print a message to standard error
just before each line is executed (liks "sh -x").

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build </dev/null

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Devel

%changelog
* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt as plain src.rpm

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.10 -> 0.11
- License: Public Domain

* Wed Oct 25 2006 Alexey Tourbin <at@altlinux.ru> 0.10-alt2
- imported sources into git and built with gear
- Trace.pm: autoflush stdout (cpan #22562)

* Sun Mar 20 2005 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- initial revision
