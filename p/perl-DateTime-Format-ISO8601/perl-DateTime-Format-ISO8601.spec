%define module DateTime-Format-ISO8601

Name: perl-%module
Version: 0.08
Release: alt1

Summary: Perl module that parses ISO8601 formats
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHOBLITT/DateTime-Format-ISO8601-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-DateTime-Format-Builder perl-File-Find-Rule perl-Module-Build perl-Test-Distribution perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module that parses almost all ISO8601 date and time formats.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/DateTime/*

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.08-alt1
- 0.08

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.07-alt1
- 0.07

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 0.06-alt2
- Fix tests that will only succeed when running before 2010 year.

* Mon Aug 11 2008 Victor Forsyuk <force@altlinux.org> 0.06-alt1
- Initial build.
