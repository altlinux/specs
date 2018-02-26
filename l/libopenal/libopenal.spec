%define lib_major 0
%def_disable static

Name: libopenal
Version: 0.0.9
Release: alt2

Summary: Main library for OpenAL, a free 3D sound library
Group: Sound
URL: http://www.openal.org
License: LGPL

#Source: openal-%version.tar.gz
Source0: openal-cvs-20060204.tar.bz2
Source1: openalrc

#Patch: openal-%version-pkgconfig.patch
Patch0: openal-arch.patch
Patch1: openal-no-undefined.patch
Patch2: openal-pkgconfig.patch
Patch3: openal-pause.patch
Patch4: openal-x86_64-mmx.patch
Patch5: openal-gcc43.patch

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ libSDL-devel libalsa-devel libsmpeg-devel libvorbis-devel

%description
OpenAL is a free 3D-audio library, with a programming interface similar
to that of OpenGL.

%prep
%setup -q -n portable
%ifarch i586
# Fix CFLAGS
%define _optlevel 6
%add_optflags %optflags_kernel %optflags_fastmath
%endif

%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch0 -p1
%patch5 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-optimization \
	--enable-sdl \
	--enable-vorbis \
	--enable-smpeg \
	--enable-alsa \
	--libdir=%_libdir
%make_build

%install
DESTDIR=%buildroot %__make install

mkdir %buildroot%_sysconfdir
install -m644 %SOURCE1 %buildroot%_sysconfdir/openalrc

mkdir -p %buildroot%_infodir
cd %buildroot%_libdir

ln -sf %name.so.%version %name.so.%lib_major

%files
%config(noreplace) %_sysconfdir/openalrc
%_libdir/*.so.*

%changelog
* Tue Mar 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.0.9-alt2
- removed devel subpackage

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.0.9-alt1
- sync with Fedora openal-0.0.9-0.15.20060204cvs.fc9

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.0.8-alt5
- apply patch from repocop

* Fri Oct 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.0.8-alt4
- fix #12667 (openal.pc contains unexpanded macro)

* Tue Apr 24 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.0.8-alt3
- alsa-devel require added

* Fri Mar 02 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.0.8-alt2
- 0.0.8 (2006-02-11) update
- spec clean up
- compile with alsa support
- #10966 (/etc/openalrc added)

* Thu Dec 15 2005 LAKostis <lakostis at altlinux.ru> 0.0.8-alt1.1
- NMU.
- fix CFLAGS for x86_64.
- disable -static by default.

* Sat Aug 20 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.0.8-alt1
- update to 2005 Jul snapshot
- libopenal soname changed (0.0.7->0.0.8)

* Tue Dec 28 2004 Kachalov Anton <mouse@altlinux.ru> 0.0.7-alt2
- update to 2004 Sep snapshot

* Fri Apr 30 2004 Kachalov Anton <mouse@altlinux.ru> 0.0.7-alt1
- remove compilation with Arts, Esd
- update from CVS

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 0.0.6-alt5
- update from CVS

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 0.0.6-alt4
- build requires fix

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.6-alt3
- Rebuilt in new environment

* Wed Jul 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.6-alt2
- Rebuilt with new OGG
- Last version from CVS

* Mon Mar 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.6-alt1
- First build for Sisyphus

* Tue Sep 11 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-2mdk
- added by Maksim Orlovich <mo002j@mail.rochester.edu> :
	- Fix the .so in the devel package.

* Sun Aug 05 2001 Maksim Orlovich <mo002j@mail.rochester.edu> 0.0.6-1mdk
-Initial Mandrake Package.
