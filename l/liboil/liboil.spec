Name: liboil
Version: 0.3.17
Release: alt1

Summary: Library of Optimized Inner Loops
License: BSD-style
Group: System/Libraries
Url: http://liboil.freedesktop.org

# http://git.altlinux.org/gears/l/liboil.git
Source: %name-%version-%release.tar

%define pkgdocdir %_docdir/%name-%version
%def_disable static
%def_enable gtk_doc
%def_enable check

BuildRequires: glib2-devel
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: /proc}

%description
Liboil is a library of simple functions that are optimized for
various CPUs.  These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to floating-poing
numbers or multiplying and summing an array of N numbers.  Clearly such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

Many multimedia applications and libraries already do similar things
internally.  The goal of this project is to consolidate some of the code
used by various multimedia projects, and also make optimizations easier
to use by a broad range of applications.

%package devel
Summary: Development environment for liboil
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for building
liboil-based software.

%package devel-doc
Summary: Development documentation for liboil
Group: Development/C
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains development documentation for the liboil library.

%package devel-static
Summary: Static liboil library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains development files required for building
statically linked liboil-based software.

%package examples
Summary: Examples for liboil
Group: Development/C
BuildArch: noarch
Requires: %name-devel = %version-%release

%description examples
This package contains examples for writing applications using
the liboil library.

%prep
%setup -q -n %name-%version-%release

%build
%autoreconf
%configure \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{subst_enable static}

# SMP-incompatible build
make

%install
%makeinstall_std
install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS BUG-REPORTING COPYING README HACKING NEWS \
	%buildroot%pkgdocdir/
make -C examples distclean
cp -a examples %buildroot%pkgdocdir/

%check
make -k -C testsuite check

%files
%_libdir/*.so.*
%pkgdocdir/
%exclude %pkgdocdir/examples

%files devel
%_bindir/oil-bugreport
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files examples
%dir %pkgdocdir
%pkgdocdir/examples/

%changelog
* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3.17-alt1
- Updated to liboil-0.3.17-2-g7059160.

* Thu Jan 07 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3.16-alt2
- Updated to liboil-0.3.16-3-g163ee94.
- Made configure.ac more friendly to autoreconf.
- Renamed and uncompressed tarball.
- Moved "make check" to %%check section.
- Fixed examples packaging.
- Updated buildreqs.

* Tue Apr 21 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.3.16-alt1
- 0.3.16 release.
- build using libtool_2.2.

* Fri Dec 05 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.15-alt2
- removed obsolete %%post{,un}_ldconfig
- don't rebuild documentation
- build -devel-doc and -examples subpackages as noarch
- modified %%files section to fix altbug #18038

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 0.3.15-alt1
- 0.3.14 -> 0.3.15

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 0.3.14-alt1
- 0.3.13 -> 0.3.14

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.3.13-alt1
- 0.3.12 -> 0.3.13
- remove obsoletes patches

* Tue Nov 06 2007 Igor Zubkov <icesik@altlinux.org> 0.3.12-alt2
- fixed build for ARM

* Fri Jun 08 2007 Igor Zubkov <icesik@altlinux.org> 0.3.12-alt1
- 0.3.10 -> 0.3.12
- sync with debian liboil_0.3.12-1.diff

* Thu Jan 18 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3.10-alt2
- Merged Debian liboil_0.3.10-1.diff.
- Removed %%__* macro abuse from specfile.
- Added ExclusiveArch tag.
- Updated build dependencies.

* Sun Dec 24 2006 Igor Zubkov <icesik@altlinux.org> 0.3.10-alt1
- 0.3.9 -> 0.3.10
- add packager tag

* Sun May 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.9-alt1
- Release 0.3.9

* Tue Apr 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.8-alt1
- Release 0.3.8
- Building with alternate optimizations is broken

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.7-alt1
- 0.3.7
- Enabled check

* Fri Nov 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.6-alt1
- Updated to 0.3.6
- Added AUTHORS, README and COPYING to the docs list
- Corrected license field
- Added examples package
- Temporarily disabled check due to a failure

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt1
- 0.3.2
- new devel-doc subpackage.

* Fri Jan 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Thu Nov 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Sat Nov 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- First build for Sisyphus
