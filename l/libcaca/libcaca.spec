Name: libcaca
Version: 0.99
Release: alt12.beta17.1

Summary: Text mode graphics library
Group: System/Libraries
License: DWTFYWTPL
Url: http://sam.zoy.org/projects/libcaca/

Source: http://sam.zoy.org/projects/libcaca/%name-%version.tar.bz2
Patch0: libcaca-ruby1.9.patch

%ifarch x86_64
Provides: libcucul.so.0()(64bit)
Provides: libcucul++.so.0()(64bit)
%else
Provides: libcucul.so.0
Provides: libcucul++.so.0
%endif

BuildPreReq: rpm-build-ruby

# Automatically added by buildreq on Mon Apr 25 2011
# optimized out: imlib2 libX11-devel libstdc++-devel libtinfo-devel pkg-config ruby tex-common texlive-base texlive-base-bin texlive-common texlive-fonts-recommended texlive-latex-base texlive-latex-recommended texmf-latex-xcolor xorg-kbproto-devel xorg-xproto-devel
BuildRequires: doxygen gcc-c++ imake imlib2-devel libncurses-devel libruby-devel libslang-devel texlive-generic-recommended texlive-publishers texlive-xetex xorg-cf-files

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

%package -n ruby-libcaca
Summary: Ruby bindings for libcaca
Group: Graphics
Provides: ruby-module-libcaca = %version-%release
Obsoletes: ruby-module-libcaca


%description -n ruby-libcaca
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains Ruby bindings for libcaca.

%prep
%setup -q
%patch0 -p1

%build

%autoreconf

%configure \
	--enable-slang \
	--enable-ncurses \
	--enable-x11 \
	--enable-imlib2 \
	--enable-doc \
	--x-libraries=%_x11libdir \
	--disable-debug

%make_build

%install
cp -a doc/man/man3caca doc/man/man3
%make_install DESTDIR=%buildroot install
rm -f %buildroot/%_docdir/libcucul-dev
mv %buildroot/%_datadir/doc/%name-dev %buildroot/%_docdir/%name-%version

rm -f %buildroot%_man3dir/*

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_bindir/caca-config
%_includedir/*
%_docdir/%name-%version
%_man1dir/caca-config.1*
%_pkgconfigdir/*

%files -n caca-utils
%_bindir/cacademo
%_bindir/cacafire
%_bindir/cacaview
%_bindir/cacaplay
%_bindir/cacaserver
%_bindir/img2txt
%_datadir/%name
%_man1dir/cacademo.1*
%_man1dir/cacafire.1*
%_man1dir/cacaview.1*
%_man1dir/cacaplay.1*
%_man1dir/cacaserver.1*
%_man1dir/img2txt.1*

%files -n ruby-libcaca
%ruby_sitelibdir/caca.rb
%ruby_sitearchdir/caca.*

%changelog
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
