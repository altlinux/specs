Name: ocaml-lwt
Version: 1.1.0
Release: alt3
Summary: OCaml lightweight thread library

Group: Development/ML
License: LGPLv2+ with exceptions
Url: http://ocsigen.org/install/lwt
Packager: Veaceslav Grecea <slavutich@altlinux.org>

Source: http://ocsigen.org/download/lwt-%version.tar.gz

# Automatically added by buildreq on Mon Sep 08 2008
BuildRequires: findlib ocamlbuild ocamldoc termutils ocaml-ssl

Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%package doc

Summary:        Documetation files for %name
Group:          Development/ML
Requires:       %name = %version-%release


%description    doc
The %{name}-doc package contains documentation files for %name.

%prep
%setup -q -n lwt-%version

mv README README.old
iconv -f iso-8859-1 -t utf-8 < README.old > README

%build
make

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p %buildroot%_libdir/ocaml/site-lib/lwt
make install

%files
%doc LICENSE COPYING CHANGES README VERSION
%_libdir/ocaml/site-lib/lwt/*

%files doc
%doc _build/lwt.docdir/*

%changelog
* Wed Dec 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt3
- rebuild with new ocaml

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt2
- darcs update

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- Initial RPM release.
