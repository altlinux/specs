%define oname gnet
%define ver_major 2.0
%def_disable static

Name: lib%oname
Version: %ver_major.8
Release: alt4

Summary: GNet is a simple network library
License: LGPL
Group: System/Libraries
URL: http://www.gnetlibrary.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Source: %gnome_ftp/%oname/%ver_major/%oname-%version.tar.bz2
Source1: %name-%ver_major.map
Patch1: %name-%version-alt-versioning.patch
Patch2: libgnet-fix-move_define.patch

BuildRequires: rpm-build-gnome
BuildRequires: gtk-doc libcheck-devel
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: gcc-c++ 


%description
GNet is a simple network library.  It is written in C,
object-oriented, and built upon GLib.  It is intended to be easy to
use and port.  GNet comes with documentation and examples.  It is
licensed under the GNU Library General Public Licence.

Features:
  * TCP "client" and "server" sockets
  * UDP and IP Multicast sockets
  * High-level TCP connection and server objects
  * Asynchronous socket IO
  * Internet address abstraction
  * Asynchronous DNS lookup
  * IPv4 and IPv6 support
  * Byte packing and unpacking
  * URI parsing
  * SHA and MD5 hashes
  * Base64 encoding and decoding
  * SOCKS support
  * High-level HTTP connection object

%package devel
Summary: Header files for the Gnet library
Group: Development/C
Requires: %name = %version-%release

%description devel
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon glib.
This package allows you to develop applications that use the Gnet library.


%if_enabled static
%package devel-static
Summary: Static Gnet library
Group: Development/C
Requires: %name-devel = %version-%release glib2-devel-static

%description devel-static
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon glib.
This package allows you to develop statically linked applications that
use the Gnet library.

%endif


%prep
%setup -q -n %oname-%version
%patch1 -p1
%patch2 -p1
install -p -m644 %SOURCE1 src/libgnet-2.0.map

%build
%autoreconf
%configure   \
	     %{subst_enable static} \
	      --with-html-dir=%_docdir
%make_build

%install
%make_install DESTDIR=%buildroot install

%make -C examples clean
rm -f examples/Makefile*
rm -Rf examples/.deps/
rm -Rf %buildroot%_docdir

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/gnet-2.0
%_pkgconfigdir/*
%_includedir/*
%_datadir/aclocal/*
%doc AUTHORS ChangeLog HACKING NEWS README TODO doc/html examples

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Nov 29 2010 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt4
- fix build by moving a #define before it's used (tnx debian)

* Fri Feb 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt3
- rm glib-devel from Requires in devel package (ALT #22900)

* Fri Feb 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt2
- fix build: update buildreq

* Tue Sep 22 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt1
- 2.0.8
- add Packager
- change description
- add versioning
- drop obsoleted post scripts

* Mon Nov 20 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.7-alt1
- 2.0.7
- disable default build static libs 

* Thu Mar 18 2004 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Wed Oct 23 2002 AEN <aen@altlinux.ru> 1.1.7-alt2
- pkgconfig file added to devel

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Sun Aug 25 2002 Rider <rider@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.0-alt1
- 1.1.0
- Moved static library to devel-static subpackage.

* Sat Jan 13 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.4-ipl2mdk
- RE adaptions.

* Thu Nov 16 2000 Vincent Saugey <vince@mandrakesoft.com> 1.0.4-2mdk
- add provides to dev package

* Mon Oct 30 2000 Vincent Saugey <vince@mandrakesoft.com> 1.0.4-1mdk
- Up to 1.0.4
- Put auconf macro and gnetconfig binarie in devel package
- make compliant with new mandrake lib policy
- add dependencie on dev package
- Patch configure for gnet.h found gnetconfig.h in /usr/lib

* Mon Oct  2 2000 Vincent Saugey <vince@mandrakesoft.com> 1.0.3-4mdk
- Change devel doc to devel package

* Fri Sep  1 2000 Vincent Saugey <vince@mandrakesoft.com> 1.0.3-3mdk
- change name
- Rebuild for next release

* Tue Aug 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.3-2mdk
- macros
- BM

* Tue Jul  4 2000 Vincent Saugey <vince@mandrakesoft.com> 1.0.3-1mdk
- First mdk release
- Mandrake adaptation
- Clean spec file

* Mon Feb 28 2000 David Helder <dhelder@umich.edu>
- Updated for version 1.0

* Sat Jan 15 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- Moved lib*.so and lib*a to the devel package
- Creation of a gnet.spec.in for autoconf process

* Wed Jan 14 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- HTML documentation has been move to /usr/doc/gnet-{version}/html

* Thu Jan 13 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- First try at an RPM
