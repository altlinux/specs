%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name haskeline
%define f_pkg_name haskeline
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.3.2
Release: alt1.1
License: BSD
Group: Development/Haskell
URL: http://trac.haskell.org/haskeline
Packager: Alexey Voinov <voins@altlinux.ru>
Source: %f_pkg_name-%version.tar
Summary: A command-line interface for user input, written in Haskell

BuildRequires: ghc
BuildRequires: %hs_package_dependencies mtl utf8-string extensible-exceptions
BuildRequires(pre): rpm-build-haskell


%description
Haskeline provides a user interface for line input in command-line
programs.  This library is similar in purpose to readline, but since
it is written in Haskell it is (hopefully) more easily used in other
Haskell programs.

%prep
%setup -n %h_pkg_name-%version


%build


%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot/%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE README


%files  -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
%doc LICENSE CHANGES


%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.6.3.2-alt1.1
- rebuild with shared objects support

* Sat Dec 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.3.2-alt1
- 0.6.3.2

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.2.1-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.2.1-alt5
- auto rebuild

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.2.1-alt2
- ghc 6.12.3

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.2.1-alt1.1.1
- rebuild with new haskell

* Wed Mar 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6.2.1-alt1.1
- rebuild with new haskell

* Mon Oct 05 2009 Alexey Voinov <voins@altlinux.ru> 0.6.2.1-alt1
- Initial build for Sisyphus.
