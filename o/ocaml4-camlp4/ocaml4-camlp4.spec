Name: ocaml4-camlp4
Version: 4.02.0.1
Release: alt0.1

Summary: Preprocessor for OCaml 4.02
License: QPL & LGPL
Group: Development/ML

Requires: ocaml4

Url: https://github.com/ocaml/camlp4
Packager: %packager

Source0: %name-%version.tar

# Automatically added by buildreq on Sun Oct 19 2014
# optimized out: ocaml4 ocaml4-runtime
BuildRequires: ocaml4-ocamlbuild

Requires: ocaml4-runtime ocaml4

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

%prep
%setup -q -T -b 0

%build

#sed -i 's@/usr/X11R6/lib\>@%_x11libdir@g' configure

%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64
./configure --bindir=%_bindir --libdir=%_libdir/ocaml

%make all

%install

#install -pD -m644 camlp4/man/camlp4.1.tpl %buildroot%_man1dir/camlp4.1
make install BINDIR=%buildroot%_bindir LIBDIR=%buildroot%_libdir/ocaml MANDIR=%buildroot%_mandir

%files
%_bindir/camlp4*
%_bindir/mkcamlp4
#%%_man1dir/camlp4.1*
%_libdir/ocaml/camlp4/

%changelog
* Sat Oct 18 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0.1-alt0.1
- Initial release for Sisyphus after removal from Ocaml distribution
(see ocaml 4.02.0 changelog).

