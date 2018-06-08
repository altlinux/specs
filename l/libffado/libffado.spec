%define _unpackaged_files_terminate_build 1

Summary: Free firewire audio driver library
Name: libffado
Version: 2.4.1
Release: alt1
License: GPLv2+
Group: Sound
Url: http://www.ffado.org/

Source: %name-%version.tar

Patch1: libffado-2.0-alt.patch

%setup_python_module ffado

BuildRequires: gcc-c++
BuildRequires: libdbus-devel libexpat-devel libiec61883-devel libxml++2-devel
BuildRequires: python-module-PyQt4 python-module-dbus python-modules-encodings
BuildRequires: scons xdg-utils libconfig-c++-devel

%description
The FFADO project aims to provide a generic, open-source solution for the
support of FireWire based audio devices for the Linux platform. It is the
successor of the FreeBoB project.

%package devel
Summary: Free firewire audio driver library development headers
Group: Development/C
Requires: %name = %EVR

%description devel
Development files needed to build applications against libffado.

%package -n ffado
Summary: Free firewire audio driver library applications and utilities
Group: Sound
Requires: %name = %EVR

%description -n ffado
Applications and utilities for use with libffado.

%package -n %packagename
Summary: Python bindings for %name, %summary
Group: Development/Python
Buildarch: noarch

%description -n  %packagename
Python bindings for %name, %summary

%prep
%setup
%patch1 -p2

# XXX this uses non-existed module and is not used itself!
rm support/mixer-qt4/ffado/mixer/nodevice.py

# We don't want to install all tests
sed -i '/Install/d' tests/{,*/}SConscript

%build
[ -n "$NPROCS" ] || NPROCS=%__nprocs;
scons -j$NPROCS \
	PREFIX=%prefix \
	LIBDIR=%_libdir \
	WILL_DEAL_WITH_XDG_MYSELF=YES \
	CFLAGS='%optflags' \
	CXXFLAGS='%optflags' \
	CUSTOM_ENV=True \
	MANDIR=%_mandir \

%install
scons \
	PREFIX=%prefix \
	LIBDIR=%_libdir \
	WILL_DEAL_WITH_XDG_MYSELF=YES \
	CFLAGS='%optflags' \
	CXXFLAGS='%optflags' \
	CUSTOM_ENV=True \
	MANDIR=%_mandir \
	DESTDIR=%buildroot install

# remove unpackaged files
rm -f %buildroot%_libdir/libffado/static_info.txt
rm -f %buildroot%_datadir/metainfo/ffado-mixer.appdata.xml

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
* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt1
- Updated to upstream version 2.4.1.

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
