%define oname cryptokit
Name: ocaml-%oname
License: GPL
Group: Development/Other
Summary: Development files for %name-runtime
Version: 1.5
Release: alt1
Url: http://forge.ocamlcore.org/projects/cryptokit/
Source: http://forge.ocamlcore.org/frs/download.php/639/cryptokit-1.5.tar.gz
Patch0: %oname-install.patch
Packager: Boris Savelev <boris@altlinux.org>
Requires: %name-runtime = %version-%release

BuildRequires: ocaml zlib-devel ocamldoc ocamlbuild findlib
BuildRequires: libtinfo-devel

%description
This package contains the development files needed to build applications
using %name.

%package runtime
Summary: Cryptographic primitives for OCaml
Group: System/Libraries
Obsoletes: libcryptokit-ocaml
Provides: libcryptokit-ocaml = %version

%description runtime
The Cryptokit library for Objective Caml provides a
variety of cryptographic primitives that can be used
to implement cryptographic protocols in security-sensitive applications.

%prep
%setup -q -n %oname-%version
#%patch0 -p0
#sed -i -e 's:/usr/lib:%_libdir:g' Makefile

%build
./configure --destdir %buildroot
%make

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
%makeinstall_std OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_libdir/ocaml/site-lib
cd %buildroot%_libdir/ocaml/site-lib
ln -s ../cryptokit cryptokit

%files runtime
%doc LICENSE.txt
%_libdir/ocaml/site-lib/cryptokit
%_libdir/ocaml/cryptokit
%_libdir/ocaml/stublibs/*.so*
%exclude %_libdir/ocaml/cryptokit/*.a
%exclude %_libdir/ocaml/cryptokit/*.cmxa
#%exclude %{_libdir}/ocaml/cryptokit/*.cmx
%exclude %_libdir/ocaml/cryptokit/*.mli

%files
%doc README.txt LICENSE.txt Changes
%_libdir/ocaml/cryptokit/*.a
%_libdir/ocaml/cryptokit/*.cmxa
#%_libdir/ocaml/cryptokit/*.cmx
%_libdir/ocaml/cryptokit/*.mli

%changelog
* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Thu Oct 02 2008 Boris Savelev <boris@altlinux.org> 1.3-alt5
- remove "directory" from META

* Tue Sep 30 2008 Boris Savelev <boris@altlinux.org> 1.3-alt4
- add requires to META (fix #170011)

* Thu Sep 04 2008 Boris Savelev <boris@altlinux.org> 1.3-alt3
- rename to ocaml-cryptokit
- move files to site-lib/cryptokit
- add META
- split runtime and devel package

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 1.3-alt2
- add make allopt (to build cryptokit.cmxa)

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 1.3-alt1
- initial build

