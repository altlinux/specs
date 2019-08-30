%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hslogger
%define f_pkg_name hslogger
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.12
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/hslogger
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Versatile logging framework

BuildRequires: ghc8.6.4 ghc8.6.4-doc ghc8.6.4-old-locale ghc8.6.4-network


%description
hslogger is a logging framework for Haskell, roughly similar to Python's
logging module.

hslogger lets each log message have a priority and source be associated
with it. The programmer can then define global handlers that route or
filter messages based on the priority and source. hslogger also has a
syslog handler built in.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Fri Aug 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.12-alt1
- Build new version for ghc8.6.4.
