# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libavcodec)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lib_major	2
%define lib_name	libucil%{lib_major}
%define develname	libucil-devel

Summary:	Library to render text and graphic overlays onto video images
Name:		libucil
Version:	0.9.10
Release:	alt1_12
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.unicap-imaging.org/
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0:		libucil-0.9.8-bz627890.patch
Patch1:		libucil-0.9.10-leaks.patch
Patch2:		libucil-0.9.10-warnings.patch
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(libunicap)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libpng)
Source44: import.info

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{lib_name}
Summary:	Dynamic libraries for libucil
Group:		System/Libraries
Conflicts:	libunicap < 0.9.12

%description -n %{lib_name}
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{develname}
Summary:	Development libraries, include files for Ucil
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Conflicts:	libunicap-devel < 0.9.12

%description -n %{develname}
The package includes header files and libraries necessary
for developing programs which use the ucil library. It contains the API
documentation of the library, too.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -pthread"
export CXXFLAGS="$CFLAGS"

autoreconf -vfi
%configure \
	--disable-static \
	--disable-rpath \
	--disable-ucil-gstreamer
%make_build

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}
%{_libdir}/*.so.%{lib_major}.*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/libucil
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so


%changelog
* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_12
- new version

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt4.1
- Rebuilt with libpng15

* Wed Mar 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt4
- rebuild with libpng-devel, libvorbis-devel, libtheora-devel,
  libalsa-devel

* Mon Mar 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt3
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt2
- rebuild for soname set-version

* Wed May 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1
- initial
