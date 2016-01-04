%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(IO/All.pm) perl(List/Util.pm) perl(MRO/Compat.pm) perl(Pod/Usage.pm) perl(Test/Manifest.pm) perl(Test/Run/Base.pm) perl(Test/Run/Iface.pm) perl(Test/Run/Obj.pm) perl(Test/Run/Trap/Obj.pm) perl(base.pm) perl-base perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Test-Run-CmdLine
%define upstream_version 0.0130

Name:       perl-%{upstream_name}
Version:    0.0130
Release:    alt1

Summary:    Command line front-end for Test-Run
License:    MIT
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/S/SH/SHLOMIF/Test-Run-CmdLine-%{version}.tar.gz

# These Requirs are not detected automatically, so we need to add them manually.
Requires:   perl(MooseX/Getopt/Basic.pm)
Requires:   perl(MooseX/Getopt.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Getopt.pm)
BuildRequires: perl(MooseX/Getopt/Basic.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Run/Core.pm)
BuildRequires: perl(Test/Trap.pm)
BuildRequires: perl(UNIVERSAL/require.pm)
BuildRequires: perl(YAML/XS.pm)
BuildArch:  noarch
Source44: import.info

%description
This is a module implementing a standalone command line application. It was
created to replace the use of the 'runprove' executable which is not always
installed or available in the path.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README examples
%{_mandir}/man1/*
%perl_vendor_privlib/*
/usr/bin/runprove

%changelog
* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.0130-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.0128-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0126-alt1
- automated CPAN update

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.0125-alt3_3
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.0125-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.0125-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0125-alt1_2
- mgaimport update

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.0125-alt1_1
- converted for ALT Linux by srpmconvert tools

