%define _name findlib
Name: ocaml-%_name
Version: 1.9.6
Release: alt2
Summary: A module packaging tool for OCaml
License: MIT
Group: Development/ML
Url: https://projects.camlcity.org/projects/findlib.html
VCS: https://github.com/ocaml/ocamlfind
Source: %_name-%version.tar
BuildRequires: rpm-build-ocaml >= 1.6 ocaml-labltk-devel >= 8.06.2 libtinfo-devel ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild libX11-devel tcl-devel tk-devel libncurses-devel openjade

%description
The "findlib" library provides a scheme to manage reusable software
components (packages), and includes tools that support this
scheme. Packages are collections of OCaml modules for which
metainformation can be stored. The packages are kept in the filesystem
hierarchy, but with strict directory structure. The library contains
functions to look the directory up that stores a package, to query
metainformation about a package, and to retrieve dependency
information about multiple packages. There is also a tool that allows
the user to enter queries on the command-line. In order to simplify
compilation and linkage, there are new frontends of the various OCaml
compilers that can directly deal with packages.


%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %_name-%version

sed -i -e 's,@LIBDIR@,%_libdir,g' src/findlib-toolbox/make_wizard.ml
sed -i -e '/path/s,@SITELIB@,\0:%_libdir/ocaml,' findlib.conf.in

%build
(cd tools/extract_args && make)
tools/extract_args/extract_args -o src/findlib/ocaml_args.ml ocamlc ocamlcp ocamlmktop ocamlopt ocamldep ocamldoc ||:
cat src/findlib/ocaml_args.ml
./configure \
    -no-custom \
    -mandir %_mandir \
    -config %_libdir/ocaml/etc/findlib.conf \
    -sitelib `ocamlc -where` \
    #
make all OCAMLC_FLAGS=-bin-annot
%ifarch %ocaml_native_arch
make opt OCAMLC_FLAGS=-bin-annot
%endif

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5}
make install \
     prefix=$RPM_BUILD_ROOT \
     OCAMLFIND_BIN=%{_bindir} \
     OCAMLFIND_MAN=%{_mandir}
%__install -m644 src/findlib/*.cmt* %buildroot%_ocamldir/findlib/
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE
%_bindir/ocamlfind
%_libdir/ocaml/topfind
%_libdir/ocaml/etc/*
%_man1dir/ocamlfind.1*
%_man5dir/*

%files devel -f ocaml-files.devel
%doc doc/README doc/guide-html
%_libdir/ocaml/findlib/Makefile.config
%_libdir/ocaml/findlib/Makefile.packages

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 1.9.6-alt2
- added support for bytecode-only version of the ocaml package

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 1.9.6-alt1
- 1.9.3 -> 1.9.6

* Mon Jan 31 2022 Anton Farygin <rider@altlinux.ru> 1.9.3-alt1
- 1.9.1 -> 1.9.3

* Tue Mar 23 2021 Anton Farygin <rider@altlinux.org> 1.9.1-alt2
- added dummy META file for seq library

* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 1.9.1-alt1
- 1.9.1

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 1.8.1-alt3
- ocaml-labltk have been renamed to ocaml-labltk-devel

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 1.8.1-alt2
- removed BR: starting with ocaml 4.10 ocaml-graphics is built from
  a separate package

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.8.1-alt1
- 1.8.1
- added dummy META file for seq library

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.8.0-alt6
- rebuilt with ocaml 4.08.0
- built without camlp4

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt5
- add dummy META file for uchar library, distributed with ocaml >= 4.02

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt4
- add ocaml-graphis to build requires
- default site-lib directory changed to %_libdir/ocaml

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt3
- rebuilt with ocaml-4.07.1

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt2
- rebuilt with ocaml-4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Dec 18 2017 Anton Farygin <rider@altlinux.ru> 1.7.3-alt3
- rebuilt for ocaml-4.06.0

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.7.3-alt2
- rebuild with ocaml-4.04.2

* Sun Jun 18 2017 Anton Farygin <rider@altlinux.ru> 1.7.3-alt1
- new version

* Fri May 05 2017 Anton Farygin <rider@altlinux.ru> 1.7.1-alt4
- fixed "native" patch for more universal linking way with tcl libs 

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.7.1-alt3
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2
- split to devel and runtime packages

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- renamed back to ocaml-findlib
- added %%ubt tag
- 1.7.1

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.6.2-alt2
- NMU: rebuilt against Tcl/Tk 8.6
- fixed patch to build against Tcl/Tk 8.6

* Sat Jun 18 2016 Andrey Bergman <vkni@altlinux.org> 1.6.2-alt1
- 1.6.2

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 1.5.5-alt2
- Rebuild with new rpm-build-ocaml4.

* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.5.5-alt1
- 1.5.5
- initial build for ocaml4
