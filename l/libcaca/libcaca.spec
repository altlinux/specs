%def_disable   static
%def_disable   doc
%def_enable    ruby
%def_enable    python

Name: libcaca
Version: 0.99
Release: alt23
Summary: Text mode graphics library
Group: System/Libraries
License: WTFPL
Url: http://caca.zoy.org/wiki/libcaca
Vcs: https://github.com/cacalabs/libcaca.git
# git://git.altlinux.org/gears/l/libcaca.git
Source: %name-%version-%release.tar
Patch: ruby-paths.patch
# Automatically added by buildreq on Thu Apr 09 2020 (-bi)
BuildRequires: gcc-c++ imlib2-devel libncurses-devel libslang2-devel zlib-devel
%if_enabled doc
# buildreqs drowns in loops and misses all latex stuff
BuildRequires: doxygen
BuildRequires: texmf-latex-tabu
BuildRequires: tex-common texlive-base texlive-base-bin texlive-common
BuildRequires: texlive-fonts-recommended texlive-generic-recommended
BuildRequires: texlive-latex-base texlive-latex-recommended
BuildRequires: texlive-publishers texlive-xetex texmf-latex-xcolor
%endif

%description
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

%package devel
Summary: Development files for libcaca
Group: Development/C
Requires: %name = %version-%release

%description devel
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains the header files and static libraries needed to
compile applications or shared objects that use libcaca.

%package -n caca-utils
Summary: Text mode graphics utilities
Group: Graphics
Requires: %name = %version-%release

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca, the
Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image
formats such as JPEG, PNG, GIF etc. and renders them on the terminal using
ASCII art. The user can zoom and scroll the image, set the dithering method
or enable anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII metaballs on
the screen, cacafire is a port of AALib's aafire and displays burning ASCII
art flames, cacamoir animates colourful moire circles and cacaplas displays
an old school plasma effect.

cacademo is a simple application that shows the libcaca rendering features
such as line and ellipses drawing, triangle filling and sprite blitting.

%if_enabled ruby
%package -n ruby-caca
Summary: Ruby bindings for libcaca
Group: Graphics
Requires: %name = %version-%release
Provides: ruby-libcaca = %EVR, ruby-module-libcaca = %EVR
Obsoletes: ruby-module-libcaca < %EVR, ruby-libcaca < %EVR
BuildRequires: rpm-build-ruby

%description -n ruby-caca
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains Ruby bindings for libcaca.
%endif

%if_enabled python
%package -n python3-module-caca
Summary: Python3 module bindings for libcaca
Group: Other
BuildArch: noarch
Requires: %name = %version-%release
BuildRequires: python3-dev

%description -n python3-module-caca
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains python3 module bindings for libcaca.
%endif

%prep
%setup -n %name-%version-%release
%autopatch
# fix python shebangs
find . -type f -print0 |
	xargs -r0 grep -lZ '^#![[:space:]]*%_bindir/.*python\>' -- |
	xargs -r0 sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python\>@\1%__python3@' --

%build
# -ffat-lto-objects is needed even if static libraries are disabled
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
touch ChangeLog
%autoreconf
export PYTHON=%__python3
%configure \
	--enable-slang \
	--enable-ncurses \
	--enable-x11 \
	--enable-imlib2 \
	--x-libraries=%_x11libdir \
	--disable-debug \
	%{subst_enable python} \
	%{subst_enable ruby} \
	%{subst_enable doc} \
	%{subst_enable static}

%make_build V=1

