Name: libmp3hip
Version: 0.1.2.1
Release: alt4

Summary: A LGPLed mpeg audio decoding library
License: LGPLv2+
Group: System/Libraries

Url: https://launchpad.net/ubuntu/+source/libmp3hip/0.1.2.1
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Patch0: %name-fix-definition.patch

BuildRequires(pre): rpm-macros-make
BuildPreReq: python-devel

%description
Based off of Michael Hipp's mpglib 0.2a <http://www.mpg123.de/>, with
many improvements by the lame development team (see AUTHORS).

The interface to the library is based off of vorbisfile.  If you add mp3
support to your app using this library it should be a snap to add Ogg
Vorbis support as well.

This isn't as fast as mpg123 will be for decoding as none of it is in
assembler.

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
assembler.

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
assembler.

This package contains python module of libmp3hip.

%prep
%setup
%patch0 -p2

cp -at . -- /usr/share/gnu-config/config.{guess,sub}
sed -i 's,-O20,-O%_optlevel,g' configure*
sed -i 's,-all-static,,' examples/Makefile*

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *) \
        $(find ./ -name '*.py')
subst 's|python|%__python|' python/Makefile.am

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
* Fri Dec 11 2020 Pavel Vasenkov <pav@altlinux.org> 0.1.2.1-alt4
- NMU: fix variable definition

* Fri Aug 07 2020 Pavel Vasenkov <pav@altlinux.org> 0.1.2.1-alt3
- NMU: set correct python2 executable in shebang and scripts

* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 0.1.2.1-alt2
- Update gnu-config files for the new arches
- Fix superfluous optimization level
- Avoid static (mis)linking of the example binary

* Sun Dec 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2.1-alt1
- Initial build for Sisyphus

