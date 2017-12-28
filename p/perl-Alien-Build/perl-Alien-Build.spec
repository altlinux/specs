%filter_from_requires /^perl.Alien.cmake3.pm/d
%filter_from_requires /^perl.Alien.gmake.pm/d
%filter_from_requires /^perl.PkgConfig.pm/d
%filter_from_requires /^perl.PkgConfig.LibPkgConf.Client.pm/d
%filter_from_requires /^perl.PkgConfig.LibPkgConf.Util.pm/d

%define perl_bootstrap 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
#BuildRequires: perl(FFI/Platypus.pm) perl(PkgConfig.pm)
BuildRequires: gcc-c++ perl(AnyEvent.pm) perl(Inline.pm) perl(Module/Build.pm) perl(Mojo/JSON.pm) perl(Mojo/URL.pm) perl(Mojolicious/Lite.pm) perl(Net/SSLeay.pm) perl(Proc/Daemon.pm) perl(autodie.pm) perl-podlators
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
%{bcond_with perl_Alien_Build_enables_optional_test}

Name:           perl-Alien-Build
Version:        1.32
Release:        alt0_1
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
%doc LICENSE
%doc Changes* example README SUPPORT
%{perl_vendor_privlib}/*

%changelog
* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt0_1
- use pkg-config by default (dropped fedora patches)
- first bootstrap build

