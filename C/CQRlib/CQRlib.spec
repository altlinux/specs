Name: CQRlib
Version: 1.1.2
Release: alt2

Summary: ANSI C API for quaternion arithmetic and rotation
License: LGPLv2+
Group: System/Libraries

Url: http://cqrlib.sourceforge.net/
Source: http://downloads.sourceforge.net/project/cqrlib/cqrlib/CQRlib-%version/CQRlib-%version.tar.gz
Patch: CQRlib-1.1.2-alt-debian-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Sep 23 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

%description
CQRlib is an ANSI C implementation of a utility library for quaternion
arithmetic and quaternion rotation math.

%package -n lib%name
Summary: Shared library for CQRlib
Group: System/Libraries

%description -n lib%name
This package includes the shared library files
for running applications that use CQRlib.

%package -n lib%name-devel
Summary: Development tools for compiling programs using CQRlib
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package includes the header and library files
for developing applications that use CQRlib.

%prep
%setup
%patch -p1

%build
%make_build all CFLAGS="%optflags"

%install
%make_install install INSTALLDIR="%buildroot%prefix"
%if %_lib != lib
mv %buildroot%_usr/{lib,%_lib}
%endif
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name '*.a' -exec rm -f {} ';'

%check
make tests

%files -n lib%name
%doc README_CQRlib.html README_CQRlib.txt lgpl.txt
%_libdir/libCQRlib.so.*

%files -n lib%name-devel
%_includedir/cqrlib.h
%_libdir/libCQRlib.so

%changelog
* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.1.2-alt2
- drop empty package

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- initial build for ALT Linux Sisyphus (based on F15 spec)
  + dropped fedora patches (were insufficient and overlapping
    with the libtool fix needed)
  + fixed libtool issue
  + merged in debian patch
  + skimmed gentoo patch as well

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.2-1
- update to 1.1.2

* Mon Oct 18 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-2
- use "make all" instead of "make"
- add %%check

* Thu Oct 14  2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-1
- initial import (#545045).

* Tue Oct 12 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-0.1
- use %%{_lib} detection to fix W: %%ifarch-applied-patch

* Thu Sep 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1.1-0
- update to 1.1.1

* Fri Sep 10 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.1-0
- update to 1.1

* Mon Aug 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.6-1
- update to 1.0.6
- provide 64 bit libdir fix as a patch
- provide s/dynamic/rsynamic/g as a patch

* Thu May  6 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.5-1
- update to 1.0.5

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-3.20090805
- remove static library

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-2.20090805
- fit to Fedora Packaging Guidelines
- apply changes pointed at rhbz #545045 comment #1

* Tue Aug 25 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.20090805
- update to 1.0.3-5Aug09

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1
- initial build
