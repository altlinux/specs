Name: ktoblzcheck
Version: 1.37
Release: alt1

Summary: A library to check account numbers and bank codes of German banks

Packager: Andrey Cherepanov <cas@altlinux.org>

License: LGPL v2+
Group: System/Libraries
Url: http://ktoblzcheck.sourceforge.net/

Source: http://prdownloads.sf.net/ktoblzcheck/%name-%version.tar.gz
Source1: %name.watch

BuildRequires: gcc-c++ libstdc++-devel lynx python-devel python-modules-encodings recode

%description
KtoBLZCheck is a library to check account numbers and bank codes of
German banks.

Both a library for other programs as well as a short command-line tool
is available. It is possible to check pairs of account numbers and
bank codes (BLZ) of German banks, and to map bank codes (BLZ) to the
clear-text name and location of the bank.

%package devel
Summary: Header files for KtoBLZCheck library
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for KtoBLZCheck library.

%package -n python-module-ktoblzcheck
Summary: Python binding for KtoBLZCheck library
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description -n python-module-ktoblzcheck
Python binding for KtoBLZCheck library.

%prep
%setup -q

%build
%autoreconf
%configure \
	--enable-python \
	--disable-static
%make_build

%install
%makeinstall_std

%_python_set_noarch

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/ktoblzcheck
%_libdir/libktoblzcheck.so.*
%dir %_datadir/%name/
%_datadir/%name/*.txt
%_datadir/%name/*.pl
%_man1dir/ktoblzcheck.1*

%files devel
%_libdir/libktoblzcheck.so
%_includedir/*.h
%_pkgconfigdir/ktoblzcheck.pc

%files -n python-module-ktoblzcheck
%python_sitelibdir/*

%changelog
* Fri Jan 20 2012 Andrey Cherepanov <cas@altlinux.org> 1.37-alt1
- New version 1.37
- Add watch file
- Remove standard library path from RPATH

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 1.34-alt1
- New version 1.34

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 16 2010 Andrey Cherepanov <cas@altlinux.org> 1.27-alt1
- New version (1.27)

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.18-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for ktoblzcheck
  * postun_ldconfig for ktoblzcheck
  * postclean-05-filetriggers for spec file

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)
- cleanup spec

* Sun May 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt0.1
- new version 1.11 (with rpmrb script)

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt0.1
- new version 1.10 (with rpmrb script)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

