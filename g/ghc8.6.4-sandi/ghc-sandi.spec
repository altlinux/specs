%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name sandi
%define f_pkg_name sandi
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/sandi
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Data encoding library

BuildRequires: ghc8.6.4 ghc8.6.4-doc
BuildRequires: ghc8.6.4-conduit ghc8.6.4-exceptions


%description
Reasonably fast data encoding library.

%prep
%setup
%patch -p1
echo -e "import Distribution.Simple\nmain = defaultMain" > Setup.hs

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 0.5-alt1
- Build new version for ghc8.6.4.
