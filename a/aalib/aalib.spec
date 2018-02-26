%def_disable static
%define prerel rc5

Name: aalib
Version: 1.4
Release: alt7%prerel

Summary: AA (Ascii Art) library
License: LGPLv2+
Group: System/Libraries
Url: http://aa-project.sourceforge.net/%name/

# http://prdownloads.sourceforge.net/aa-project/%name-%version%prerel.tar.gz
Source: %name-%version%prerel.tar
Source1: %name-config.1
Patch0: %name-info.patch
Patch1: %name-debian_man.patch
Patch2: %name-1.4-suse-m4.patch
Patch3: %name-1.4-fc-aalinuxkbd.patch
Patch4: %name-1.4-alt-rpath.patch

%ifdef prerel
Provides: %name = %version%prerel
%endif

# Automatically added by buildreq on Mon Apr 25 2011
# optimized out: xorg-xproto-devel
BuildRequires: libX11-devel libgpm-devel libslang2-devel

%package devel
Summary: Header files for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release

%ifdef prerel
Provides: %name-devel = %version%prerel
%endif

%package devel-static
Summary: Static library for developing apps which will use %name
Group: Development/C
Requires: %name-devel = %version-%release

%package utils
Summary: AA-lib tools
Group: Graphics
Requires: %name = %version-%release

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP.

%description devel
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

Install the %name-devel package if you want to develop applications that
will use the %name library.

%description devel-static
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP.

Install the %name-devel-static package if you want to develop
statically linked applications that will use the %name library.

%description utils
These programs demonstrate the capabilities of the aalib
library, an ASCII art library.

%prep
%setup -n %name-%version.0
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

install -pD -m644 %SOURCE1 %buildroot%_man1dir/aalib-config.1

for p in `ls -1 %buildroot%_bindir | grep -Ev '\-|fire'`; do
    echo .so aafire.1 >%buildroot%_man1dir/"$p".1
done

# remove none-packaged files
rm -f %buildroot%_infodir/dir

%files
%doc ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_datadir/aclocal/*
%_infodir/*.info*
%_man1dir/*-config.*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/*
%exclude %_bindir/*-config
%_man1dir/*
%exclude %_man1dir/*-config.*

%changelog
* Sun Dec 18 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 1.4-alt7rc5
- Fixed "aalib-config --libs" output (closes: #26727).

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt6rc5
- Build with libslang2.
- Rebuilt for debuginfo.

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt5rc5.1
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Zubkov <icesik@altlinux.org> 1.4-alt5rc5
- fix buildreqs

* Mon Nov 02 2009 Igor Zubkov <icesik@altlinux.org> 1.4-alt4rc5
- fix repocop warning

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.4-alt3rc5
- Get rid of post/postun ldconfig.

* Tue May 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4-alt2rc5
- Added patch from FC (fixes their #149361).

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4-alt1rc5
- Spec cleanup.
- Added packager field.
- Fixed buildrequires for Xorg.

* Sun Nov 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt0.8rc5
- Fix quoting in autoconf macros (tanks Suse).
- do not build devel-staic subpackage by default.

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt0.7rc5
- use libtool-1.4
- do not package .la files.
- devel-staic subpackage now is optional.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt0.6rc5
- Rebuild with gcc-3.2.

* Fri May 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt0.5rc5
- 1.4rc5.
- Applied PLD patches.
- utils package.

* Tue Feb 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.2-ipl14mdk
- Fixed URL.
- Fixed build via libtoolize & co. in %%prep section.

* Fri Jun 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2-ipl13mdk
- Moved static library to devel-static subpackage.

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.2-ipl2mdk
- Specfile cleanup.

* Sun Nov 27 2000 AEN <aen@logic.ru>
- rebuild for RE

* Mon Oct  2 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2-10mdk
- Correct info installation
- Remove french description

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2-9mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2-8mdk
- BM
- make rpmlint happier

* Fri Mar 10 2000 Jerome Dumonteil <jd@mandrakesoft.com>
- rebuilt for 7.1

* Wed Dec  1 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- use _tmppath in Buildroot

* Thu Oct  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Install info files
- Don't include the dir file
- Split the packages into two packages

* Mon Aug 09 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- fixed the Summary to be more meaningfull

* Tue Jul 9 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a bug in the spec that garbage the french description

* Tue Jul 06 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- new library needed for GIMP
