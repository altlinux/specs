Name:		libsfml
Version:	1.6
Release:	alt2.1
Group:		System/Libraries
License:	zlib
Summary:	Multimedia C++ API that provides low and high level access to graphics, input, audio, etc.
Source:		SFML-%version-sdk-linux-32.tar.gz
Patch:		SFML-1.6-reqlibs.patch
Patch1:		SFML-1.6-make_build.patch
patch2: libsfml-1.6-alt-gcc4.6.patch

# /*G*/ Gosh, too many dependencies are optimized out!
BuildRequires: zlib-devel libXrandr-devel libqt4-devel

# Automatically added by buildreq on Fri May 13 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libX11-devel libXrandr-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libstdc++-devel pkg-config xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ libglew-devel libgtk+2-devel libjpeg-devel libopenal-devel libsndfile-devel libwxGTK-devel

%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL. SFML is composed of several
packages to perfectly suit your needs. You can use SFML as a minimal windowing
system to interface with OpenGL, or as a fully-featured multimedia library for
building games or interactive programs.

%package devel
Summary: Development environment for %name
Group: Development/C++
Requires: %name = %version

%description devel
Development environment for %name

%package samples
Summary: Examples applications of %name
Group: Development/Documentation

%description samples
Examples applications of %name

%prep
%setup -n SFML-%version
%patch -p0
%patch1 -p0
%patch2 -p2

# Binaries
rm -f lib/*
# devel versions
for s in audio graphics network system window; do
  ln -s libsfml-$s.so.%version lib/libsfml-$s.so
done

(
cd src/SFML
sed -i '/ -l[a-zA-Z]/s@\( -l[a-zA-Z]\)@ -L../../../lib -lsfml-system\1@' Audio/Makefile
sed -i '/ -l[a-zA-Z]/s@\( -l[a-zA-Z]\)@ -L../../../lib -lsfml-system\1@' Window/Makefile
)
sed -i 's/ -lGLU/ -lGL -lGLU/' samples/window/Makefile
sed -i 's/ -lsfml-system/ -lsfml-system -lX11/' samples/wxwidgets/Makefile

%build
%make_build

%make_build -C samples LDFLAGS="-L../../lib"

%install
make DESTDIR=%buildroot DESTLIBDIR=%buildroot%_libdir DESTINCDIR=%buildroot%_includedir install

cp -r samples/bin %buildroot%_libdir/%name-samples

%files
%doc readme-en.txt
%_libdir/*.so.*

%files devel
%doc doc
%_includedir/SFML
%_libdir/*.so

%files samples
%doc samples/[^b]*
%_libdir/%name-samples

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.1
- Fixed build

* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 1.6-alt2
- DSO list completion

* Sat May 14 2011 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Initial build from scratch

