Name: libmp3hip
Version: 0.1.2.1
Release: alt1
Summary: A LGPLed mpeg audio decoding library.
License: LGPLv2+
Group: System/Libraries
Url: https://launchpad.net/ubuntu/+source/libmp3hip/0.1.2.1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: python-devel

%description
Based off of Michael Hipp's mpglib 0.2a <http://www.mpg123.de/>, with
many improvements by the lame development team (see AUTHORS).

The interface to the library is based off of vorbisfile.  If you add mp3
support to your app using this library it should be a snap to add Ogg
Vorbis support as well.

This isn't as fast as mpg123 will be for decoding as none of it is in
assmbler.

%package devel
Summary: Development files of libmp3hip
Group: Development/C
Requires: %name = %version-%release

%description devel
Based off of Michael Hipp's mpglib 0.2a <http://www.mpg123.de/>, with
many improvements by the lame development team (see AUTHORS).

The interface to the library is based off of vorbisfile.  If you add mp3
support to your app using this library it should be a snap to add Ogg
Vorbis support as well.

This isn't as fast as mpg123 will be for decoding as none of it is in
assmbler.

This package contains development files of libmp3hip.

%package -n python-module-hip
Summary: Python module of libmp3hip
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-hip
Based off of Michael Hipp's mpglib 0.2a <http://www.mpg123.de/>, with
many improvements by the lame development team (see AUTHORS).

The interface to the library is based off of vorbisfile.  If you add mp3
support to your app using this library it should be a snap to add Ogg
Vorbis support as well.

This isn't as fast as mpg123 will be for decoding as none of it is in
assmbler.

This package contains python module of libmp3hip.

%prep
%setup

%build
./autogen.sh
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-static=no \
	--enable-python \
	--with-installation-domain=SYSTEM

%make_build_ext \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -m644 AUTHORS README TODO %buildroot%_docdir/%name-0.1/

%files
%doc %_docdir/%name-0.1
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%files -n python-module-hip
%python_sitelibdir/*

%changelog
* Sun Dec 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2.1-alt1
- Initial build for Sisyphus

