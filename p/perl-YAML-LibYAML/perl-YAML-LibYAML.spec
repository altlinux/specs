%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(LWP/Simple.pm) perl(Test/Deep.pm) perl(Test/Pod.pm) perl(Text/Diff.pm) perl(YAML.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Filter
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%if ! 0%{?rhel}
%bcond_without perl_YAML_LibYAML_enables_optional_test
%else
%bcond_with perl_YAML_LibYAML_enables_optional_test
%endif

Name:           perl-YAML-LibYAML
Epoch:          1
Version:        0.86
Release:        alt1
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/YAML-LibYAML
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/YAML-LibYAML-%{version}.tar.gz
Patch0:         YAML-LibYAML-0.79-Unbundled-libyaml.patch

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libyaml2 >= 0.2.2
BuildRequires:  libyaml-devel >= 0.2.2
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  sed

# Module
BuildRequires:  perl(B/Deparse.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)

# Tests
BuildRequires:  perl(B.pm)
BuildRequires:  perl(blib.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/Peek.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(Filter/Util/Call.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Pipe.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(utf8.pm)

%if %{with perl_YAML_LibYAML_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Path/Class.pm)
%endif

# Dependencies
Requires:       perl(B/Deparse.pm)
Requires:       libyaml2 >= 0.2.2

# Avoid provides for perl shared objects

Source44: import.info

%description
Kirill Siminov's "libyaml" is arguably the best YAML implementation. The C
library is written precisely to the YAML 1.1 specification. It was originally
bound to Python and was later bound to Ruby.

%prep
%setup -q -n YAML-LibYAML-%{version}
# Unbundled libyaml, the source files are the same as in libyaml-0.2.2
# It was determined by comparing commits in upstream repo:
# https://github.com/yaml/libyaml/
%patch0 -p1 -b .orig
for file in api.c dumper.c emitter.c loader.c parser.c reader.c scanner.c \
    writer.c yaml.h yaml_private.h; do
    rm LibYAML/$file
    sed -i -e "/^LibYAML\/$file/d" MANIFEST
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
find %{buildroot} -type f -name '*.bs' -empty -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes CONTRIBUTING README
%{perl_vendor_archlib}/auto/YAML/
%{perl_vendor_archlib}/YAML/

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 1:0.86-alt1
- automated CPAN update

* Tue Sep 13 2022 Igor Vlasenko <viy@altlinux.org> 1:0.85-alt1
- automated CPAN update

* Sun Sep 04 2022 Igor Vlasenko <viy@altlinux.org> 1:0.84-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 1:0.83-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.82-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.81-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.80-alt1_1
- update to new release by fcimport

* Sun Aug 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.80-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.79-alt1
- automated CPAN update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.78-alt1_1
- update to new release by fcimport

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.78-alt1
- automated CPAN update

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.77-alt1
- automated CPAN update

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.76-alt1.1_1
- update to new release by fcimport

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.76-alt1.1
- rebuild with new perl 5.28.1

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.76-alt1
- automated CPAN update

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.75-alt1_1
- update to new release by fcimport

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.75-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.74-alt1_1
- update to new release by fcimport

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.74-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.72-alt1_1
- update to new release by fcimport

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1.1.1
- rebuild with new perl 5.24.1

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 0.71-alt1_1.1
- E2K: drop gcc-common
- BOOTSTRAP: avoid test BRs when --without check

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1
- update to new release by fcimport

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.41-alt2
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_2
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_1
- update to new release by fcimport

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

