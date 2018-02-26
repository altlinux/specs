%def_enable shared
%def_disable static
%def_with doc

%define sonum 1
%define libname libmpd

Name: %libname%sonum
Version: 0.19.0
Release: alt3
Summary: Client library for MPD
License: GPLv2+
Group: System/Libraries
URL: http://gmpcwiki.sarine.nl/index.php/Libmpd
Source: %name-%version.tar
Patch: %name-%version-alt1.patch
Packager: Alexey Rusakov <ktirf@altlinux.org>

Provides: %libname

BuildRequires: glib2-devel
%{?_with_doc:BuildRequires: doxygen}

%description
Libmpd is an a library to easily connect to a Music Player Daemon
server. It's wraps around libmpdclient and provides a higher level API.
GMPC, Gnome Music Player Client, relies on this library to work with
MPD.


%package -n %libname-devel
Summary: Development environment for %libname
Group: Development/C
%if_enabled shared
Requires: %name = %version-%release
%else
Requires: %libname-devel-static = %version-%release
%endif

%description -n %libname-devel
This package contains the header files and libraries for building
programs that use %libname.


%if_enabled static
%package -n %libname-devel-static
Summary: Static %libname
Group: Development/C
Requires: %libname-devel = %version-%release

%description -n %libname-devel-static
This package contains static %libname.
%endif

%if_with doc
%package doc
Summary: Documentation for %libname
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for %libname.
%endif

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    %{subst_enable shared} \
    %{subst_enable static} \
    --with-pic \
    --with-gnu-ld
%make_build all %{?_with_doc:doc}

%install
%makeinstall_std
%if_with doc
install -d -m 0755 %buildroot%_docdir/%name-%version/html
install -m 0644 ChangeLog %buildroot%_docdir/%name-%version/
install -m 0644 doc/html/* %buildroot%_docdir/%name-%version/html/
%endif

%if_enabled shared
%files
%_libdir/*.so.*
%endif

%files -n %libname-devel
%{?_enable_shared:%_libdir/*.so}
%_includedir/*
%_pkgconfigdir/*

%if_enabled static
%files -n %libname-devel-static
%_libdir/*.a
%endif

%if_with doc
%files doc
%_docdir/%name-%version
%endif

%changelog
* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.19.0-alt3
- Disabled %libname-devel-static.
- Rebuilt for debuginfo.

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19.0-alt2
- Rebuilt for soname set-versions

* Sun Sep 20 2009 Alexey Rusakov <ktirf@altlinux.org> 0.19.0-alt1
- 0.19.0 release

* Tue Sep 01 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.100-alt1
- 0.19 RC (updated from git)

* Tue Jul 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt2
- fixed a wrong macro for a buffer size passed to snprintf

* Thu Mar 12 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- 0.18.0
- new Packager

* Thu Jan 08 2009 Led <led@altlinux.ru> 0.17.0-alt1
- 0.17.0
- cleaned up spec

* Wed Nov 12 2008 Led <led@altlinux.ru> 0.16.5-alt0.1
- 0.16.5 beta1

* Sun Oct 19 2008 Led <led@altlinux.ru> 0.16.1-alt2
- updated from upstream SCM for some fixes

* Sat Oct 04 2008 Led <led@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Fri Oct 03 2008 Led <led@altlinux.ru> 0.16.0-alt1
- 0.16.0
- fixed License
- fixed Group
- fixed URL
- cleaned up BuildRequires
- cleaned up spec
- added doc package

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.0-alt1
-  new version.

* Tue Jun 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14.0-alt1
- new version (0.14.0)
- updated Url and Source links
- removed unneeded buildreq of gcc-c++
- pass --disable-static to configure script.
- updated description and summary

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.5rev4832-alt1
-  initial build for ALTLinux Sisyphus.
