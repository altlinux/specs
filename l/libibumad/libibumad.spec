%def_enable shared
%def_enable static

Name: libibumad
Version: 1.3.6
Summary: OpenFabrics Alliance InfiniBand umad (user MAD) library
Release: alt2
License: %gpl2only, %bsdstyle
Group: System/Libraries
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libibcommon-devel

%description
%name provides the user MAD library functions which sit on top of
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM.


%if_enabled shared
%package devel
Summary: Development files for the %name library
Group: Development/C
Requires: %name%{?_disable-shared:-devel-static} = %version-%release
Requires: libibcommon-devel
%endif

%description devel
Development files for the %name library.


%package devel-man
Summary: Manuals for development with the %name library
Group: Development/Documentation
BuildArch: noarch

%description devel-man
Manuals for development with the %name library.


%if_enabled static
%package devel-static
Summary: Static version of the %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static version of the %name library.
%endif

%prep
%setup


%build
./autogen.sh
%configure %{subst_enable shared} %{subst_enable static}
%make_build
gzip -9c ChangeLog > ChangeLog.gz


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 AUTHORS COPYING ChangeLog.* %buildroot%_docdir/%name-%version/
rm -f %buildroot%_libdir/*.la


%if_enabled shared
%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/COPYING
%_libdir/*.so.*
%endif


%files devel
%_includedir/infiniband/*
%if_enabled shared
%_libdir/*.so
%else
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/COPYING
%endif


%files devel-man
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/ChangeLog.*
%_man3dir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt2
- Rebuilt for debuginfo

* Wed Dec 15 2010 Timur Aitov <timonbl4@altlinux.org> 1.3.6-alt1
- New version

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt2
- Rebuilt for soname set-versions

* Tue Aug 31 2010 Andriy Stepanov <stanv@altlinux.ru> 1.3.5-alt1
- New version

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Rebuild from upstream git repository

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.1
- Build for Sisyphus

* Tue May 26 2009 Led <led@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt2
- Add static package

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.1.7-alt0.M41.1
- build for 4.1

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.1.7-alt1
- ODED 1.3.1

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.6-alt1
- Initial release
