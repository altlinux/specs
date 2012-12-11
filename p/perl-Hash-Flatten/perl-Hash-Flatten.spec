# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Hash-Flatten
Version:        1.19
Release:        alt3_7
Summary:        Flatten/unflatten complex data hashes
License:        GPLv2
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Hash-Flatten/
Source0:        http://www.cpan.org/authors/id/B/BB/BBC/Hash-Flatten-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Log/Trace.pm)
BuildRequires:  perl(Test/Assertions.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
Converts back and forth between a nested hash structure and a flat hash of
delimited key-value pairs. Useful for protocols that only support key-value
pairs (such as CGI and DBMs).

%prep
%setup -q -n Hash-Flatten-%{version}

# fix file encoding
iconv --from=ISO-8859-1 --to=UTF-8 Changes >Changes.tmp && mv Changes.tmp Changes

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2_5
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_5
- fc import

