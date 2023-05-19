%define _unpackaged_files_terminate_build 1

Name: ocaml-augeas
Version: 0.6
Release: alt1

Summary: OCaml bindings for Augeas
License: MIT
Group: Development/ML

Url: https://people.redhat.com/~rjones/augeas/
VCS: git://git.annexia.org/ocaml-augeas.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-ocaml
BuildRequires: ocaml ocaml-findlib ocaml-runtime
BuildRequires: libaugeas-devel

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
%summary

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --prefix=%buildroot
%make_build -j1

%install
export OCAMLFIND_DESTDIR=%buildroot%_ocamldir
export OCAMLFIND_LDCONF=%buildroot%_ocamldir/ld.conf
mkdir -vp $OCAMLFIND_DESTDIR
ocamlfind install -destdir $OCAMLFIND_DESTDIR  \
          -ldconf $OCAMLFIND_LDCONF \
          augeas \
          META *.mli *.cmx *.cma *.cmxa *.a augeas.cmi *.so

%files
%doc COPYING.LIB
%_ocamldir/augeas

%changelog
* Mon Mar 20 2023 Egor Ignatov <egori@altlinux.org> 0.6-alt1
- First build for ALT

