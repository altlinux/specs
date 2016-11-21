Name: libguess
Version: 1.2
Release: alt1.1

Summary: high-speed character set detection library
License: BSD
Group: System/Libraries
Url: http://rabbit.dereferenced.org/~nenolod

Source: %url/distfiles/%name-%version.tar.bz2

Obsoletes: %{name}1 < 1.2
Provides: %{name}1 = %version-%release

%description
%name is a library for autodetecting encodings.

%package devel
Summary: Header files for libguess
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for libguess.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Nov 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1.1
- fixed "Obsoletes" tag

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2
- new source %url
- obsoletes/provides libguess1

* Mon Jan 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.0-alt4.qa1
- NMU: rebuilt for updated dependencies.

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 0.2.0-alt4
- rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt3
- Rebuilt for soname set-versions

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release

