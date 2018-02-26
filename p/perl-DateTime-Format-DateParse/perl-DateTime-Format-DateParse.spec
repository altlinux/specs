%define dist DateTime-Format-DateParse
Name: perl-%dist
Version: 0.05
Release: alt1.1

Summary: Parses Date::Parse compatible formats
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-0.05.tar.gz
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue May 04 2010
BuildRequires: perl-DateTime perl-Module-Build perl-TimeDate

%description
This module is a compatibility wrapper around Date::Parse.

%prep
%setup -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DateTime/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- 0.04 -> 0.05

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- DateParse.pm: applied nanoseconds patch from rt.cpan.org #52598

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.04-alt1
- initial build for Sisyphus

