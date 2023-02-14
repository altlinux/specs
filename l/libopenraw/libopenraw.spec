%def_disable snapshot

%define gdk_pixbuf_moduledir  %(pkg-config --variable gdk_pixbuf_moduledir gdk-pixbuf-2.0)
%define api_ver 0.3

%def_enable gnome
%def_disable bootstrap

Name: libopenraw
Version: 0.3.4
Release: alt1

Summary: Decode camera RAW files
Group: System/Libraries
License: GPL-3.0-or-later and LGPL-3.0-or-later
Url: https://libopenraw.freedesktop.org/

%if_disabled snapshot
Source: https://libopenraw.freedesktop.org/download/libopenraw-%version.tar.bz2
%else
Vcs: https://gitlab.freedesktop.org/libopenraw/libopenraw.git
Source: %name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %name-%version-mp4.tar}

BuildRequires: autoconf-archive boost-devel gcc-c++ libcurl-devel libgio-devel
BuildRequires: libjpeg-devel libxml2-devel
# for CR3 support (lib/mp4)
BuildRequires: /proc rust rust-cargo
%{?_enable_gnome:BuildRequires: libgdk-pixbuf-devel}

%description
libopenraw is an ongoing project to provide a free software implementation for
camera RAW files decoding. One of the main reason is that dcraw is not suited
for easy integration into applications, and there is a need for an easy to use
API to build free software digital image processing application.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name.

%package gnome
Summary: GUI components of libopenraw
Group: System/Libraries
Requires: %name = %version-%release

%description gnome
The %name-gnome package contains gui components of %name.

%package gnome-devel
Summary: Development files for %name-gnome
Group: Development/C
Requires: %name-gnome = %version-%release
Requires: %name-devel = %version-%release

%description gnome-devel
The %name-gnome-devel package contains libraries and header files for developing
applications that use %name-gnome.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
pushd lib/mp4
cargo vendor -s Cargo.toml -s mp4parse/Cargo.toml -s mp4parse_capi/Cargo.toml
mkdir .cargo
cat << _EOF_ >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
_EOF_
tar -cf %_sourcedir/%name-%version-mp4.tar vendor .cargo
popd
}
#mv vendor .cargo lib/mp4
sed -i 's/byteorder = "1.2.1"/byteorder = "1.2.2"/' lib/mp4/mp4parse/Cargo.toml

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static \
    %{subst_enable gnome}
%make_build

%install
%makeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make check

%files
%_libdir/%name.so.*
%gdk_pixbuf_moduledir/*.so
%exclude %gdk_pixbuf_moduledir/*.la
%doc AUTHORS NEWS README TODO RELEASE_NOTES

%files devel
%dir %_includedir/%name-%api_ver
%_includedir/%name-%api_ver/%name
%_libdir/%name.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled gnome
%files gnome
%_libdir/%{name}gnome.so.*

%files gnome-devel
%_includedir/%name-%api_ver/%name-gnome/
%_libdir/%{name}gnome.so
%_pkgconfigdir/%name-gnome-%api_ver.pc
%endif

%changelog
* Wed Feb 15 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Fri Dec 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Tue Jun 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- updated to 0.3.1-12-gf2cfeee

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1.1
- fixed boost.m4 for e2k

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Jan 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.0.9-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Dec 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9
- removed upstreamed patch2

* Thu Sep 16 2010 Victor Forsiuk <force@altlinux.org> 0.0.8-alt2
- Add patches to fix ALT #24093.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 0.0.8-alt1
- 0.0.8

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.0.5-alt2
- Remove obsolete ldconfig calls.

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 0.0.5-alt1
- 0.0.5

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 0.0.3-alt1
- 0.0.3

* Thu May 17 2007 Victor Forsyuk <force@altlinux.org> 0.0.2-alt1
- Initial build.
