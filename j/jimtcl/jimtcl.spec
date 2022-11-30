Name: jimtcl
Version: 0.81
Release: alt2

Summary: A small embeddable Tcl interpreter
License: BSD
Group: Development/Tcl
Url: http://jim.tcl.tk

# https://github.com/msteveb/jimtcl.git
Source0: %name-%version.tar

BuildRequires: asciidoc

%description
Jim is an opensource small-footprint implementation of the Tcl
programming language. It implements a large subset of Tcl and adds new
features like references with garbage collection, closures, built-in
Object Oriented Programming system, Functional Programming commands,
first-class arrays and UTF-8 support.

%package devel
Summary: Development files for %name
Group: Development/Tcl
Requires: %name%{?_isa} = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
#configure is not able to locate the needed binaries, so specify it manualy
export CC=gcc
export LD=ld
export AR=ar
export RANLIB=ranlib
export STRIP=strip

%configure \
	--full \
	--shared \
	--disable-option-checking \
	#
%make_build

%check
make test

%install
%makeinstall_std
rm -rf %buildroot/%_datadir/doc/jim
pushd %buildroot/%_libdir/
ln -s libjim.so.* libjim.so
popd

%files
%doc LICENSE AUTHORS README Tcl.html
%_bindir/jimdb
%_bindir/jimsh
%_libdir/libjim.so.*

%files devel
%doc DEVELOPING README.extensions README.metakit README.namespaces README.oo README.utf-8 STYLE
%_includedir/*
%_bindir/build-jim-ext
%_libdir/libjim.so
%_pkgconfigdir/jimtcl.pc

%changelog
* Wed Nov 30 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.81-alt2
- filter out outdated test

* Mon Jun 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.81-alt1
- 0.81 released

* Fri Mar 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.80-alt1
- 0.80 released

* Thu Nov 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.76-alt1
- Updated to 0.76.

* Mon May 05 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.75-alt1.git72bbd6c
- Initial build.
