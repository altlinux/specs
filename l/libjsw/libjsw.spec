Name: libjsw
Version: 1.5.6
Release: alt1.qa1

Summary: UNIX joystick driver wrapper library

License: GPL
Group: System/Libraries
#Url: http://wolfpack.twu.net/libjsw/index.html
Url: http://freshmeat.net/projects/libjsw/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://wolfpack.twu.net/users/wolfpack/%name-%version.tar.bz2
Patch: %name-gcc4.patch

# Automatically added by buildreq on Mon Dec 25 2006
BuildRequires: gcc-c++

BuildConflicts: %name-devel

Provides: %name.so

%description
The UNIX Joystick Driver Wrapper Library and Calibrator (aka libjsw) provides
the programmer with the assistance to easily code applications that need to
use the joystick driver and a convience to users by storing the calibration
information in a .joystick calibration file


%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package calibrator
Summary: Joystick calibrator
Group: Development/C
Requires: %name = %version

%description calibrator
Joystick calibrator itself

%prep
%setup
%patch

DIRS="jscalibrator libjsw"
for DIR in $DIRS; do
	subst 's|^PREFIX = /usr|PREFIX = \$(RPM_BUILD_ROOT)%prefix|g' $DIR/Makefile
	subst 's|^CFLAGS = [^\\]*|CFLAGS = \$(RPM_OPT_FLAGS) -fPIC|g' $DIR/Makefile.Linux
done
subst 's|^LIB_DIRS =|LIB_DIRS = -L../libjsw|g' jscalibrator/Makefile
subst 's|<jsw.h>|"../include/jsw.h"|' jscalibrator/jc*.*

%build
cd libjsw
make -f Makefile.Linux
cd -

%install
cd libjsw
%makeinstall JSW_MAN_DIR=%buildroot%_man3dir JSW_LIB_DIR=%buildroot%_libdir
cd -
rm -f %buildroot%_man1dir/

%files
%doc AUTHORS LICENSE README jswdemos
%_libdir/lib*.so.*
# Strange so loading?
%_libdir/*.so

%files devel
%_includedir/*
%_man3dir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- cleanup spec

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt0.4
- fix build on x86_64

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt0.2
- disable jscalibrator (gtk1 app) build

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt0.1
- new version 1.5.6 (with rpmrb script)
- fix build with GCC4

* Fri Feb 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version
- enable calibrator packing
- hack fix bug #6134

* Sat Sep 11 2004 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- first build for Sisyphus
- calibrator disabled

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5.4-2mdk
- don't do stuff within parantheses
- do install in %%install
- fix shlib-with-non-pic-code
- cosmetics

* Sun Apr 18 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.4-1mdk
- new version
- no explicit gtk dependency

* Mon Jan 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.2-5mdk
- fix build (slbd)

* Tue Jul 08 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.5.2-4mdk
- rebuild for new rpm devel computation

* Fri May 23 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.5.2-3mdk
- fixed dir ownership (Olivier Thauvin <thauvin@aerov.jussieu.fr>)

* Fri May 02 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.5.2-2mdk
- 1.5.2.

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-4mdk
- rebuild

* Mon Jun 03 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-3mdk
- rebuild against new libstdc++

* Sun Jan 06 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.5.0-2mdk
- added help files for calibrator  (Andre Duclos <shirka@wanadoo.fr>)

* Fri Jan 04 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.5.0-1mdk
- 1.5.0
- lib man page in devel package
- app man page in calibrator package
- spec cleanup
- mandrake optimisations

* Thu Sep 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Mon Aug 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0d-2mdk
- rebuild

* Wed Apr 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0d-1mdk
- updated by Guillaume Rousse <g.rousse@linux-mandrake.com> :
	- 1.4.0d
	- add gtk to requires and buildrequires or libjsw1-calibrator
	- synced with Lenny's spec

* Mon Mar 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0c-3mdk
- update requires for libjsw1-calibrator

* Mon Mar 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0c-2mdk
- split package

* Tue Feb 13 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0c-1mdk
- used srpm from Guillaume Rousse <g.rousse@mandrake-linux.com> :
	- first Mandrake release
