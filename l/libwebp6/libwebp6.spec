%define _name libwebp

%def_enable libwebpmux
%def_enable libwebpdemux
%def_enable libwebpdecoder
%define soversion 6

Name: %_name%soversion
Version: 0.5.2
Release: alt2

Summary: Library for the WebP graphics format
License: BSD
Group: System/Libraries

URL: http://webmproject.org/
Source: http://downloads.webmproject.org/releases/webp/%_name-%version.tar.gz

BuildRequires: libjpeg-devel libpng-devel libtiff-devel libgif-devel
BuildRequires: libfreeglut-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{subst_enable libwebpmux} \
	%{subst_enable libwebpdemux} \
	%{subst_enable libwebpdecoder}
%make_build

%install
%makeinstall_std

%files
%_libdir/%_name.so.*
%{?_enable_libwebpmux:%_libdir/%{_name}mux.so.*}
#%{?_enable_libwebpdemux:%_libdir/%{_name}demux.so.*}
%{?_enable_libwebpdecoder:%_libdir/%{_name}decoder.so.*}

%changelog
* Thu Feb 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt2
- compat library

* Wed Dec 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2 (fixed CVE-2016-8888, CVE-2016-9085)

* Thu Aug 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Nov 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Thu Feb 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2.2
- libwebp5: add O: libwebp = 0.4.0-alt1.

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2.1
- libwebp5: remove obsolete.

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0-alt2
- libwebp: add so version to package name.

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Oct 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.1
- Rebuilt with libpng15

* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3

* Wed Jul 13 2011 Victor Forsiuk <force@altlinux.org> 0.1.2-alt1
- Initial build.
