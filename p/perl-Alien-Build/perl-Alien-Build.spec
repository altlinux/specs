%define _unpackaged_files_terminate_build 1
# Alien-MSYS: Tools required for automake scripts in Windows
%filter_from_requires /^perl.Alien.MSYS.pm/d
%filter_from_requires /^perl.Alien.gmake.pm/d
%filter_from_requires /^perl.PkgConfig.pm/d
%filter_from_requires /^perl.PkgConfig.LibPkgConf.Client.pm/d
%filter_from_requires /^perl.PkgConfig.LibPkgConf.Util.pm/d

%define perl_bootstrap 0
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
#BuildRequires: perl(FFI/Platypus.pm) perl(PkgConfig.pm)
BuildRequires: gcc-c++ perl(AnyEvent.pm) perl(Inline.pm) perl(Module/Build.pm) perl(Mojo/JSON.pm) perl(Mojo/URL.pm) perl(Mojolicious/Lite.pm) perl(Net/SSLeay.pm) perl(Proc/Daemon.pm) perl(autodie.pm) perl-podlators cmake
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%{bcond_without perl_Alien_Build_enables_optional_test}

Name:           perl-Alien-Build
Version:        2.75
Release:        alt1
Summary:        Build external dependencies for use in CPAN
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Alien-Build/
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz
# Support only the most advanced pkgconfig implementation,
# the files are deleted in prep section
Patch0:         Alien-Build-1.32-Remove-redundant-pkgconfig-implementations.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
%if !%{defined perl_bootstrap}
# Build cycle: perl-Alien-cmake3 a.. perl-Alien-Build
BuildRequires:  perl(Alien/cmake3.pm)
%endif
# Archive::Tar or (tar and bzip2 and gzip and xz)
BuildRequires:  perl(Archive/Tar.pm)
# Archive::Zip or unzip
BuildRequires:  perl(Archive/Zip.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Config/INI/Reader/Multiline.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(Env.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(FFI/CheckLib.pm)
# FFI::Platypus is optional and not packaged
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/BOM.pm)
BuildRequires:  perl(File/chdir.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(JSON/PP.pm)
BuildRequires:  perl(Module/Load.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Path/Tiny.pm)
# Alien::Build::Plugin::PkgConfig::Negotiate finds a pkgconfig implementation
# in this order:
# PkgConfig::LibPkgConf 0.04, pkgconf, pkg-config, PkgConfig 0.14026
# We selected the most advanced PkgConfig::LibPkgConf and removed the other
# plugins.
#BuildRequires:  perl(PkgConfig/LibPkgConf/Client.pm)
#BuildRequires:  perl(PkgConfig/LibPkgConf/Util.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Test2/API.pm)
BuildRequires:  perl(Test2/Require.pm)
BuildRequires:  perl(Text/ParseWords.pm)
# YAML or Data::Dumper
BuildRequires:  perl(YAML.pm)
# Tests:
# AnyEvent not used
# AnyEvent::FTP::Server not used
BuildRequires:  perl(File/Glob.pm)
# Getopt::Long not used
# IO::Socket::INET not used
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
# Mojo::JSON not used
# Mojo::URL not used
# Mojolicious::Lite not used
BuildRequires:  perl(Net/FTP.pm)
# Proc::Daemon not used
BuildRequires:  perl(Test2/Mock.pm)
BuildRequires:  perl(Test2/Require/Module.pm)
BuildRequires:  perl(Test2/V0.pm)
# URI not used
%if %{with perl_Alien_Build_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: Acme::Alien::DontPanic a.. Test::Alien
BuildRequires:  perl(Acme/Alien/DontPanic.pm)
%endif
BuildRequires:  perl(Alien/Base/ModuleBuild.pm)
BuildRequires:  perl(Alien/Base/PkgConfig.pm)
BuildRequires:  perl(Devel/Hide.pm)
BuildRequires:  perl(Env/ShellWords.pm)
# FFI::Platypus not packaged
BuildRequires:  perl(HTTP/Tiny.pm)
# PkgConfig not packaged
BuildRequires:  perl(Readonly.pm)
BuildRequires:  perl(Sort/Versions.pm)
BuildRequires:  perl(URI/file.pm)
%endif
# make in the lib/Alien/Build/Plugin/Build/CMake.pm plugin
# make in the lib/Alien/Build/Plugin/Build/Make.pm plugin
# make or Alien::gmake
Requires:       curl
%if !%{defined perl_bootstrap}
# Build cycle: perl-Alien-cmake3 a.. perl-Alien-Build
Requires:       perl(Alien/cmake3.pm) >= 0.020
%endif
# Archive::Tar or (tar and bzip2 and gzip and xz)
Requires:       perl(Archive/Tar.pm)
# Archive::Zip or unzip
Requires:       perl(Archive/Zip.pm)
Requires:       perl(Config/INI/Reader/Multiline.pm)
Requires:       perl(DynaLoader.pm)
Requires:       perl(ExtUtils/CBuilder.pm)
Requires:       perl(ExtUtils/ParseXS.pm) >= 3.300
Requires:       perl(FFI/CheckLib.pm)
Requires:       perl(File/BOM.pm)
Requires:       perl(File/Find.pm)
Requires:       perl(Path/Tiny.pm) >= 0.077
# Alien::Build::Plugin::PkgConfig::Negotiate finds a pkgconfig implementation
# in this order:
# PkgConfig::LibPkgConf 0.04, pkgconf, pkg-config, PkgConfig 0.14026
# We selected the most advanced PkgConfig::LibPkgConf and removed the other
# plugins.
#Requires:       perl(PkgConfig/LibPkgConf/Client.pm) >= 0.040
#Requires:       perl(PkgConfig/LibPkgConf/Util.pm) >= 0.040
Requires:       perl(Storable.pm)
Requires:       perl(Test2/API.pm) >= 1.302.015
Requires:       perl(Test2/Require.pm) >= 0.000.060
Requires:       perl(Text/ParseWords.pm) >= 3.260
# YAML or Data::Dumper
Requires:       perl(YAML.pm)
Requires:       wget
# Alien::Base::PkgConfig moved from perl-Alien-Base-ModuleBuild
Conflicts:      perl-Alien-Base-ModuleBuild < 1.00

# Do not gather dependencies from the documentation


# Remove underspecified dependencies

Source44: import.info
%filter_from_requires /^perl\\((Capture.Tiny|Path.Tiny|Test2.API|Test2.Require|Text.ParseWords).pm\\)$/d

%description
This package provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at run time.

%prep
%setup -q -n Alien-Build-%{version}
# Remove redundant pkgconfig implementations, keep
# Alien::Build::Plugin::PkgConfig::LibPkgConf,
# MANIFEST is updated by Remove-redundant-pkgconfig-implementations.patch
#patch0 -p1
# lib/Alien/Build/Plugin/PkgConfig/{CommandLine,PP}.pm 
# rm t/alien_build_plugin_pkgconfig_{commandline,pp}.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%check
make test

%files
%doc author.yml
%doc Changes* example README SUPPORT
%{perl_vendor_privlib}/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.75-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 2.74-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 2.72-alt1
- automated CPAN update

* Thu Oct 06 2022 Igor Vlasenko <viy@altlinux.org> 2.71-alt1
- automated CPAN update

* Tue Sep 27 2022 Igor Vlasenko <viy@altlinux.org> 2.70-alt1
- automated CPAN update

* Wed Sep 07 2022 Igor Vlasenko <viy@altlinux.org> 2.68-alt1.1
- automated CPAN update

* Tue Sep 06 2022 Igor Vlasenko <viy@altlinux.org> 2.68-alt1
- automated CPAN update

* Sun Sep 04 2022 Igor Vlasenko <viy@altlinux.org> 2.67-alt1
- automated CPAN update

* Fri Sep 02 2022 Igor Vlasenko <viy@altlinux.org> 2.66-alt1
- automated CPAN update

* Wed Aug 31 2022 Igor Vlasenko <viy@altlinux.org> 2.65-alt1
- automated CPAN update

* Fri Aug 26 2022 Igor Vlasenko <viy@altlinux.org> 2.59-alt1
- automated CPAN update

* Thu Aug 04 2022 Igor Vlasenko <viy@altlinux.org> 2.51-alt1
- automated CPAN update

* Fri Jun 24 2022 Igor Vlasenko <viy@altlinux.org> 2.50-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 2.48-alt1
- automated CPAN update

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 2.46-alt1
- automated CPAN update

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 2.45-alt1
- automated CPAN update

* Thu Oct 21 2021 Igor Vlasenko <viy@altlinux.org> 2.44-alt1
- automated CPAN update

* Tue Oct 05 2021 Igor Vlasenko <viy@altlinux.org> 2.42-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 2.41-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 2.40-alt1
- automated CPAN update

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1
- automated CPAN update

* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.29-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.26-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1
- automated CPAN update

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1
- automated CPAN update

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Sun Feb 16 2020 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Wed Dec 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.94-alt1
- automated CPAN update

* Wed Dec 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.93-alt1
- automated CPAN update

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.89-alt1
- automated CPAN update

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.86-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.85-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.83-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.79-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.69-alt1
- automated CPAN update

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.68-alt1
- automated CPAN update

* Tue Apr 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Mon Apr 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1
- automated CPAN update

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- automated CPAN update

* Fri Mar 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- automated CPAN update

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1
- automated CPAN update

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- automated CPAN update

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_1
- non-bootstrap build

* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt0_1
- use pkg-config by default (dropped fedora patches)
- first bootstrap build

