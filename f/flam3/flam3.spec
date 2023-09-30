%define _stripped_files_terminate_build 1
%define _unpackaged_files_terminate_build 1

Name: flam3
Version: 3.1.1
Release: alt5

Summary: Programs to generate and render cosmic recursive fractal flames
License: GPL-3.0-or-later
Group: Graphics
Url: https://flam3.com
Vcs: https://github.com/scottdraves/flam3

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: flam3-3.1.1-alt-001-manpage_whatis_fix.patch
Patch2: flam3-3.1.1-alt-002-libxml.patch
Patch3: flam3-3.1.1-alt-003-ljpeg.patch
Patch4: flam3-3.1.1-alt-004-flam3.patch
Patch5: flam3-3.1.1-alt-005-readme.patch
Patch6: flam3-3.1.1-alt-006-icu67.patch
Patch7: flam3-3.1.1-alt-007-autoconf.patch
Patch8: flam3-3.1.1-alt-008-libm_linking.patch
Patch9: flam3-3.1.1-alt-009-optimisation_fix.patch

Requires: %name-palettes = %EVR

# Automatically added by buildreq on Mon Dec 07 2020 (-bi)
BuildRequires: libjpeg-devel libpng-devel libxml2-devel zlib-devel

%description
Flam3 renders fractal flames and manipulates their genomes.

%package devel
Summary: Development environment for building applications with %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the files needed to develop programs which use
the %name library.

%package palettes
Summary: The %name palettes xml file
Group: Graphics
BuildArch: noarch

%description palettes
The %name palettes xml file.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_libdir/lib%name.so.*
%_bindir/%name-*
%_man1dir/%{name}*.1*
%doc README.txt

%files -n %name-palettes
%_datadir/%name

%files -n %name-devel
%_includedir/*.*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Fri Sep 22 2023 Aleksei Kalinin <kaa@altlinux.org> 3.1.1-alt5
- Naming patches according to recommendations.
- Changed GIT package strategy and worktree location.
- Uses upstream Git repository to maintain history.
- Previous changelog display of macros corrected.

* Tue Sep 12 2023 Aleksei Kalinin <kaa@altlinux.org> 3.1.1-alt4
- Spec refactoring: %%define place changed. File COPYING excluded.
- Prapared patch: fix optimisations flags.
- Prapared patch: fix undefined libm references.

* Wed Apr 21 2021 Slava Aseev <ptrnine@altlinux.org> 3.1.1-alt3
- Rebuilt with glibc-2.32 (since 2.31 libm has no *_finite functions)

* Mon Dec 07 2020 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt2
- Imported patches from Debian.
- %%configure --enable-shared --disable-static.

* Mon Dec 07 2020 Motsyo Gennadi <drool@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sat Oct 18 2014 Motsyo Gennadi <drool@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.18-alt2.1
- Fixed built with libpng15

* Thu Jan 28 2010 Alexandra Panyukova <mex3@altlinux.org> 2.7.18-alt2
- palettes subpackage made noarch (repocop) (Closes: 20867)

* Wed Jul 22 2009 Alexandra Panyukova <mex3@altlinux.ru> 2.7.18-alt1
- new version

* Fri Apr 11 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.11-alt1
- new version

* Fri Jan 5 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.7-alt1
- 2.7.7
- added %name-devel package
- added %name-devel-static package
- added %name-palettes package

* Wed Apr 11 2007 Alexandra Panyukova <mex3@altlinux.ru> 2.7.2-alt1
- Initial build
