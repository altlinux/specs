%def_with check
%define modname ocamlgraph
Name: ocaml-%modname
Version: 2.1.0
Release: alt1
Summary: OCaml library for arc and node graphs
Group: Development/ML
License: LGPLv2 with exceptions
Url: https://github.com/backtracking/ocamlgraph/
Source0: %name-%version.tar
BuildRequires: libart_lgpl-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: dune
BuildRequires: ocaml-ocamldoc
%if_with check
BuildRequires: ocaml-graphics-devel
%endif
BuildRequires(pre): rpm-build-ocaml >= 1.3

%description
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal
reusability. Also has input and output capability for Graph Modeling
Language file format and Dot and Neato graphviz (graph visualization)
tools.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
sed -i 's,stdlib-shims,,' */dune
%dune_build -p %modname

%install
%dune_install %modname

%check
%dune_check -p %modname

%files -f ocaml-files.runtime
%doc CREDITS FAQ COPYING LICENSE

%files devel -f ocaml-files.devel
%doc CHANGES.md README.md

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0
- enabled tests

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- new version
- disabled tests for bootstrap ocaml-4.13

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 1.8.8-alt5
- adaptation for rpm-build-ocaml-1.4

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.8.8-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.8.8-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.8.8-alt2
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.8.8-alt1
- 1.8.8

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.8.7-alt2
- rebuild with ocaml 4.04.2

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 1.8.7-alt1
- first build for ALT
