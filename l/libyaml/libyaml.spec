%define abiversion 2
%def_with doc

Name: libyaml
Version: 0.1.7
Release: alt1.1

Summary: A C library for parsing and emitting YAML

License: MIT/X11
Group: System/Libraries
Url: http://pyyaml.org/wiki/LibYAML

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://pyyaml.org/download/libyaml/yaml-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 02 2010
%if_with doc
BuildRequires: doxygen
%endif

%description
YAML 1.1 parser and emitter written in C.

%package -n %name%abiversion
Summary: A C library for parsing and emitting YAML
Group: System/Libraries

%description -n %name%abiversion
YAML 1.1 parser and emitter written in C.

%package devel
Summary: Header files for the yaml library
Group: Development/C
Requires: %name%abiversion = %version-%release

%description devel
Header files for the yaml library.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%if_with doc
top_srcdir=`pwd` top_builddir=`pwd` doxygen doc/doxygen.cfg
%endif

%install
%makeinstall_std

%files -n %name%abiversion
%doc README
%_libdir/lib*.so.*

%files devel
%if_with doc
%doc doc/html
%endif
%_libdir/lib*.so
%_includedir/*.h
%_pkgconfigdir/*

%changelog
* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 0.1.7-alt1.1
- BOOTSTRAP: added doc knob (doxygen)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- new version 0.1.7 (with rpmrb script)

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.1.6-alt1
- Autobuild version bump to 0.1.6

* Thu Feb 06 2014 Fr. Br. George <george@altlinux.ru> 0.1.5-alt1
- Autobuild version bump to 0.1.5 (closes: #29802)
- Generate and package development documentation

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Version 0.1.4

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- new version (0.1.3) import in git (ALT bug #24182)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libyaml
  * postun_ldconfig for libyaml
  * postclean-05-filetriggers for spec file

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

