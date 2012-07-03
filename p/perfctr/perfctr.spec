Name: perfctr
Summary: Linux performance monitoring counters software
Version: 2.6.42
Release: alt1
License: LGPL
Group: Development/Tools
URL: http://user.it.uu.se/~mikpe/linux/perfctr/
Source: %name-%version.tar.gz
Source1: init.info
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Requires: lib%name = %version-%release

%description
This package adds support for using the Performance-Monitoring
Counters (PMCs) found in many modern processors.

PMCs are "event counters" capable of recording any of a large
number of performance-related events during execution.
These events typically include instructions executed, cache
misses, TLB misses, stalls, and other events specific to
the microarchitecture of the processor being used.

PMCs are primarily used to identify low-level performance problems,
and to validate code changes intended to improve performance.

%package -n lib%name
Summary: Shared libraries for perfctr
Group: Development/C

%description -n lib%name
Shared libraries for perfctr.

%package -n lib%name-devel
Summary: Development library for perfctr
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The perfctr-devel package contains object files
necessary for developing programs which use the perfctr C library.

%package -n lib%name-devel-static
Summary: Static library for perfctr
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static library for perfctr.

%prep
%setup
install %SOURCE1 .

%build
cp linux/include/linux/perfctr.h linux/include/
%make_build

%install
%makeinstall install2 \
	PREFIX=%buildroot%prefix \
	BINDIR=%buildroot%_bindir \
	LIBDIR=%buildroot%_libdir \
	INCLDIR=%buildroot%_includedir \
	ETCDIR=%buildroot%_sysconfdir

mv %buildroot%_includedir/linux/%name.h \
	%buildroot%_includedir/
mv %buildroot%_includedir/asm/%name.h \
	%buildroot%_includedir/asm_%name.h
sed -i 's|asm/%name.h|asm_%name.h|' \
	%buildroot%_includedir/%name.h

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/perfex
%config %_initdir/perfctr
%config %_sysconfdir/udev/rules.d/*perfctr.rules

%doc README CHANGES TODO OTHER

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*.h

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.42-alt1
- Version 2.6.42

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.41-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.41-alt2
- Rebuilt for soname set-versions

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.41-alt1
- Version 2.6.41

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.40-alt1
- Version 2.6.40

* Sun Sep 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.39-alt2
- Added necessary headers

* Wed Jun 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.39-alt1
- Version 2.6.39

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.38-alt3
- Rebuild with PIC

* Fri May 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.38-alt2
- Add 'modprobe %name' into start section of init script

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.38-alt1
- Version 2.6.38

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.35-alt2
- Remove asm&linux from %_includedir
- Remove mknod from %%post

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.35-alt1
- Initial build for Sisyphus

* Sun Oct 07 2007 Mikael Pettersson <mikpe@it.uu.se> -
- Corrected URL.

* Wed Jul 18 2007 Mikael Pettersson <mikpe@it.uu.se> -
- Correct udev rules path (/etc/udev.d/ -> /etc/udev/).

* Mon Apr 09 2007 Mikael Pettersson <mikpe@it.uu.se> -
- Install perfctr udev rules file and perfctr rc script
  so /dev/perfctr creation with correct permissions and
  perfctr module autoloading can work with udev.

* Tue Sep 16 2004 Mikael Pettersson <mikpe@csd.uu.se> -
- Dropped obsolete x86 qualification from Summary.

* Sun Dec 21 2003 Mikael Pettersson <mikpe@csd.uu.se> -
- Create /dev/perfctr in %post, not in %install and %files.
  This avoids incorrect deletion of the node on package uninstall.
- Don't add alias to /etc/modules.conf if it's already there.

* Sun Nov 23 2003 Mikael Pettersson <mikpe@csd.uu.se> -
- libperfctr.so install and uninstall fixes.

* Tue Sep 16 2003 Mikael Pettersson <mikpe@csd.uu.se> -
- No longer necessary to add module alias to /etc/modprobe.conf.

* Wed Jul 03 2003 Bryan O'Sullivan <bos@serpentine.com> -
- Fix module files for both 2.4 and 2.5 kernels.

* Wed Jul 02 2003 Mikael Pettersson <mikpe@csd.uu.se> -
- Corrected License and URL fields.

* Mon Jun 16 2003 Bryan O'Sullivan <bos@serpentine.com> -
- Add device file.
- Add module alias.

* Thu Jun 12 2003 Bryan O'Sullivan <bos@serpentine.com> - 
- Initial build.
