%define dist AppConfig-Std
Name: perl-%dist
Version: 1.07
Release: alt2

Summary: Subclass of AppConfig that provides standard options
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-AppConfig perl-Pod-Parser perl-devel

%description
AppConfig::Std is a Perl module that provides a set of standard
configuration variables and command-line switches.  It is implemented
as a subclass of AppConfig; AppConfig provides a general mechanism for
handling global configuration variables.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/AppConfig

%changelog
* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 1.07-alt2
- fixed unpackaged directory

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1.1
- rebuilt with perl 5.12

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt1
- initial build for ALT Linux Sisyphus
