# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(blib.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Filter
Name:           perl-YAML-LibYAML
Version:        0.38
Release:        alt3_4
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/YAML-LibYAML/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-LibYAML-%{version}.tar.gz
Patch0:         YAML-LibYAML-0.35-format-error.patch

# Install
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)

# Module
BuildRequires:  perl
BuildRequires:  perl(B/Deparse.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(XSLoader.pm)

# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/Peek.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Module.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/Hash.pm)

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
* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt3_4
- Sisyphus release

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.38-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_2
- fc import

