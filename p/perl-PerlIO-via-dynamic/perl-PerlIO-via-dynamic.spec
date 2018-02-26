%define dist PerlIO-via-dynamic
Name: perl-%dist
Version: 0.13
Release: alt1

Summary: Dynamic PerlIO layers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-devel

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers. It is
useful when the behavior or the layer depends on variables. You should
not use this module as via layer directly (ie :via(dynamic)).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# disable perl-5.10.0-only dependency
%filter_from_requires /^perl.Internals/d

%files
%doc README CHANGES
%perl_vendor_privlib/PerlIO

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.11 -> 0.13

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt2
- fix directory ownership violation

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- initial build for ALT Linux Sisyphus
