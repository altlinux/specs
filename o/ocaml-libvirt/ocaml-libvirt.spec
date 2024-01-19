%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-libvirt
Version: 0.6.1.7
Release: alt1
Summary: OCaml binding for libvirt
Group: System/Libraries

License: LGPLv2+
Url: http://libvirt.org/ocaml/

Source: http://libvirt.org/sources/ocaml/%name-%version.tar
Patch1: Fix-ocamlopt-detection.patch
BuildRequires(pre): rpm-build-ocaml >= 1.6
BuildRequires: ocaml >= 3.10.0 ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-findlib

BuildRequires: libvirt-devel >= 0.2.1
BuildRequires: perl-devel
BuildRequires: gawk

%description
OCaml binding for libvirt.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make
%make doc

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%makeinstall_std
%ocaml_find_files

%files -f ocaml-files.runtime
%doc COPYING.LIB README
%_libdir/ocaml/stublibs/*.so.owner

%files devel -f ocaml-files.devel
%doc COPYING.LIB README TODO.libvirt html/*

%changelog
* Fri Jan 12 2024 Alexey Shabalin <shaba@altlinux.org> 0.6.1.7-alt1
- 0.6.1.7

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 0.6.1.5-alt2
- fixed build with LTO

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.6.1.5-alt1
- 0.6.1.5

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt8
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt7
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt6
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt5
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt3
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2
- rebuild with ocaml-4.04

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.1.4-alt1
- Initial build for ALT (based on 0.6.1.4-13.fc26.src)

