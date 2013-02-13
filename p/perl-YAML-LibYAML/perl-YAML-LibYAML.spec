# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Deparse.pm) perl(CPAN.pm) perl(Config.pm) perl(Devel/Peek.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(Scalar/Util.pm) perl(XSLoader.pm) perl(blib.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Filter
Name:           perl-YAML-LibYAML
Version:        0.39
Release:        alt1_1
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/YAML-LibYAML/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-LibYAML-%{version}.tar.gz
Patch0:         YAML-LibYAML-0.35-format-error.patch

# Install

# Module
BuildRequires:  perl

# Tests

# Runtime

# Avoid provides for perl shared objects

Source44: import.info

%description
Kirill Siminov's "libyaml" is arguably the best YAML implementation. The C
library is written precisely to the YAML 1.1 specification. It was originally
bound to Python and was later bound to Ruby.

%prep
%setup -q -n YAML-LibYAML-%{version}

# Fix format string vulnerabilities (CVE-2012-1152, CPAN RT#46507)
%patch0 -p1

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/YAML/

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_1
- update to new release by fcimport

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt3_4
- Sisyphus release

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.38-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_2
- fc import