%install
%makeinstall_std
rm %buildroot%_libdir/*.la
%if_enabled doc
rm -r %buildroot%_man3dir
rm -f %buildroot%_docdir/libcucul-dev
mv %buildroot%_datadir/doc/%name-dev %buildroot%_docdir/%name-%version
%endif

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_bindir/caca-config
%_man1dir/caca-config.1*
%_includedir/*
%_pkgconfigdir/*
%if_enabled doc
%_docdir/%name-%version
%endif

%files -n caca-utils
%_bindir/cacademo
%_bindir/cacafire
%_bindir/cacaclock
%_bindir/cacaplay
%_bindir/cacaserver
%_bindir/cacaview
%_bindir/img2txt
%_datadir/%name
%_man1dir/cacademo.1*
%_man1dir/cacafire.1*
%_man1dir/cacaplay.1*
%_man1dir/cacaserver.1*
%_man1dir/cacaview.1*
%_man1dir/img2txt.1*

%if_enabled ruby
%files -n ruby-caca
%ruby_vendorlibdir/caca.rb
%ruby_vendorarchdir/caca.*
%endif

%if_enabled python
%files -n python3-module-caca
%doc README
%python3_sitelibdir_noarch/*
%endif

%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.99-alt23
- ruby-caca: fixed install paths (closes #44113, #43828).

* Fri Aug 27 2021 Pavel Skrylev <majioa@altlinux.org> 0.99-alt22
- Reenabled packaging of ruby site module.
- Fixed ruby sitelibdir variable name.

* Thu Aug 26 2021 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt21
- NMU.
- v0.99.beta19-60-g813baea -> v0.99.beta19-62-ge4968ba (fixes: CVE-2021-3410).

* Thu Apr 09 2020 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt20
- NMU.
- Fixed and enabled python3 bindings.
- Disabled ruby bindings, ruby packaging in Sisyphus is broken beyond repair.

* Wed Mar 18 2020 Pavel Skrylev <majioa@altlinux.org> 0.99-alt19.git813baea7a
- ^ 0.99.beta19 -> 0.99.beta19.git813baea7a
- ! spec

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.99-alt18.beta19.5
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.99-alt18.beta19.4
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.99-alt18.beta19.3
- Rebuild with Ruby 2.4.2

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 0.99-alt18.beta19.2
- Rebuild with Ruby 2.4.1

* Fri Sep 08 2017 Michael Shigorin <mike@altlinux.org> 0.99-alt18.beta19.1
- Introduced doc knob (off by default: FTBFS).

* Fri Sep 08 2017 Michael Shigorin <mike@altlinux.org> 0.99-alt17.beta19.1
- Introduced ruby knob (on by default).

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.99-alt16.beta19.1
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.99-alt15.beta19.1
- Rebuilt with Ruby 2.3.1.

* Wed Jun 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.99-alt14.beta19.1
- Rebuilt with zlib support.

* Fri Jun 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.99-alt14.beta19
- Updated to v0.99.beta19.
- Dropped strange arch-dependent provides.

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.99-alt13.beta17.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.99-alt13.beta17.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Sep 25 2012 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt13.beta17
- Fixed interpackage dependencies.
- Built with libslang2-devel.

* Tue Oct 04 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.99-alt12.beta17.1
- remove obsolete macro

* Wed Apr 20 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.99-alt12.beta17
- New version

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99-alt11.beta16
- Rebuilt for soname set-versions

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt10.beta16
- 0.99.beta16 release.
- Disabled debug (closes #20568).
- Added fake provides for libcucul/libcucul++ for both arches.

* Fri Jul 03 2009 Alexey I. Froloff <raorn@altlinux.org> 0.99-alt10.beta14.1
- Rebuilt with Ruby 1.9
- ruby-module-libcaca renamed to ruby-libcaca

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt10.beta14
- 0.99.beta14 release.

* Wed Dec 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt10.beta13b
- Added debian's patch to prevent API breakage.

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt9.beta13b
- 0.99.beta13b release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt8.beta12
- 0.99.beta12 release.

* Tue Apr 24 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt7.beta11.debug
- Build with debug.

* Sat Mar 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt6.beta11
- Fix license, it's Do What The Fuck You Want To Public License, not LGPL.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt5.beta11
- Added post/postun ldconfig scripts.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt4.beta11
- Moved docs to %%_docdir/%%name-%%version.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt3.beta11
- Added Requires: to devel subpackage.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt2.beta11
- Pack pkg-config files.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99-alt1.beta11
- 0.99.beta11.
- Removed unneeded patch.
- Proper packaging/build fixes with new version.

* Mon Jun 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt2
- Build fixes
- Major spec cleanup
- Patch0: fix linker flags to withstand --as-needed

* Fri Jun 10 2005 Vitaly Smirnov <device@altlinux.org> 0.9-alt1
- Inital build
