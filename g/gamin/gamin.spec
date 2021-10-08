Name: gamin
Version: 0.1.10
Release: alt7

%def_disable debug
%def_disable check
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

%prep
%setup -q
%patch
%patch10
%patch11
%patch12

%build
%autoreconf
%configure --disable-static \
    %{subst_enable debug} \
    %{subst_enable server}
%make_build

%if_enabled check
%make tests
%endif

%install
%makeinstall

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS ChangeLog Copyright NEWS README TODO \
    %buildroot%pkgdocdir/
bzip2 -9 %buildroot%pkgdocdir/ChangeLog
ln -s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING
install -p -m644 doc/*.{html,gif,txt} \
    %buildroot%pkgdocdir/

rm -fv %buildroot%_libdir/libgamin_shared.a

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
%_libdir/pkgconfig/*

%changelog
* Fri Oct 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.10-alt7
- Fixed FTBFS: rebuild without static library.

* Mon May 25 2020 Grigory Ustinov <grenka@altlinux.org> 0.1.10-alt6
- Fixed FTBFS: rebuild without python support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt5.2.qa2
- NMU: applied repocop patch

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.10-alt5.2.qa1
- NMU: rebuilt for updated dependencies.

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt5.2
- Disabled checking

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
