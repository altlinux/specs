Name: camlmix
Version: 1.3.1
Release: alt1
Summary: Generic preprocessor for OCaml program with embedded text.

Group: Development/ML
License: BSD
Url: https://github.com/mjambon/camlmix
Source: %name-%version.tar
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
mkdir -p %buildroot%_bindir
%makeinstall PREFIX=%buildroot%_prefix

%files
%doc LICENSE
%_bindir/*

%changelog
* Sun Jan 03 2021 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1
- fixed License
- cleanup specfile

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 23 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux
