Name: pure
Summary: PURE - The Pure programming language
License: GPL
Version: 0.45
Release: alt1
Group: Development/Functional
Url: http://pure-lang.googlecode.com/
Source0: http://pure-lang.googlecode.com/files/%name-%version.tar.gz
Source90: %name-rpmlintrc

#Requires: pure-doc
#Requires:		web_browser
#Requires: w3m

# Automatically added by buildreq on Sat Mar 28 2009
BuildRequires: gcc-c++ libelf-devel libgmp-devel libgsl-devel libreadline-devel llvm-devel

%description
Pure is a functional programming language based on term rewriting.
It has a modern syntax featuring curried function applications,
lexical closures and equational definitions with pattern matching,
and thus is somewhat similar to languages of the Haskell and ML
variety. But Pure is also a very dynamic and reflective language,
and is more like Lisp in this respect. The interpreter has an LLVM
backend to do JIT compilation, hence programs run blazingly fast
and interfacing to C modules is easy.

Author: Albert Graef <Dr.Graef@t-online.de>

%package -n libpure
Summary: Shared libraries for PURE
Group: System/Libraries

%description -n libpure
Shared libraries for PURE.

Author: Albert Graef <Dr.Graef@t-online.de>

%package -n libpure-devel
Summary: Include Files and Libraries mandatory for Development
Group: Development/C++
Requires: libpure = %version

%description -n libpure-devel
This package contains all necessary include files and libraries
needed to develop applications that require these.

Author: Albert Graef <Dr.Graef@t-online.de>

#%package complete
#Summary: Virtual package to install pure and all its components
#Group: Development/Tools/Other
#Requires: pure-csv
#Requires: pure-doc
#Requires: pure-ffi
#Requires: pure-gl
#Requires: pure-gsl
#Requires: pure-odbc
#Requires: pure-xml
#
#%description complete
#Virtual package to install pure and all its components:
#pure-ffi, pure-csv and pure-gsl.

%package examples
Summary: Some examples for pure
Group: Development/Functional
Requires: pure

%description examples
Some examples for package pure.

%prep
%setup -q -n %name-%version

%build
export LIBS=-ldl
%configure --enable-release --disable-rpath --enable-versioned

%make_build \
	CXXFLAGS="$RPM_OPT_FLAGS -fPIC" \
	CPPFLAGS="$RPM_OPT_FLAGS -fPIC" \
	LDFLAGS="$RPM_OPT_FLAGS -fPIC" \
	shared="-shared -fPIC"

%install
make install DESTDIR=%buildroot

%check
make check

%files
%doc COPYING ChangeLog NEWS README
# TODO: etc/* are separate packages for vim, emacs, gedit, kate and libhighlight
%doc etc
%_man1dir/*
%_bindir/%{name}*
%_libdir/%name
%dir %_libdir/%name-%version
%_libdir/%name-%version/*.????

%files -n libpure
%_libdir/*.so.*

%files -n libpure-devel
%_includedir/%name
%_libdir/*.so
%_libdir/%name-%version/*.?
%dir %_includedir/%name-%version
%_includedir/%name-%version/runtime.h

#%files complete
#%doc COPYING ChangeLog NEWS README

%files examples
%doc examples

%changelog
* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 0.45-alt1
- Version up

* Fri Apr 30 2010 Fr. Br. George <george@altlinux.ru> 0.43-alt1
- Version up

* Sat Aug 01 2009 Fr. Br. George <george@altlinux.ru> 0.25-alt1
- Version up

* Sun Jun 07 2009 Fr. Br. George <george@altlinux.ru> 0.24-alt1
- Version up

* Thu Apr 16 2009 Fr. Br. George <george@altlinux.ru> 0.22-alt1
- Version up

* Mon Mar 16 2009 Fr. Br. George <george@altlinux.ru> 0.19-alt1
- Initial build from SuSE

* Sun Mar 15 2009 Toni Graffy <toni@links2linux.de> - 0.19-0.pm.2
- update to 0.19
- extended pure-complete to pull in all pure-* packages
* Mon Feb 23 2009 Toni Graffy <toni@links2linux.de> - 0.18-0.pm2
- added a patch from upstream to avoid memleaks with pure-odbc
* Sun Feb 22 2009 Toni Graffy <toni@links2linux.de> - 0.18-0.pm.1
- update to 0.18
- new SO-name ==> libpure0_18
- added pure-gl to package pure-complete
- splitted of examples as sub-package
* Fri Jan 30 2009 Toni Graffy <toni@links2linux.de> - 0.17-0.pm.1
- update to 0.17
- new SO-name ==> libpure0_17
- added virtual sub-package pure-complete to install all pure modules
* Tue Jan 13 2009 Toni Graffy <toni@links2linux.de> - 0.16-0.pm.1
- update to 0.16
- new SO-name ==> libpure0_16
* Wed Dec 17 2008 Toni Graffy <toni@links2linux.de> - 0.15-0.pm.1
- update to 0.15
- new SO-name ==> libpure0_15
* Fri Nov 21 2008 Toni Graffy <toni@links2linux.de> - 0.14-0.pm.1
- update to 0.14
- new SO-name ==> libpure0_14
* Wed Nov 05 2008 Toni Graffy <toni@links2linux.de> - 0.13-0.pm.1
- update to 0.13
- new SO-name ==> libpure0_13
* Fri Oct 10 2008 Toni Graffy <toni@links2linux.de> - 0.12-0.pm.1
- update to 0.12
- new SO-name ==> libpure0_12
* Mon Oct 06 2008 Toni Graffy <toni@links2linux.de> - 0.11-0.pm.1
- update to 0.11
- new SO-name ==> libpure0_11
* Sun Oct 05 2008 Toni Graffy <toni@links2linux.de> - 0.10-0.pm.1
- update to 0.10
- new SO-name ==> libpure0_10
* Wed Oct 01 2008 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
- new SO-name ==> libpure0_9
- new URL
* Sun Sep 28 2008 Toni Graffy <toni@links2linux.de> - 0.8-0.pm.1
- update to 0.8
- new SO-name ==> libpure0_8
* Sat Sep 27 2008 Toni Graffy <toni@links2linux.de> - 0.7-0.pm.1
- update to 0.7
- new SO-name ==> libpure0_7
* Fri Sep 12 2008 Toni Graffy <toni@links2linux.de> - 0.6-0.pm.1
- update to 0.6
- new SO-name ==> libpure0_6
* Thu Aug 28 2008 Toni Graffy <toni@links2linux.de> - 0.5-0.pm.1
- update to 0.5
- new SO-name ==> libpure0_5
* Sat Jun 21 2008 Toni Graffy <toni@links2linux.de> - 0.4-0.pm.3
- added etc-subdir (templates for Emacs, Vim, Kate or HTML)
- changed description
* Fri Jun 20 2008 Toni Graffy <toni@links2linux.de> - 0.4-0.pm.2
- update to 0.4
* Fri Jun 13 2008 Toni Graffy <toni@links2linux.de> - 0.4-225.pm.svn20080614
- initial build version 0.4 -r225
