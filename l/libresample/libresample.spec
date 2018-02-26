Name: libresample
Version: 0.1.3
Release: alt4
Summary: real-time resampling library
Group: Development/C
License: LGPL

Url: http://svn.digium.com/svn/thirdparty/libresample/trunk

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Jul 05 2009
BuildRequires: libsamplerate-devel libsndfile-devel

%package devel
Summary: %summary
Group: %group

%description devel
%summary

%description
This library is not the highest-quality resampling library
available, nor is it the most flexible, nor is it the
fastest.  But it is pretty good in all of these regards, and
it is quite portable.  The best resampling library I am aware
of is libsamplerate by Erik de Castro Lopo.  It's small, fast,
and very high quality.  However, it uses the GPL for its
license (with commercial options available) and I needed
a more free library.  So I wrote this library, using
the LGPL resample-1.7 library by Julius Smith as a basis.

%prep
%setup
%build
%configure
%make_build
%install
%make_install INSTALL_PREFIX=%buildroot install
%files
%_libdir/libresample.so.1.0

%files devel
%_includedir/libresample.h
%_libdir/libresample.so

%changelog
* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt4
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt3
- auto rebuild

* Mon Oct 26 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt2
- Add Url tag

* Sun Jul 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt1
- first build for Sisyphus
