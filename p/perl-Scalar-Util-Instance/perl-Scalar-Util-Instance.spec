# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Benchmark.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Data/Util.pm) perl(Devel/PPPort.pm) perl(DynaLoader.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Find.pm) perl(FindBin.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Params/Util.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(mro.pm)
# END SourceDeps(oneline)
%define module_version 0.001
%define module_name Scalar-Util-Instance
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001
Release: alt2.1.1.1.1
Summary: Generates and installs is-a predicates
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/G/GF/GFUJI/%module_name-%module_version.tar.gz

%description
Scalar::Util::Instance provides is-a predicates to look up.an is-a hierarchy for specific classes. This is an alternative to
`blessed($obj) && $obj->isa(...)', but is significantly faster than it.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2.1
- rebuild with new perl 5.20.1

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

