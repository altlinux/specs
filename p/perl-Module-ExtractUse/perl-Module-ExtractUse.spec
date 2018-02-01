%define _unpackaged_files_terminate_build 1
%define module_name Module-ExtractUse

Name: perl-%module_name
Version: 0.342
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Find out what Perl modules are used
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source0: http://www.cpan.org/authors/id/D/DO/DOMM/%{module_name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 16 2009
BuildRequires: perl-Module-Build perl-Parse-RecDescent perl-Pod-Strip perl-Test-Deep perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage perl-UNIVERSAL-require

%description
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl code.
It tries very hard to find all modules (whether pragmas, Core, or from CPAN)
used by the parsed code.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE example
%perl_vendor_privlib/Module/

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.342-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.341-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 0.23-alt1
- Initial build.
