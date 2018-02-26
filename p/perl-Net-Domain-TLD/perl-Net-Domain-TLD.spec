%define dist Net-Domain-TLD

Name: perl-%dist
Version: 1.69
Release: alt1

Summary: Gives ability to retrieve currently available TLD
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXP/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 20 2011
BuildRequires: perl-devel

%description
The purpose of this module is to provide user with current list of available
top level domain names including new ICANN additions and ccTLDs

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/Domain

%changelog
* Wed Apr 20 2011 Victor Forsiuk <force@altlinux.org> 1.69-alt1
- 1.69

* Fri Aug 11 2006 Alexey Tourbin <at@altlinux.ru> 1.65-alt1
- 1.5 -> 1.65

* Mon Aug 30 2004 Alexey Tourbin <at@altlinux.ru> 1.5-alt1
- initial revision (needed by perl-Email-Valid, which is needed by otrs)
