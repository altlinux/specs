Name: bakefile
Version: 0.2.11
Release: alt1

Summary: Native makefiles generator

License: MIT
Group: Development/Other
Url: http://bakefile.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/vslavik/bakefile/archive/v%version.tar.gz
Source: %name-%version.tar
Patch: %name-empy.patch

# Automatically added by buildreq on Sat Mar 07 2009
BuildRequires: gcc-c++ swig python-devel python-module-em
BuildRequires: xsltproc docbook-style-xsl

%description
Bakefile is cross-platform, cross-compiler native makefiles generator.
It takes compiler-independent description of build tasks as input and
generate native makefile (autoconf's Makefile.in, Visual C++ project,
bcc makefile etc.).

%prep
%setup
#%patch0 -p1
#rm -rf src/empy
touch ChangeLog

%build
#autoreconf
./bootstrap
%configure --enable-maintainer-mode

%install
%makeinstall_std

# use system available modules
#rm -rf %buildroot%_libdir/%name/{empy,optik}

%files
%doc README THANKS doc/html
%_bindir/*
%_aclocaldir/*.m4
%_datadir/%name/
%dir %_libdir/%name/
%_libdir/%name/*.py*
%_libdir/%name/*.so
%_libdir/%name/*.la
%_libdir/%name/empy/
%_libdir/%name/py25modules/
%_man1dir/bakefil*.1*

%changelog
* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.11-alt1
- new version 0.2.11 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt1
- new version (0.2.10) with rpmgs script

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.9-alt1
- new version 0.2.9 (with rpmrb script)

* Fri Dec 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1
- Version 0.2.8

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.6-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.1
- Rebuilt with python 2.6

* Sat Apr 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt1
- new version 0.2.6 (with rpmrb script)

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- new version 0.2.5 (with rpmrb script)

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- initial build for ALT Linux Sisyphus (thanks, PLD)

