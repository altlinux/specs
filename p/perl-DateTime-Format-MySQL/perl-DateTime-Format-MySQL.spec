# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# Note:  Some tests for this package are disabled by default, as they
# require network access and would thus fail in the buildsys' mock
# environments.  To build locally while enabling tests, either:
#
#   rpmbuild ... --define '_with_network_tests 1' ...
#   rpmbuild ... --with network_tests ...
#   define _with_network_tests 1 in your ~/.rpmmacros
#
# Note that right now, the only way to run tests locally from a cvs sandbox
# "make noarch" type scenario is the third one.


Name:           perl-DateTime-Format-MySQL
Version:        0.04        
Release:        alt2_17
Summary:        Parse and format MySQL dates and times 

Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DateTime-Format-MySQL
Source0: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-Format-MySQL-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  perl(Module/Build.pm) perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(Test/More.pm)

# not picked up explicitly, for whatever reason...
Requires:  perl(DateTime/Format/Builder.pm)

# for signature checking
%{?_with_network_tests:BuildRequires: perl(Module/Signature.pm)}
Source44: import.info


%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in order
to create DateTime objects, and it can take a DateTime object and produce a
string representing it in the MySQL format.


%prep
%setup -q -n DateTime-Format-MySQL-%{version}

# digital signature checking.  Not essential, but nice
%{?_with_network_tests: cpansign -v }


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}


%install

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'



%check
make test


%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_17
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_17
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_15
- fc import

