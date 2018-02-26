Name: tre
Version: 0.8.0
Release: alt2.1

Summary: TRE is "approximate regexp" library
License: BSD
Group: Development/C

Url: http://laurikari.net/tre
Source: %url/%name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

%define agrep agrep-%name
%define soversion 5

# Automatically added by buildreq on Mon May 10 2004
BuildRequires: hostinfo libdb4-devel python-devel

%description
(void package)

%package -n %agrep
Summary: agrep version using TRE library
Group: Text tools
Conflicts: agrep = 2.04-alt1

%description -n %agrep
agrep is a grep-like utility which can do approximate searches.

%package -n lib%name%soversion
Summary: TRE is a regexp matching library with approximate matching capability
Group: System/Libraries

%description -n lib%name%soversion
TRE is a lightweight, robust, and efficient POSIX compliant
regexp matching library with some exciting features such as
approximate matching.

%package -n lib%name-devel
Summary: Development environment for lib%name
Group: Development/C
Requires: lib%name%soversion = %version-%release

%description -n lib%name-devel
TRE is a lightweight, robust, and efficient POSIX compliant
regexp matching library with some exciting features such as
approximate matching.

This is the development environment to compile TRE software.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for lib%name%soversion
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
TRE is a lightweight, robust, and efficient POSIX compliant
regexp matching library with some exciting features such as
approximate matching.

This package contains static library to build statically linked
TRE software.
%endif

%package -n python-module-%name
Summary: Python bindings for TRE, regex library with approximate matching
Group: Development/Python

%description -n python-module-%name
TRE is a lightweight, robust, and efficient POSIX compliant
regexp matching library with some exciting features such as
approximate matching.

This package contains Python bindings for TRE.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build
cd python
python setup.py build

%install
%makeinstall
%find_lang %name
cd python
python setup.py install --root=%buildroot

%files -n %agrep -f %name.lang
%_bindir/*
%_man1dir/*

%files -n lib%name%soversion
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n python-module-%name
%python_sitelibdir/*.egg-info
%python_sitelibdir/%name.so

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- drop RPATH
- minor spec cleanup

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt1.1
- Rebuild with Python-2.7

* Sat Jul 10 2010 Alexander Myltsev <avm@altlinux.ru> 0.8.0-alt1
- new version (soname change, new API, license change to BSD).

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.7.5-alt3
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.7.5-alt2
- applied repocop patch

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 0.7.5-alt1
- 0.7.5 (minor feature enhancements)

* Mon May 22 2006 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1
- 0.7.4 (64-bit fixes)

* Sun Apr 02 2006 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- 0.7.3
  + upstream license changed from GPL to LGPL
  + minor enhancements/bugfixes

* Sun Nov 27 2005 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- 0.7.2
- updated package Url

* Mon May 10 2004 Michael Shigorin <mike@altlinux.ru> 0.6.7-alt1
- 0.6.7
- refreshed build reqs

* Sun Feb 01 2004 Michael Shigorin <mike@altlinux.ru> 0.6.4-alt1
- 0.6.4 (minor bugfixes)

* Fri Dec 26 2003 Michael Shigorin <mike@altlinux.ru> 0.6.3-alt1
- 0.6.3
- removed *.la
- don't build static library by default

* Mon Jul 14 2003 Michael Shigorin <mike@altlinux.ru> 0.5.3-alt1
- built for ALT Linux (thanks to Alexander Bokovoy for suggestion)

