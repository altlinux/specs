Name: facile
Version: 1.1.3
Release: alt1%ubt

Group: System/Libraries
Summary: Constraint programming library
License: GPL
URL: http://www.recherche.enac.fr/log/facile/

Source0: http://www.recherche.enac.fr/log/facile/distrib/%name-%version.tar.gz
Patch1: facile-1.1-install.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: rpm-build-ocaml4 ocaml4

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
* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt1%ubt
- new version

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 1.1-alt5
- Rebuild with ocaml4 4.03.0.

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 1.1-alt4
- Rebuild with new rpm-build-ocaml4.

* Wed Jun 24 2015 Andrey Bergman <vkni@altlinux.org> 1.1-alt3
- Adopted for Ocaml 4.x

* Wed Dec 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- rebuilt

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- initial specfile
