%set_verify_elf_method textrel=relaxed

Name: ocaml-fileutils
Version: 0.5.1
Release: alt3%ubt
Summary: OCaml library for common file and filename operations
Group: Development/ML

License: LGPLv2 with exceptions
Url: https://forge.ocamlcore.org/projects/ocaml-fileutils/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild
BuildRequires(pre):rpm-build-ubt

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml setup.ml -configure --prefix %prefix --destdir %buildroot
make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

# Set htmldir to current directory, then copy the docs (in api/)
# as a %%doc rule.
make htmldir=. install

%check
make test

%files
%doc COPYING.txt
%_libdir/ocaml/fileutils
%exclude %_libdir/ocaml/fileutils/*.a
%exclude %_libdir/ocaml/fileutils/*.cmx
%exclude %_libdir/ocaml/fileutils/*.cmxa
%exclude %_libdir/ocaml/fileutils/*.ml
%exclude %_libdir/ocaml/fileutils/*.mli

%files devel
%doc COPYING.txt AUTHORS.txt CHANGELOG.txt README.txt TODO.txt
%_libdir/ocaml/fileutils/*.a
%_libdir/ocaml/fileutils/*.cmx
%_libdir/ocaml/fileutils/*.cmxa
%_libdir/ocaml/fileutils/*.ml
%_libdir/ocaml/fileutils/*.mli

%changelog
* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt3%ubt
- moved out from site-lib dir
- added ubt tag

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt3
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt2
- rebuild with ocaml-4.04

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- Initial build for ALT (based on 0.5.1-2.fc26.src)

