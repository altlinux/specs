%define tag beta
%define stamp 6852ded9
%define soversion 2

Name: fastcgi++
Version: 2.0
Release: alt4.svn.%tag.%stamp.1
Summary: A C++ FastCGI Library

Group: System/Libraries
License: LGPLv3
Url: http://savannah.nongnu.org/projects/fastcgipp/
Packager: Anatoly Lyutin <vostok@altlinux.org>

Source: %name-%version%tag-%stamp.tar

Patch: make_addlibs.patch

# Automatically added by buildreq on Mon Dec 06 2010
BuildRequires: boost-devel gcc-c++ libmysqlclient-devel

%description
fastcgi++ is a C++ library for developing Web applications in C++ with the
FastCGI protocol. This library does not support the old CGI protocol. It
effectively manages simultaneous requests without the need for multiple
threads. Session data is organized into meaningful data types as opposed to a
series of text strings. Internationalization and Unicode support is another
priority. The library is templated to allow internal wide character use, while
converting down to UTF-8 upon transmission to the client.

%package -n lib%name%soversion
Summary: A C++ FastCGI library
License: LGPLv3
Group: System/Libraries

%description -n lib%name%soversion
fastcgi++ is a C++ library for developing Web applications in C++ with the
FastCGI protocol. This library does not support the old CGI protocol. It
effectively manages simultaneous requests without the need for multiple
threads. Session data is organized into meaningful data types as opposed to a
series of text strings. Internationalization and Unicode support is another
priority. The library is templated to allow internal wide character use, while
converting down to UTF-8 upon transmission to the client.

%package -n lib%name-devel
Summary: A C++ FastCGI library
License: LGPLv3
Group: Development/C++
Requires: lib%name%soversion = %version-%release

%description -n lib%name-devel
A C++ FastCGI library

%package -n lib%name-devel-static
Summary: A C++ FastCGI library
License: LGPLv3
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
A C++ FastCGI library

%prep
%setup -n %name-%version%tag-%stamp
%patch0 -p0

%build
%autoreconf -I config
%configure
%make_build

%install
%makeinstall
rm -f %buildroot%_libdir/*.la
mkdir -p %buildroot%_docdir/%name
mv %buildroot%_datadir/%name/doc/html %buildroot%_docdir/%name

%files -n lib%name-devel
%_docdir/%name
%dir %_includedir/%name
%dir %_includedir/asql
%_includedir/%name/*.h*
%_includedir/asql/*.h*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name%soversion
%doc README LICENSE_1_0.txt AUTHORS NEWS TODO THANKS
%_libdir/*.so.*

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt4.svn.beta.6852ded9.1
- Rebuilt with Boost 1.49.0

* Fri Dec 02 2011 Anatoly Lyutin <vostok@altlinux.org> 2.0-alt4.svn.beta.6852ded9
- rebuild with new boost

* Tue Jul 26 2011 Anatoly Lyutin <vostok@altlinux.org> 2.0-alt3.svn.beta.6852ded9
- new version

* Mon Mar 14 2011 Anatoly Lyutin <vostok@altlinux.org> 2.0-alt2.svn.beta.8ead2aff
- rebuild

* Tue Jan 25 2011 Anatoly Lyutin <vostok@altlinux.org> 2.0-alt1.svn.beta.8ead2aff
- new version
- droped configure_boost_macros.patch

* Thu Dec 02 2010 Anatoly Lyutin <vostok@altlinux.org> 2.0-alt0.svn.beta.b4ffcb49
- initial build for Sisyphus

