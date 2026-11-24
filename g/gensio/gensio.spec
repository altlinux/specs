Name: gensio
Version: 3.0.4
Release: alt1

Summary: General Stream I/O library
License: GPL-2.0-or-later
Group: Communications
URL: https://github.com/cminyard/gensio
VCS: https://github.com/cminyard/gensio

Source: %name-%version.tar

BuildRequires: gcc-c++ swig python3-dev
BuildRequires: pkgconfig(openssl)

%package -n libgensio
Summary: General Stream I/O shared library
Group: System/Libraries

%package -n libgensio-devel
Summary: Development files for libgensio
Group: Development/C

%package -n python3-module-gensio
Summary: Python bindings for gensio
Group: Development/Python

%define desc\
gensio is a general library for managing streaming I/O. It hides the\
details of the underlying I/O like serial ports, network connections,\
etc., and provides a consistent interface on top of them. It is the\
I/O library used by ser2net.

%description %desc

%description -n libgensio %desc
This package contains gensio shared libraries.

%description -n libgensio-devel %desc
This package contains header files and development libraries.

%description -n python3-module-gensio %desc
This package contains python bindings to gensio.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--without-tcl \
	--without-go \
	--without-soapy \
	--without-sound \
	--without-alsa \
	--without-portaudio \
	--without-openipmi \
	--without-avahi \
	--without-dnssd \
	--without-cm108gpio \
	--without-tcp-wrappers \
	--with-pythoninstall=%python3_sitelibdir \
	#
%make_build

%install
%makeinstall_std
rm %buildroot%_bindir/gsound

%files
%doc COPYING README.rst
%_bindir/gagwpe
%_bindir/gensiot
%_bindir/greflector
%_bindir/gtlssh
%_bindir/gtlssh-keygen
%_bindir/gtlssync
%_bindir/gsh
%_man1dir/*.1*
%_man5dir/*.5*

%files -n libgensio
%_libdir/libgensio*.so.*
%exclude %_libdir/libgensio_python_swig.so.*
%_libexecdir/gensio

%files -n libgensio-devel
%_includedir/gensio
%_libdir/libgensio*.so
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%files -n python3-module-gensio
%_libdir/libgensio_python_swig.so.*
%python3_sitelibdir/*.py
%python3_sitelibdir/*/*.py*
%python3_sitelibdir/*.so

%changelog
* Fri Nov 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.4-alt1
- 3.0.4 released

