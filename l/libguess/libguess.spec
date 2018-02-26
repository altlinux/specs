Name: libguess
Version: 0.2.0
Release: alt4

Summary: library for detecting far east encodings

License: BSD
Group: System/Libraries
Url: http://www.nongnu.org/libtranslate/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version-d7.tar.gz
Patch: libguess-ds-cn.patch

%description
libguess is a library for autodetecting Chinese(Traditional/Simplified),Korean
and Japanese encodings.

%package devel
Summary: Header files for libguess
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for libguess.

%prep
%setup -q -n %name-%version-d7
%patch -p1

%build
%make_build

%install
subst "s|\${PREFIX}\/lib|%buildroot%_libdir|g" Makefile
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
%make PREFIX=%buildroot%_prefix install

ln -sf %name.so.%version %buildroot%_libdir/%name.so.0
ln -sf %name.so.%version %buildroot%_libdir/%name.so

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 0.2.0-alt4
- rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt3
- Rebuilt for soname set-versions

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release

