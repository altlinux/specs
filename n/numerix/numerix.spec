%ifarch %ix86
%define ppctarget i386-linux
%else
%define ppctarget x86_64-linux
%endif
%define ppcname %(basename `fpc -PB`)

Name: numerix
License: GPL
Group: System/Libraries
Summary: Numerix "big integer"
Version: 0.22
Release: alt7.1
Url: http://pauillac.inria.fr/~quercia/
Source: http://pauillac.inria.fr/~quercia/cdrom/bibs/%name.tar.gz
Patch: %name-install.patch
Packager: Boris Savelev <boris@altlinux.org>
Requires: lib%name-ocaml = %version-%release

BuildRequires: rpm-build-fpc fpc fpc-utils ocaml libgmp-devel

%package -n lib%name-ocaml
Summary: Numerix "big integer" library for OCaml
Group: System/Libraries

%package -n lib%name
Summary: Numerix "big integer" library for C
Group: System/Libraries

%package -n lib%name-devel
Summary: Numerix "big integer" library for C (Devel)
Group: Development/C

%package -n lib%name-fpc-unit
Summary: Numerix "big integer" library for FPC
Group: Development/Other

%package doc
Summary: Documentation for %name
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description
OCaml program uses Numerix library.

%description -n lib%name-ocaml
The Numerix library provides unlimited precision integer arithmetic
facilities for use in OCaml programs. This package contains only
the ocamlnumx runtime and the shared runtime stub libraries.
Numerix is a library implementing arbitrary long signed integers
and the usual arithmetic operations between those numbers.

%description -n lib%name
C library of the Numerix

%description -n lib%name-devel
This package contains devel files for lib%name

%description -n lib%name-fpc-unit
FPC unit of the Numerix

%description doc
This package contains most of documentation for %name

%prep
%setup -q
%patch0 -p0

%build
%configure \
--disable-sse2 \
--enable-ocaml_bignum \
--enable-gmp \
--enable-shared
%make lib

%install
%makeinstall_std
# ocaml
mkdir -p %buildroot%_libdir/ocaml/stublibs/
mv %buildroot%_libdir/{dll*.so,lib%name-ocaml.*} %buildroot%_libdir/ocaml/stublibs
mv %buildroot%_libdir/{*.cm?*,%name.a} %buildroot%_libdir/ocaml
mv %buildroot%_includedir/*.ml* %buildroot%_libdir/ocaml

# fpc
mkdir -p %buildroot%fpc_dir/units/%ppctarget/%name
mv %buildroot%_libdir/{*.o,*.ppu} %buildroot%fpc_dir/units/%ppctarget/%name
# fpc meta
cat >> %buildroot%fpc_dir/units/%ppctarget/%name/Package.fpc << EOF
[package]
name="%name"
version="%version"
EOF

# docs
for f in `ls doc` ; do
    mv doc/$f/%name.pdf doc/$f/%name-$f.pdf
done
mkdir -p %buildroot%_datadir/examples/%name
cp -a exemples/* %buildroot%_datadir/examples/%name/

%files
%_bindir/*

%files -n lib%name-ocaml
%_libdir/ocaml/*
%_libdir/ocaml/stublibs/*.*

%files -n lib%name
%_libdir/lib%name-c.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name-c.so

%files -n lib%name-fpc-unit
%dir %fpc_dir/units/%ppctarget/%name
%fpc_dir/units/%ppctarget/%name/*

%files doc
%doc LISEZ.MOI doc/*/*.pdf
%dir %_datadir/examples/%name
%_datadir/examples/%name/*

%changelog
* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt7.1
- Rebuild with new ocaml

* Sun Jan 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt7
- Rebuild with new fpc

* Fri Aug 26 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt6
- Rebuild with new fpc

* Mon Feb 21 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt5
- Rebuild with new fpc

* Wed Apr 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt4
- Rebuild with new fpc

* Tue Jan 05 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt3
- Rebuild with new fpc

* Fri Apr 24 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.22-alt2
- Rebuild with new fpc

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 0.22-alt1
- initial build

