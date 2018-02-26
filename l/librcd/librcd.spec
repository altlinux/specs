Name: librcd
Version: 0.1.13
Release: alt1

Summary: Russian Encoding Detection Library
License: GPL
Group: System/Libraries
Source: %name-%version.tar.bz2
URL: http://rusxmms.sourceforge.net/
Packager: Nick S. Grechukh <gns@altlinux.org>

BuildRequires: gcc-c++

%description
Automatic encoding detection library for russian/ukrainian languages.
Optimized for very small words and phrases.

%package devel
Summary: Russian Encoding Detection Library
Group: Development/Other
Requires: %name = %version-%release

%description devel
Automatic encoding detection library for russian/ukrainian languages.
Optimized for very small words and phrases.

This package includes headers and shared libraries for development %name-based
applications.

%prep
%setup

%build
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README COPYING
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so

%changelog
* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 0.1.13-alt1
- 0.1.13

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt2.2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.1.11-alt2.1
- Rebuilt for soname set-versions.

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.11-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Aug 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.1.10-alt1
- 0.1.10

* Sun May 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.1.8-alt1
- NMU:	cleanup spec
	fixed libdir
	disabled static

* Thu Jan 12 2006 Nick S. Grechukh <gns@altlinux.org> 0.1.8-alt0.2
- new version

* Sat Aug 13 2005 Nick S. Grechukh <gns@altlinux.ru> 0.1.7-alt0.2
- initial build for Sisyphus
