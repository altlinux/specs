Name: libagg
Version: 2.5
Release: alt3
Summary: Anti-Grain Geometry
Group: System/Libraries
URL: http://www.antigrain.com
License: GPL

Source: agg-%version.tar.gz
Patch1: agg-2.5-alt.patch

BuildRequires: gcc-c++ libSDL-devel libX11-devel

%description
A High Quality Rendering Engine for C++

%package devel
Summary: Support files necessary to compile applications with agg
Group: Development/C++
Requires: %name = %version-%release

%description devel
Libraries, headers, and support files necessary to compile applications using agg

%prep
%setup -q -n agg-%version
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%changelog
* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt3
- droped unused libs/headers

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jan 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt1
- 2.5

* Tue May 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt1
- 2.4

* Sun Mar 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt2
- no build demos/examples
- updated build dependencies

* Wed Dec 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- initial release

