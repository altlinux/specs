%define _unpackaged_files_terminate_build 1

Name: ocaml-augeas
Version: 0.6
Release: alt2

Summary: OCaml bindings for Augeas
License: MIT
Group: Development/ML

Url: https://people.redhat.com/~rjones/augeas/
VCS: git://git.annexia.org/ocaml-augeas.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml ocaml-findlib ocaml-runtime
BuildRequires: libaugeas-devel

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description devel
This package includes development files necessary for developing
programs which use %name

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
%summary

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --prefix=%buildroot

%ifarch %ocaml_native_arch
%make_build -j1
%else
%make_build -j1 mlaugeas.cma test_augeas
%endif

%install
export OCAMLFIND_DESTDIR=%buildroot%_ocamldir
export OCAMLFIND_LDCONF=%buildroot%_ocamldir/ld.conf
mkdir -vp $OCAMLFIND_DESTDIR
ocamlfind install -destdir $OCAMLFIND_DESTDIR  \
          -ldconf $OCAMLFIND_LDCONF \
          augeas \
%ifarch %ocaml_native_arch
          META *.mli *.cmx *.cma *.cmxa *.a augeas.cmi *.so
%else
          META *.mli *.cma *.a augeas.cmi *.so
%endif
%ocaml_find_files

%files -f ocaml-files.runtime
%doc COPYING.LIB

%files devel -f ocaml-files.devel

%changelog
* Wed Nov 22 2023 Egor Ignatov <egori@altlinux.org> 0.6-alt2
- Support build without native compilation

* Mon Mar 20 2023 Egor Ignatov <egori@altlinux.org> 0.6-alt1
- First build for ALT
