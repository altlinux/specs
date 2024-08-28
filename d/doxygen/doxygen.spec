Name: doxygen
Version: 1.12.0
Release: alt1
Epoch: 1

Summary: Doxygen is a documentation system for C, C++ and IDL
License: GPLv2+
Group: Development/Other
Url: http://www.doxygen.org/

# ftp://ftp.stack.nl/pub/users/dimitri/doxygen-%version.src.tar.gz
Source: %name-%version.src.tar.gz
Source500: %name.unused

## Ubuntu patches
Patch101: Ubuntu-manpages.patch
Patch102: Ubuntu-dot-config.patch
Patch104: Ubuntu-avoid-compass.patch
Patch107: Ubuntu-libatomic.patch
Patch108: Ubuntu-reproducible_manpages.patch
Patch109: Ubuntu-sass_fix.patch

## ALT patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex bison
BuildRequires: /usr/bin/epstopdf
BuildRequires: git-core
BuildRequires: graphviz
BuildRequires: perl
BuildRequires: texlive-collection-basic texlive-dist
BuildRequires: qt5-base-devel
BuildRequires: sassc node-uglify-js

# graphviz uses pango as the default backend. pango needs some font and
# a properly configured fontconfig to produce something sane.
BuildRequires: fontconfig fonts-ttf-dejavu
Requires: fontconfig fonts-ttf-dejavu

%description
Doxygen is a documentation system for C, C++ and IDL.  It can generate
an on-line class browser (in HTML) and/or an off-line reference manual
(in LaTeX) from a set of documented source files.  There is also support
for generating man pages and for converting the generated output into
Postscript, hyperlinked PDF or compressed HTML.  The documentation is
extracted directly from the sources.

Doxygen can also be configured to extract the code-structure from
undocumented source files.  This can be very useful to quickly find
your way in large source distributions.

%package wizard
Summary: GUI frontend for doxygen
Group: Development/Other
Requires: %name = %epoch:%version-%release

%description wizard
Doxywizard is a GUI front-end for creating and editing
configuration files that are used by doxygen.

%package doc
Summary: Documentation and examples for doxygen
Group: Development/Other
BuildArch: noarch
Requires: %name = %epoch:%version-%release

%description doc
This package contains doxygen examples and documentation in html and
pdf formats.

%prep
%setup

## Remove junk
find * -name "*._*" -delete

## Ubuntu apply patches
%patch101 -p1
%patch102 -p1
%patch104 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1

## ALT apply patches

%build
%make_build -C deps/jquery \
	UGLIFYJS=uglifyjs \
	install

%define _cmake__builddir BUILD
%cmake -G "Unix Makefiles" \
	-Dbuild_doc=ON -Dbuild_wizard=ON -Dbuild_xmlparser=ON \
	-Dbuild_search=OFF \
	-DMAN_INSTALL_DIR=%_mandir/man1 \
	-DDOC_INSTALL_DIR=share/doc/%name-%version \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix
%cmake_build

export NPROCS=1
%cmake_build -t docs

%install
%cmakeinstall_std

%check
cd BUILD && make tests

%files
%doc README.md
%_bindir/doxygen
%_man1dir/doxygen.*

%files wizard
%_bindir/doxywizard
%_man1dir/doxywizard.*

%files doc
%_defaultdocdir/%name-%version
%exclude %_defaultdocdir/%name-%version/README.md

%changelog
* Wed Aug 28 2024 Ivan A. Melnikov <iv@altlinux.org> 1:1.12.0-alt1
- 1.12.0
- BuildRequires and patches cleanup

* Wed May 22 2024 Ivan A. Melnikov <iv@altlinux.org> 1:1.11.0-alt1
- 1.11.0.

* Tue Dec 26 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.10.0-alt1
- 1.10.0;
- require fonts-ttf-dejavu (fixes broken graphviz diagrams).

* Fri Sep 01 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.9.8-alt1
- 1.9.8

* Fri Aug 25 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.9.7-alt1
- 1.9.7

* Mon Aug 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.9.6-alt1.1
- NMU: fixed FTBFS

* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 1:1.9.6-alt1
- Autobuild version bump to 1.9.6

* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 1:1.9.1-alt1
- Autobuild version bump to 1.9.1
- Introducing Qt5 wizard

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1:1.8.17-alt2.1
- NMU: spec: adapted to new cmake macros.

* Mon May 18 2020 Nikita Ermakov <arei@altlinux.org> 1:1.8.17-alt2
- Use Qt5 instead of Qt4 for doxygen-wizard

* Tue May 12 2020 Fr. Br. George <george@altlinux.ru> 1:1.8.17-alt1
- Autobuild version bump to 1.8.17

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 1:1.8.15-alt1
- Autobuild version bump to 1.8.15

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.13-alt2.1
- NMU: fixed build with texlive 2017

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.8.13-alt2
- Applied upstream patch to fix some crash cases

* Mon Apr 17 2017 Fr. Br. George <george@altlinux.ru> 1:1.8.13-alt1
- Autobuild version bump to 1.8.13

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.6.1-alt1
- Updated to 1.7.6.1.

* Thu Sep 29 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.5.1-alt1
- Updated to 1.7.5.1.

* Sun Apr 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.4-alt1
- Updated to 1.7.4 (closes: #25270).

* Sun Aug 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.9-alt2
- Updated build dependencies.

* Thu Jun 25 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.9-alt1
- Updated to 1.5.9.
- Built wizard with qt4.
- Packaged -doc subpackage as noarch.

* Thu Apr 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.5-alt1
- Updated to 1.5.5.
- Updated build dependencies.
- Packaged manpages.
- Moved documentation and examples to -doc subpackage (#9742).

* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.1-alt1
- Updated to 1.5.1.

* Tue Jun 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.7-alt1
- Updated to 1.4.7.

* Fri Feb 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.6-alt1
- Updated to 1.4.6.

* Mon Oct 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.5-alt1
- Updated to 1.4.5.
- Fixed build with new flex.

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.3-alt1
- Updated to 1.4.3.
- Added multilib support (mouse, closes #6732).

* Mon Jan 24 2005 Stanislav Ievlev <inger@altlinux.org> 1:1.4.1-alt1.1
- 1.4.1

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.3.9.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Oct 19 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.9.1-alt1
- 1.3.9.1

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.6-alt1
- 1.3.6

* Tue Jan 27 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.5-alt1
- 1.3.5

* Thu Sep 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.3.3-alt1
- 1.3.3

* Thu Sep 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.18-alt1
- 1.2.18
- The image map generation patch merged upstream.
- Added changelog.html to docs.

* Fri Aug 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.17-alt2
- Fixed image map generation (#0001188).

* Wed Jul 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.17-alt1
- 1.2.17

* Thu May 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.16-alt1
- 1.2.16

* Fri Apr 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.15-alt1
- 1.2.15.

* Thu Mar 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.14-alt2
- Fixed %%clean.

* Tue Feb 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.14-alt1
- 1.2.14.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.13.1-alt1
- 1.2.13.1

* Mon Nov 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.12-alt1
- 1.2.12

* Wed Oct 10 2001 Rider <rider@altlinux.ru> 1.2.11.1-alt1
- 1.2.11.1

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.8.1-alt1
- 1.2.8.1

* Thu Jun  7 2001 Sergey Vlasov <vsu@altlinux.ru> 1.2.8-alt2
- Fixed compilation options in qtools
- Compile with --no-exceptions --no-rtti
- Fixed QTDIR setting; removed broken conf patch from Mandrake
- Build doxywizard (separate package doxygen-wizard)

* Tue Jun 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Wed Jan 03 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.4-ipl1mdk
- 1.2.4

* Sat Nov 11 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.3-ipl1mdk
- 1.2.3

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.2-ipl1mdk
- 1.2.2
- Automatically added BuildRequires.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.1-ipl1mdk
- RE adaptions.

* Sun Aug 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.0-2mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- BM
- macros

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.0-3mdk
- ExcludeArch: alpha (yep lazzyness).

* Sat Apr  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-1mdk
- first Mandrake release
- patch to fix wrong lookup of Qt include/lib
