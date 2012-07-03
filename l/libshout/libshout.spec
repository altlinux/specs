%def_without static

Name: libshout
Version: 1.0.9
Release: alt5

Summary: libshout - icecast source streaming library
Group: System/Libraries
License: %lgpl2only

Url: http://www.icecast.org
Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: ftp://ftp.icecast.org/pub/libshout/%name-%version.tar
Patch0: %name-1.0.9-alt-buffer_overflow.patch
Patch1: %name-1.0.9-alt-types.patch

BuildRequires(pre): rpm-build-licenses

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package devel
Summary: icecast source streaming library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server. Install libshout-devel if
you want to develop applications using libshout.

%package devel-static
Summary: icecast static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static version of libshout library. Install
libshout-devel-static if you want to develop applications statically linked
with libshout.

%prep
%setup -q
%patch0
%patch1

%build
%autoreconf
%def_enable Werror
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%if_without static
rm -f -- %buildroot%_libdir/*.a
%endif

rm -rf -- %buildroot%_prefix/doc


%files
%_libdir/*.so.*
%doc AUTHORS CHANGES README

%files devel
%_includedir/*
%_libdir/*.so
%doc doc/{*.html,*.css} example

%if_with static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Jul 14 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt5
- Fix buffer overflow in sock_connect_wto() function.
- Build with -Werror.
- Minor spec cleanup.

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.9-alt4
- Minor spec cleanup.
- Adopted packager.

* Fri Dec 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.9-alt3
- do not package .la files.
- do not build devel-static subpackage by default.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.9-alt2
- Rebuild with gcc-3.2. 

* Mon May 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.9-alt1
- 1.0.9
- Adopted for Sisyphus.

* Tue Mar 21 2000 Jeremy Katz <katzj@icecast.org> 1.0.7-1
- split into libshout and libshout-devel packages

* Tue Mar 21 2000 Jack Moffitt <jack@icecast.org>
- new version

* Wed Mar 15 2000 Jack Moffitt <jack@icecast.org>
- More files to get installed

* Wed Mar 15 2000 Jeremy Katz <katzj@icecast.org>
- Clean up the spec file a tad
- Do an ldconfig after installing the lib

* Tue Mar 14 2000 Jack Moffitt <jack@icecast.org>
- First official rpm build, using 1.0.0
