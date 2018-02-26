%define dist Devel-Trace
Name: perl-%dist
Version: 0.11
Release: alt2

Summary: Print out each line before it is executed
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
