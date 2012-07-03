Name: libalut
Version: 1.1.0
Release: alt5
Group: System/Libraries
Summary: Freealut is a free implementation of OpenAL's ALUT standard
Url: http://openal.org
License: GPL

Source:	freealut-1.1.0.tar.gz
Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildRequires: libopenal-devel

%description
Freealut is a free implementation of OpenAL's ALUT standard
This package contains shared library

%package devel
Group: Development/C
Summary: Freealut is a free implementation of OpenAL's ALUT standard
Requires: %name = %version-%release

%description devel
Freealut is a free implementation of OpenAL's ALUT standard
This package contains development files

%prep
%setup -n freealut-%version

%build
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/AL
%_bindir/freealut-config
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5
- Rebuilt for debuginfo

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0-alt4.1
- rebuild (with the help of girar-nmu utility)

* Thu Nov 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4
- Rebuilt for soname set-versions

* Tue Mar 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt3
- rebuild with libopenal.so.1

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libalut
  * postun_ldconfig for libalut

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.1.0-alt2
- Fixed openal dependency search

* Thu Mar 22 2007 Albert R. Valiev <darkstar@altlinux.ru> 1.1.0-alt1.2
- bug #11176 fix

* Thu Feb 15 2007 Albert R. Valiev <darkstar@altlinux.ru> 1.1.0-alt1.1
- Spec fixes

* Thu Feb 15 2007 Albert R. Valiev <darkstar@altlinux.ru> 1.1.0-alt1
- Initial build

