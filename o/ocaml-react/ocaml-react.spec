Name: ocaml-react
Version: 0.9.2
Release: alt1
Summary: Development files for %name
License: BSD
Group: Development/ML
Url: http://erratique.ch/software/react

Source: http://erratique.ch/software/react/releases/react-%version.tbz
Requires: %name-runtime = %version-%release
Requires: rpm-build-ocaml >= 1.1

BuildPreReq: rpm-build-ocaml >= 1.1
BuildRequires: ocaml ocamlbuild

%description
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%package runtime
Summary: OCaml module for Functional Reactive Programming (FRP)
Group: Development/ML

%description runtime
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%prep
%setup -n react-%version

%build
chmod u+x build
./build

%check
./build test.native
./test.native

%install

INSTALLDIR=%buildroot/%_libdir/ocaml/react ./build install

%files runtime
%doc README
%dir %_libdir/ocaml/react
%_libdir/ocaml/react/META
%_libdir/ocaml/react/react.cmi
%_libdir/ocaml/react/react.cmo

%files
%doc doc
%_libdir/ocaml/react/react.cmx
%_libdir/ocaml/react/react.o
%_libdir/ocaml/react/react.mli
%_libdir/ocaml/react/react.ml

%changelog
* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus
