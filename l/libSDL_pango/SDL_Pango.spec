%define shortname SDL_pango

Name: lib%shortname
Version: 0.1.2
Release: alt5

Summary: Rendering of internationalized text for SDL (Simple DirectMedia Layer)
License: LGPL
Group: System/Libraries
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Url: http://sdlpango.sourceforge.net/

Source0: http://dl.sf.net/sdlpango/%shortname-%version.tar.bz2
Source1: doxygen.png

Patch0: SDL_Pango-0.1.2-suppress-warning.patch
Patch1: SDL_Pango-0.1.2-API-adds.patch

BuildRequires: libpango-devel libSDL-devel dos2unix

%description
Pango is the text rendering engine of GNOME 2. SDL_Pango connects that engine
to SDL, the Simple DirectMedia Layer.

%package -n lib%shortname-devel
Summary: Development files for SDL_pango
Group: Development/C
Requires: lib%shortname = %version-%release
#, pango-devel, SDL-devel, pkgconfig

%description -n lib%shortname-devel
Development files for SDL_Pango.

%prep
%setup -q -n %shortname-%version
%patch0 -p1 -b .suppress-warning
%patch1 -p1 -b .API-adds

# Clean up, we include the entire "docs/html" content for the devel package
%__rm -rf docs/html/CVS/

# Replace the corrupt doxygen.png file with a proper one
%__install -m 0644 -p %SOURCE1 docs/html/doxygen.png

# Fix the (many) DOS encoded files, not *.png since they get corrupt
find . -not -name \*.png -type f -exec dos2unix {} \;

%build
%autoreconf
libtoolize --copy --force

%configure --disable-static
%make

%install
%make_install DESTDIR="%buildroot" install

%files -n lib%shortname
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files -n lib%shortname-devel
%doc docs/html/*
%_includedir/SDL_Pango.h
%_libdir/pkgconfig/SDL_Pango.pc
%_libdir/*.so

%changelog
* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt5
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt4
- Rebuilt with set-versioned SDL

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt3
- Rebuilt for soname set-versions

* Thu Aug 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Removed post[un]_ldconfig

* Mon Oct 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.2-alt1
- ALTLinuxized package.

* Fri Sep 29 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-4
- Add autoreconf and libtoolize calls since on FC5 x86_64 the shared library
  isn't build otherwise.
- Add API-adds patch (submitted upstream), required for the only project known
  to use SDL_Pango, so it does makes kind of sense...

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-3
- Use dos2unix to convert all DOS encoded files.
- Replace the corrupt doxygen.png file with a proper one.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-2
- Change %%makeinstall to using DESTDIR, according to the guidelines.
- Include patch from Mamoru Tasaka to remove all compilation warnings.

* Fri Sep 22 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.

