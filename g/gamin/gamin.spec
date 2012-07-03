Name: gamin
Version: 0.1.10
Release: alt5.1

%def_disable static
%def_disable debug
%def_enable  check
%def_enable server

Summary: Lightweight replacement of the File Alteration Monitor
Group: System/Servers
License: LGPLv2+
URL: http://www.gnome.org/~veillard/gamin/

Requires: lib%name = %version-%release

%define pkgdocdir %_docdir/%name-%version

Source: ftp://ftp.gnome.org/pub/GNOME/sources/gamin/%version/%name-%version.tar.bz2
Patch: gamin-0.1.10-alt-deperecations.patch

# Suse patches
Patch10: gamin-0.1.10-suse-return.patch
Patch11: gamin-0.1.10-suse-fam_abi_compatibility_FamErrlist.patch
Patch12: gamin-0.1.10-suse-fix_python_main.patch

BuildPreReq: rpm-build-python python-dev
%{?_enable_server:BuildRequires: glib2-devel}
BuildRequires: common-licenses

%description
Gamin is a file and directory monitoring system defined to be
a subset of the FAM (File Alteration Monitor) system. This is
a service provided by a library which allows to detect when a
file or a directory has been modified.

%package -n lib%name
Summary: Shared libraries for Gamin, a file and directory monitoring system
Group: System/Libraries

%description -n lib%name
Gamin is a file and directory monitoring system defined to be
a subset of the FAM (File Alteration Monitor) system. This is
a service provided by a library which allows to detect when a
file or a directory has been modified.

%package -n lib%name-fam
Summary: FAM compatilitity libraries for Gamin
Group: System/Libraries
Conflicts: libfam

%description -n lib%name-fam
Libraries from the Gamin system that provide binary compatibility with
FAM (File Alteration Monitor).

%package -n lib%name-devel
Summary: Development files for Gamin, a file and directory monitoring system
Group: Development/C
Requires: lib%name = %version-%release
Requires: lib%name-fam = %version-%release
Provides: gamin-devel = %version
Obsoletes: gamin-devel
Provides: libfam-devel
Obsoletes: libfam-devel

%description -n lib%name-devel
Files necessary to develop applications using Gamin.
Gamin is a file and directory monitoring system defined to be
a subset of the FAM (File Alteration Monitor) system.

%package -n lib%name-devel-static
Summary: Static libraries for Gamin, a file and directory monitoring system
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static library build of Gamin.
Gamin is a file and directory monitoring system defined to be
a subset of the FAM (File Alteration Monitor) system.

%package -n python-module-%name
Summary: Python bindings for Gamin, a file and directory monitoring system
Group: Development/Python
Obsoletes: python-modules-%name
Provides: python-modules-%name = %version-%release
Requires: lib%name = %version-%release

%description -n python-module-%name
Python scripting language bindings for Gamin.
Gamin is a file and directory monitoring system defined to be
a subset of the FAM (File Alteration Monitor) system.

%prep
%setup -q
%patch
%patch10
%patch11
%patch12

%build
%autoreconf
%configure \
    %{subst_enable debug} \
    %{subst_enable static} \
    %{subst_enable server}
%make_build

%if_enabled check
%make tests
%endif

%install
%makeinstall

%__install -d -m755 %buildroot%pkgdocdir
%__install -p -m644 AUTHORS ChangeLog Copyright NEWS README TODO \
    %buildroot%pkgdocdir/
%__bzip2 -9 %buildroot%pkgdocdir/ChangeLog
%__ln_s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING
%__install -p -m644 doc/*.{html,gif,txt} \
    %buildroot%pkgdocdir/

# remove non-packaged files
%__rm -f %buildroot/%python_sitelibdir/*.la

%if_enabled server
%files
%_libexecdir/gam_server
%pkgdocdir
%endif

%files -n lib%name
%_libdir/libgamin*.so.*

%files -n lib%name-fam
%_libdir/libfam.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/libgamin_shared.a
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%exclude %_libdir/libgamin_shared.a
%endif

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Sun Nov 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.10-alt5.1
- Rebuild with Python-2.7

* Sun Nov 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt5
- build without DG_DISABLE_DEPRECATED

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt4
- rebuilt for debuginfo

* Thu Oct 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt3
- rebuild

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt2.1
- Rebuilt with python 2.6

* Thu Feb 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt2
- renamed python-modules-gamin to python-module-gamin

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10
- updated buildreqs
- fix license tag, source url

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.1.9-alt1.1
- Rebuilt with python-2.5.

* Sun Jan 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.9-alt1
- new version
- add watch file

* Sun Nov 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.1.8-alt1
- new version 0.1.8

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.7-alt3
- x86_64 fix: specify gam_server location via %%_libexecdir

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.7-alt2
- Renamed gamin-devel to libgamin-devel (bug 9086)
- libgamin-devel provides libfam-devel

* Thu Jan 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.7-alt1
- First release for Sisyphus
