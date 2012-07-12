%define cvs 20091223
Name: libtuxcap
Version: 1.4.0
Release: alt1.cvs%cvs.4
License: GNU
Summary: The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap Games Framework used for 2D game development.
Group: System/Libraries
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Url: http://sourceforge.net/projects/tuxcap/
Source: %name-%cvs.tar.gz

BuildPreReq: ImageMagick-tools

# Automatically added by buildreq on Wed Dec 23 2009
BuildRequires: cmake gcc-c++ libGL-devel libImageMagick-devel libSDL_mixer-devel libX11-devel python-devel xorg-xf86vidmodeproto-devel

%description
The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap Games Framework used
for 2D game development. It comes with PyCap Python bindings, a fast 2D physics engine,
a particle engine, widgets and many documented examples.

%package devel
Group: Development/C
Requires: %name = %version-%release
Summary: Development headers for %name

%description devel
Development headers for TuxCap Games Framework

%prep
%setup -q -n %name-%cvs

#%__subst "s|pythondemo1||g" tuxcap/CMakeLists.txt
sed -i '/pythondemo1/d' tuxcap/CMakeLists.txt

%build
%cmake
%make_build -C BUILD

%install
%make install DESTDIR=%buildroot -C BUILD

%files
%_libdir/*.so.*

%files devel
%doc AUTHORS CHANGELOG COPYRIGHT README TODO doc/*
%_includedir/*
%_libdir/*.so

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.cvs20091223.4
- Fixed build

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1.cvs20091223.3
- Rebuild with new libImageMagick

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1.cvs20091223.2.1
- Rebuild with Python-2.7

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1.cvs20091223.2
- rebuild with new ImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1.cvs20091223.1
- rebuild with new ImageMagick

* Wed Dec 23 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1.cvs20091223
- Build for ALT

