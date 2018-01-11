Summary: Free firewire audio driver library
Name: libffado
Version: 2.4.0
Release: alt1
License: GPLv2+
Group: Sound
Url: http://www.ffado.org/
Source: %name-%version.tgz
Patch0: libffado-2.0.0-rc1-dbus-mainloop-qt-detect.patch
Patch1: libffado-2.0.0-ffado-diag-path.patch
Patch2: libffado-2.0-rc1-includes.patch
Patch3: libffado-2.0-alt.patch
Patch4: libffado-2.0.1-alt.DSO.patch
Patch5: libffado-2.0-alt-2.patch
%setup_python_module ffado

# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: gcc-c++ libdbus-devel libexpat-devel libiec61883-devel libxml++2-devel python-module-PyQt4 python-module-dbus python-modules-encodings scons subversion xdg-utils libconfig-c++-devel          

%description
The FFADO project aims to provide a generic, open-source solution for the
support of FireWire based audio devices for the Linux platform. It is the
successor of the FreeBoB project.

%package devel
Summary: Free firewire audio driver library development headers
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files needed to build applications against libffado.

%package -n ffado
Summary: Free firewire audio driver library applications and utilities
Group: Sound
Requires: %name = %version-%release

%description -n ffado
Applications and utilities for use with libffado.

%package -n %packagename
Summary: Python bindings for %name, %summary
Group: Development/Python
Buildarch: noarch
%description -n  %packagename
Python bindings for %name, %summary

%prep
%setup -n %name-%version
# XXX this uses non-existed module and is not used itself!
rm support/mixer-qt4/ffado/mixer/nodevice.py
#patch0 -p1
# This patch may be useful
%patch1
#patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2

%build
[ -n "$NPROCS" ] || NPROCS=%__nprocs; scons -j$NPROCS PREFIX=%prefix LIBDIR=%_libdir WILL_DEAL_WITH_XDG_MYSELF=YES COMPILE_FLAGS='%optflags' MANDIR=%_mandir

%install
rm -rf %buildroot
scons PREFIX=%prefix LIBDIR=%_libdir \
      WILL_DEAL_WITH_XDG_MYSELF=YES \
      MANDIR=%_mandir \
      DESTDIR=%buildroot install
# install missing python modules
install -m 0644 support/tools/listirqinfo.py %buildroot%_datadir/libffado/python
install -m 0644 support/tools/helpstrings.py %buildroot%_datadir/libffado/python

%clean
rm -rf %buildroot

%files
%doc AUTHORS ChangeLog LICENSE.* README
%_libdir/libffado.so.*

%files devel
%dir %_includedir/libffado
%_includedir/libffado/*.h
%_libdir/pkgconfig/libffado.pc
%_libdir/libffado.so

%files -n ffado
%_bindir/*
%_man1dir/*
%dir %_datadir/libffado
%_datadir/libffado/*
/lib/udev/rules.d/*ffado*.rules

%files -n %packagename
%python_sitelibdir_noarch/%modulename

%changelog
* Thu Jan 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.0-alt1
- Updated to upstream version 2.4.0

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Oct 30 2012 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0
- Separate python module
- Remove unused python file with non-existent requirement

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.0.1-alt2
- DSO list completion

* Mon Mar 12 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1.2
- use default optflags

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Tue Sep 14 2010 Fr. Br. George <george@altlinux.ru> 2.0.1-alt1
- Version up (utilize firewire stack used)

* Fri Sep 10 2010 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Version up to release

* Fri Sep 10 2010 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Initial build from FC

* Tue Jun  9 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2.0.0-0.6.rc1
- add patch2 for building on fc11

* Fri Dec 12 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2.0.0-0.6.rc1
- added explicit PyQt4 dependency
- install listirqinfo, otherwise ffado-diag does not run
  (and the helpstrings module as well)
- ffado-diag needs to use the libffado python path (patch1)

* Tue Dec  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2.0.0-0.4.rc1
- update to rc1
- redo install section, change to qt4 build dependency, add patch
  because the python module dbus.mainloop.qt is not autodetected
  (but it is there and the build goes ahead just fine)
- do not install in libexec (tried, not really working fine)

* Thu Nov 06 2008 Jarod Wilson <jarod@redhat.com> - 2.0.0-0.3.beta7
- Update to beta7
- Put arch-dependent helper/test binaries in libexecdir instead of datadir

* Sun Aug 10 2008 Jarod Wilson <jwilson@redhat.com> - 2.0.0-0.2.beta6
- Review clean-ups (#456353)

* Tue Jul 22 2008 Jarod Wilson <jwilson@redhat.com> - 2.0.0-0.1.beta6
- Initial Fedora build of libffado
