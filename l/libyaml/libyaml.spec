%define oname yaml
%define abiversion 2
Name: libyaml
Version: 0.1.4
Release: alt1

Summary: A C library for parsing and emitting YAML

License: MIT/X11
Group: System/Libraries
Url: http://pyyaml.org/wiki/LibYAML

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pyyaml.org/download/libyaml/%oname-%version.tar

# Automatically added by buildreq on Sat Oct 02 2010
BuildRequires: doxygen

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
%setup -n %oname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n %name%abiversion
%doc README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*.h
%_pkgconfigdir/*

%changelog
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

