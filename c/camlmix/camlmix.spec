Name: camlmix
Version: 1.3.0
Release: alt1
Summary: Generic preprocessor for OCaml program with embedded text.

Group: Development/ML
License: GPL
Url: http://martin.jambon.free.fr/camlmix/
Packager: Veaceslav Grecea <slavutich@altlinux.org>

Source: http://martin.jambon.free.fr/camlmix/%name-%version.tar.bz2

# Automatically added by buildreq on Tue Sep 23 2008
BuildRequires: ocaml

%description
Camlmix is a generic preprocessor which converts text with embedded 
OCaml into an OCaml program with embedded text. It produces text 
documents from one or several templates. Camlmix is not a Camlp4 syntax 
extension.

%prep
%setup -q

%build
make

%install
mkdir -p %buildroot/usr/bin
make install PREFIX=%buildroot/usr

#install -m755  camlmix %buildroot/usr
%files
%doc LICENSE
%_bindir/*

%changelog
* Mon Sep 23 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux
