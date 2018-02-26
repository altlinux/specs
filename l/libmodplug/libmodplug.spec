Name: libmodplug
Version: 0.8.8.4
Release: alt1

Summary: Modplug mod music file format library
License: Public Domain
Group: Sound
Url: http://modplug-xmms.sourceforge.net/
Packager: Yury Aliaev <mutabor@altlinux.ru>
# http://download.sourceforge.net/modplug-xmms/%name-%version.tar.gz
Source: %name-%version.tar
Patch: libmodplug-0.8.8.1-rh-timidity.patch
BuildRequires: gcc-c++
# backwards compatibility
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
Provides: libmodplug.so.0%lib_suffix

%description
This is a library based on the mod rendering code from ModPlug.

%package devel
Summary: Development files for libmodplug
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files (headers and library links)
for the software development using libmodplug library.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std
# backwards compatibility
ln -s libmodplug.so.1.0.0 %buildroot%_libdir/libmodplug.so.0

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog COPYING README

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Sat Sep 03 2011 Michael Shigorin <mike@altlinux.org> 0.8.8.4-alt1
- NMU: 0.8.8.4
- Security fixes:
  CVE-2011-2911 CVE-2011-2912 CVE-2011-2913 CVE-2011-2914 CVE-2011-2915

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8.1-alt2
- Rebuilt for debuginfo

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 0.8.8.1-alt1
- Updated to 0.8.8.1.

* Fri May 01 2009 Vladimir Lettiev <crux@altlinux.ru> 0.8.7-alt1
- NMU: 0.8.7
- Security fixes:
  + CVE-2009-1438 (Closes: 19694)
  + PATinst() Buffer Overflow Vulnerability (Closes: 19824)
- removed obosolete post{,un}_ldconfig

* Sun Nov 12 2006 Yury Aliaev <mutabor@altlinux.ru> 0.8.4-alt1
- 0.8.4 issued

* Wed Apr 19 2006 Yury Aliaev <mutabor@altlinux.ru> 0.8-alt1
- 0.8 issued

* Sat Dec 20 2003 Yury Aliaev <mutabor@altlinux.ru> 0.7-alt2
- Included forgotten documentation into the package

* Wed Dec 3 2003 Yury Aliaev <mutabor@altlinux.ru> 0.7-alt1
- First build for Sisyphus.
