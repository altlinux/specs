# BEGIN SourceDeps(oneline):
BuildRequires: perl(UNIVERSAL/require.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define module_name Getargs-Long

Name: perl-%module_name
Version: 1.1012
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: %module_name module for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source0: http://www.cpan.org/authors/id/D/DC/DCOPPIT/%{module_name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: perl-Log-Agent perl-Module-Install perl(Test/Compile.pm)

%description
The "Getargs::Long" module allows usage of named parameters in function calls,
along with optional argument type-checking. It provides an easy way to get at
the parameters within the routine, and yields concise descriptions for the
common cases of all-mandatory and all-optional parameter lists.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES LICENSE README
%perl_vendor_privlib/Getargs/

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 1.1012-alt2
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.1012-alt1
- automated CPAN update

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.1010-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.1007-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.1005-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1003-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 1.1003-alt1
- 1.1003

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 1.1001-alt1
- Initial build.
