Name: facile
Version: 1.1
Release: alt2

Group: System/Libraries
Summary: Constraint programming library
License: GPL
URL: http://www.recherche.enac.fr/log/facile/

Requires: ocaml

Source0: http://www.recherche.enac.fr/log/facile/distrib/%name-%version.tar.gz
Patch1: facile-1.1-install.patch
BuildRequires: ocaml

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml.

%prep
%setup -q 
%patch1 -p1

%build
./configure
make

%install
make DESTDIR=%buildroot install

%files
%_libdir/ocaml/facile

%changelog
* Wed Dec 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- rebuilt

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- initial specfile
