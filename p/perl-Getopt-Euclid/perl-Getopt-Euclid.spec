%define dist Getopt-Euclid
Name: perl-%dist
Version: 0.3.2
Release: alt1

Summary: Executable Uniform Command-Line Interface Descriptions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Module-Build perl-Perl-Tidy perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Balanced

%description
Getopt::Euclid uses your program's own documentation to create a command-line
argument parser. This ensures that your program's documented interface and
its actual interface always agree.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Getopt

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.3.2-alt1
- 0.2.3 -> 0.3.2

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.2.3-alt1
- initial revision
