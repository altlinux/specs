Name: ocaml-text
License: BSD
Group: Development/ML
Summary: Development files for %name-runtime
Version: 0.5
Release: alt1
Url: http://forge.ocamlcore.org/projects/ocaml-text/
Source: http://forge.ocamlcore.org/frs/download.php/641/ocaml-text-0.5.tar.gz
Patch: ocaml-text-alt-fix-rpath.patch
Requires: %name-runtime = %version-%release

BuildRequires: ocaml ocamldoc ocamlbuild findlib camlp4
BuildRequires: glibc-devel pcre-ocaml libncurses-devel

%description
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way

It supports:

  - character encoding/decoding using iconv
  - manipulation of text as UTF-8 encoded strings
  - localised text functions such as compare, upper, ...
  - human readable regular expression inside patterns

In order to be the compatible with other ocaml library without pain,
OCaml-Text choose to use only regular strings for dealing with text.

This package contains the development files needed to build applications
using %name.

%package runtime
Summary: Ocaml-text is a library for manipulation of unicode text
Group: Development/ML

%description runtime
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way

It supports:

  - character encoding/decoding using iconv
  - manipulation of text as UTF-8 encoded strings
  - localised text functions such as compare, upper, ...
  - human readable regular expression inside patterns

In order to be the compatible with other ocaml library without pain,
OCaml-Text choose to use only regular strings for dealing with text.

%prep
%setup
%patch -p1

%build
ocaml setup.ml -configure --prefix %_prefix --destdir '%buildroot' --enable-pcre 
make
# make doc

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_libdir/ocaml/site-lib/%name
%makeinstall_std OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml

%files runtime
%doc LICENSE
%_libdir/ocaml/text
%_libdir/ocaml/stublibs/*.so*
%exclude %_libdir/ocaml/text/*.a
%exclude %_libdir/ocaml/text/*.cmxa
#%exclude %{_libdir}/ocaml/text/*.cmx
%exclude %_libdir/ocaml/text/*.mli

%files
%doc LICENSE CHANGES CHANGES.darcs README
%_libdir/ocaml/text/*.a
%_libdir/ocaml/text/*.cmxa
#%_libdir/ocaml/text/*.cmx
%_libdir/ocaml/text/*.mli


%changelog
* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- initial build
