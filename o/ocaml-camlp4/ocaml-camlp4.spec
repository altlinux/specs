Name: ocaml-camlp4
Version: 4.04.1
Release: alt1%ubt

Summary: Preprocessor for OCaml
License: QPL & LGPL
Group: Development/ML

Requires: ocaml

Url: https://github.com/ocaml/camlp4
Packager: %packager

Source0: %name-%version.tar

Requires: rpm-build-ocaml >= 1.1.1
BuildRequires(pre): rpm-build-ocaml >= 1.1.1
BuildRequires(pre): rpm-build-ubt

# Automatically added by buildreq on Sun Oct 19 2014
BuildRequires: ocaml-runtime ocaml >= 4.04 ocaml-ocamlbuild
Requires: ocaml-runtime ocaml
Provides: ocaml4-campl4
Obsoletes: ocaml4-campl4
Conflicts: camlp4

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

%prep
%setup -q -T -b 0

%build

%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64
./configure --bindir=%_bindir --libdir=%_libdir/ocaml

%make all

%install

make install BINDIR=%buildroot%_bindir LIBDIR=%buildroot%_libdir/ocaml MANDIR=%buildroot%_mandir

%files
%_bindir/camlp4*
%_bindir/mkcamlp4
#%%_man1dir/camlp4.1*
%_libdir/ocaml/camlp4/

%changelog
* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 4.04.1-alt1%ubt
- new version

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.1-alt1
- Version update (switch to ocaml 4.03).

* Mon Apr 04 2016 Andrey Bergman <vkni@altlinux.org> 4.02.7-alt1
- Version update.

* Sun Jul 12 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt2
- Added conflict with camlp4.

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt1
- Rebuild with new rpm-build-ocaml4.

* Fri Jun 19 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt0.1
- Version update.

* Mon Feb 02 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1+2-alt0.1
- Version update. Added rpm-build-ocaml4 to buildreq.

* Sat Oct 18 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0.1-alt0.1
- Initial release for Sisyphus after removal from Ocaml distribution
(see ocaml 4.02.0 changelog).

