%define dist Module-Runtime
Name: perl-%dist
Version: 0.013
Release: alt1

Summary: Runtime module handling
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Module-Build perl-Params-Classify perl-Test-Pod perl-Test-Pod-Coverage

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt1
- 0.011 -> 0.013

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.011-alt1
- initial revision
