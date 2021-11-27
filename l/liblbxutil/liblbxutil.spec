%def_disable static

Name:		liblbxutil
Version:	1.1.0
Release:	alt4
License:	MIT
Group:		System/X11
Summary:	LBX utility routines
Source:		%{name}-%{version}.tar.bz2
Patch:		liblbxutil-1.1.0-alt-Xalloc.patch
Patch1:     liblbxutil-1.1.0-alt-gcc10.patch
URL:		http://cgit.freedesktop.org/xorg/lib/%name

# Automatically added by buildreq on Thu Feb 14 2013
# optimized out: pkg-config
BuildRequires: xorg-xextproto-devel xorg-xproto-devel zlib-devel

BuildRequires: xorg-util-macros

%description
liblbxutil - Low Bandwith X extension (LBX) utility routines

%package devel
Summary:	LBX utility routines -- development envoronment
License:	MIT
Group:		System/X11
Requires:	libXext-devel

%description devel
%summary -- development envoronment

%package devel-static
Summary:	LBX utility routines -- static development envoronment
License:	MIT
Group:		System/X11
Requires:	%name-devel

%description devel-static
%summary -- static development envoronment

%prep
%setup
%patch -p1
%patch1 -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall

%files
%_libdir/lib*.so.1*

%files devel
%_includedir/X11/extensions/*

%_libdir/lib*.so
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 1.1.0-alt4
- picked from orphaned
- fixed build

* Tue Apr 06 2021 Fr. Br. George <george@altlinux.ru> 1.1.0-alt3
- Fix GCC10 build

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.1.0-alt2
- Fix build

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build

