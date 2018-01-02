%define perl_bootstrap 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(autodie.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional tests
%bcond_without perl_Alien_Base_ModuleBuild_enables_optional_test
# Enable SSL support
%bcond_without perl_Alien_Base_ModuleBuild_enables_ssl

Name:           perl-Alien-Base-ModuleBuild
Version:        1.00
Release:        alt2_1
Summary:        Perl framework for building Alien:: modules and their libraries
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Alien-Base-ModuleBuild/
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Base-ModuleBuild-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>
# Run-time:
BuildRequires:  perl(Alien/Base/PkgConfig.pm)
BuildRequires:  perl(Archive/Extract.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Env.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Installed.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/chdir.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/ShareDir.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(HTTP/Tiny.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Net/FTP.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Path/Tiny.pm)
# PkgConfig not used if pkg-config tool is available
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Shell/Config/Generate.pm)
BuildRequires:  perl(Shell/Guess.pm)
BuildRequires:  perl(Sort/Versions.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(Text/ParseWords.pm)
BuildRequires:  perl(URI.pm)
# Optional run-time:
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(HTML/LinkExtor.pm)
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
# IO::Socket::SSL 1.56 not used at tests
# Net::SSLeay 1.49 not used at tests
%endif
# Tests:
# bash for /bin/sh
BuildRequires:  bash sh
BuildRequires:  perl(base.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test2/Mock.pm)
BuildRequires:  perl(Test2/Require/Module.pm)
BuildRequires:  perl(Test2/V0.pm)
BuildRequires:  perl(URI/file.pm)
%if %{with perl_Alien_Base_ModuleBuild_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: Acme::Alien::DontPanic a.. Alien::Base::ModuleBuild
BuildRequires:  perl(Acme/Alien/DontPanic.pm)
BuildRequires:  perl(Inline.pm)
BuildRequires:  perl(Inline/C.pm)
BuildRequires:  perl(Inline/CPP.pm)
%endif
BuildRequires:  perl(LWP/UserAgent.pm)
%endif
Requires:       perl(Alien/Base/PkgConfig.pm) >= 1.200
Requires:     perl(Digest/SHA.pm)
Requires:       perl(File/chdir.pm) >= 0.100.500
Requires:       perl(File/Find.pm)
Requires:       perl(File/ShareDir.pm) >= 1.0
Requires:     perl(HTML/LinkExtor.pm)
Requires:       perl(HTTP/Tiny.pm) >= 0.044
Requires:       perl(List/Util.pm) >= 1.450
Requires:       perl(Module/Build.pm) >= 0.400.400
Requires:       perl(Path/Tiny.pm) >= 0.077
Requires:       perl(Text/ParseWords.pm) >= 3.260
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
Requires:       perl(IO/Socket/SSL.pm) >= 1.560
Requires:       perl(Net/SSLeay.pm) >= 1.490
%endif
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\((Alien.Base.PkgConfig|File.chdir|HTTP.Tiny|List.Util|Module.Build|Path.Tiny|Text.ParseWords).pm\\)/d

%description
This is a Perl base class and framework for creating Alien distributions. The
goal of the project is to make things as simple and easy as possible for both
developers and users of Alien modules.

Alien is a Perl name space for defining dependencies in CPAN for libraries and
tools which are not "native" to CPAN. Alien modules will typically use the
system libraries if they are available, or download the latest version from
the internet and build them from source code. These libraries can then be
used by other Perl modules, usually modules that are implemented with XS or FFI.

%prep
%setup -q -n Alien-Base-ModuleBuild-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2_1
- non-bootstrap build

* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_1
- to Sisyphus

