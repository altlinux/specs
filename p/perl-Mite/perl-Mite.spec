%define _unpackaged_files_terminate_build 1
%define module_name Mite
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Child.pm) perl(Class/XSAccessor.pm) perl(Devel/GlobalDestruction.pm) perl(Devel/Hide.pm) perl(ExtUtils/MakeMaker.pm) perl(Fennec.pm) perl(File/Copy/Recursive.pm) perl(Getopt/Kingpin.pm) perl(Import/Into.pm) perl(MRO/Compat.pm) perl(Module/Build.pm) perl(Module/Pluggable.pm) perl(Path/Tiny.pm) perl(Perl/Tidy.pm) perl(Role/Hooks.pm) perl(Role/Tiny.pm) perl(Sub/HandlesVia/CodeGenerator.pm) perl(Test/Compile.pm) perl(Test/Deep.pm) perl(Test/FailWarnings.pm) perl(Test/Most.pm) perl(Test/Output.pm) perl(Test/Sims.pm) perl(Test2/V0.pm) perl(Types/Path/Tiny.pm) perl(Types/Standard.pm) perl(YAML/XS.pm) perl(autodie.pm) perl(namespace/autoclean.pm) perl(parent.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.012000
Release: alt1
Summary: Moose-like OO, fast to load, with zero dependencies.
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Mite

Source0: http://www.cpan.org/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

[ "%version" == "0.012000" ] && rm -f t/Mite-Attribute/isa.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CREDITS Changes COPYRIGHT
%perl_vendor_privlib/M*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Sun Dec 25 2022 Igor Vlasenko <viy@altlinux.org> 0.012000-alt1
- automated CPAN update

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 0.010008-alt1
- automated CPAN update

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.008003-alt1
- automated CPAN update

* Thu Aug 04 2022 Igor Vlasenko <viy@altlinux.org> 0.008002-alt1
- automated CPAN update

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 0.008000-alt1
- automated CPAN update

* Fri Jul 29 2022 Igor Vlasenko <viy@altlinux.org> 0.007006-alt1
- automated CPAN update

* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 0.006013-alt1
- automated CPAN update

* Tue Jul 12 2022 Igor Vlasenko <viy@altlinux.org> 0.006008-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Mon Jul 11 2022 Igor Vlasenko <viy@altlinux.org> 0.006008-alt1
- updated by package builder

* Fri Jul 08 2022 Igor Vlasenko <viy@altlinux.org> 0.005003-alt1
- updated by package builder

* Wed Jul 06 2022 Igor Vlasenko <viy@altlinux.org> 0.005001-alt1
- updated by package builder

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.004000-alt1
- updated by package builder

* Mon Jul 04 2022 Igor Vlasenko <viy@altlinux.org> 0.003001-alt1
- updated by package builder

* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 0.003000-alt1
- updated by package builder

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 0.002002-alt1
- updated by package builder

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.001013-alt1
- updated by package builder

* Thu Jun 30 2022 Igor Vlasenko <viy@altlinux.org> 0.001011-alt1
- updated by package builder

* Mon Jun 27 2022 Igor Vlasenko <viy@altlinux.org> 0.0.8-alt1
- updated by package builder

* Fri Jun 24 2022 Igor Vlasenko <viy@altlinux.org> 0.0.7-alt1
- updated by package builder

* Thu Jun 23 2022 Igor Vlasenko <viy@altlinux.org> 0.0.5-alt1
- updated by package builder

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 0.0.4-alt1
- updated by package builder

* Tue Jun 21 2022 Igor Vlasenko <viy@altlinux.org> 0.0.2-alt1
- updated by package builder

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1
- initial import by package builder

