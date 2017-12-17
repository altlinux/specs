%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Attribute/Handlers.pm) perl(Benchmark.pm) perl(CPAN.pm) perl(Carp.pm) perl(Class/Method/Modifiers.pm) perl(Config.pm) perl(Data/OptList.pm) perl(Devel/PPPort.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FindBin.pm) perl(Hash/Util/FieldHash/Compat.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Params/Util.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Symbol.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(if.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(parent.pm) perl(Module/Build/XSUtil.pm)
# END SourceDeps(oneline)
%define module_name Data-Util
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.66
Release: alt1.1
Summary: A selection of utilities for data and data types
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SY/SYOHEX/%{module_name}-%{version}.tar.gz
# https://rt.cpan.org/Public/Bug/Display.html?id=99097

%description
This module provides utility functions for data and data types,
including functions for subroutines and symbol table hashes (stashes).

The implementation of this module is both Pure Perl and XS, so if you have a C
compiler, all the functions this module provides are really faster.

There are many benchmarks in the DIST-DIR/benchmark/ directory.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes example
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.63-alt2.1
- rebuild with new perl 5.22.0

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.63-alt2
- fixed build with new perl 5.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.1
- rebuild with new perl 5.20.1

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- initial import by package builder

