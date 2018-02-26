%define dist Spiffy
Name: perl-%dist
Version: 0.30
Release: alt2

Summary: Spiffy Perl Interface Framework For You
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Filter perl-Module-Install

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It
attempts to fix all the nits and warts of traditional Perl OO, in a
clean, straightforward and (perhaps someday) standard way.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Spiffy*

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.30-alt2
- rebuilt

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- initial revision
