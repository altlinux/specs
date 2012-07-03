Name: evas_generic_loaders
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: A set of loaders for Evas
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

# http://svn.enlightenment.org/svn/e/trunk/%name
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libevas-devel >= 1.2.0
BuildRequires: libpoppler-devel
BuildRequires: libraw-devel-static
BuildRequires: libspectre-devel
BuildRequires: gst-plugins-devel
BuildRequires: zlib-devel

%description
These are additional "generic" loaders for Evas that are stand-alone
executables that evas may run from its generic loader module. This means
that if they crash, the application loading the image does not crash
also. In addition the licensing of these binaries will not affect the
license of any application that uses Evas as this uses a completely
generic execution system that allows anything to be plugged in as a
loader.


%prep
%setup

%build
%configure
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_libdir/evas/utils/*
%doc AUTHORS COPYING README

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

