Name: libosip2
Summary: The GNU oSIP library
Version: 3.5.0
Release: alt1
License: LGPL
Group: System/Libraries
Url: http://www.gnu.org/software/osip/osip.html
Packager: Egor Glukhov <kaman@altlinux.org>

Source0: %name-%version.tar
BuildRequires: OpenSP docbook-dtds docbook-to-man

%description
This is "the GNU oSIP library". It has been designed to provide
the Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package devel
Summary: The GNU oSIP library - development files
Group: System/Libraries
Requires: %name = %version-%release

%description devel
Development files for the GNU oSIP library.

%package static
Summary: The GNU oSIP library - static version
Group: System/Libraries
Requires: %name-devel = %version-%release

%description static
Static version of the GNU oSIP library.

%def_disable static

%prep
%setup

%build
./autogen.sh
%configure \
	--enable-pthread \
	%{subst_enable static}
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS NEWS README TODO
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_man1dir/*

%if_enabled static
%files static
%_libdir/lib*.a
%endif

%changelog
* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.5.0-alt1
- 3.5.0

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.git.5a3da085.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1.git.5a3da085
- 3.4.0

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libosip2
  * postun_ldconfig for libosip2

* Mon Apr 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Fri Dec 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt3
- fixed build with new auto*

* Sat Oct 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt2
- drop MD5 functions (close #13086)

* Wed Aug 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Wed Jan 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1-alt1
- 3.0.1:
  + Fix memory leaks (not likely to happen).
  + Fix buffer overrun in url.

* Sat Sep 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Jun 29 2004 Gor <vg@altlinux.ru> 2.0.8-alt1
- try to package for Sisyphus

