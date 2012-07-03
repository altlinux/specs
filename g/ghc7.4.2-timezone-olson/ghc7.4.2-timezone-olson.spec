%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name timezone-olson
%define f_pkg_name timezone-olson
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.2
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://projects.haskell.org/time-ng/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A pure Haskell parser and renderer for binary Olson timezone files



# Automatically added by buildreq on Sat Jun 30 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-doc ghc7.4.2-timezone-series

%description
A parser and renderer for binary Olson timezone files whose format is
specified by the tzfile(5) man page on Unix-like systems. For more
information about this format, see <http://www.twinsun.com/tz/tz-link.htm>.
Functions are provided for converting the parsed data into 'TimeZoneSeries'
objects from the timezone-series package. On many platforms, binary Olson
timezone files suitable for use with this package are available in the
directory /usr/share/zoneinfo and its subdirectories on your computer.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- Spec created by cabal2rpm 0.20_08
