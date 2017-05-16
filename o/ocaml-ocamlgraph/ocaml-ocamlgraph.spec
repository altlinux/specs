%set_verify_elf_method textrel=relaxed

Name: ocaml-ocamlgraph
Version: 1.8.7
Release: alt1%ubt
Summary: OCaml library for arc and node graphs
Group: Development/ML
License: LGPLv2 with exceptions
Url: http://ocamlgraph.lri.fr/index.en.html
# https://github.com/backtracking/ocamlgraph
Source0: %name-%version.tar
BuildRequires: libart_lgpl-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-lablgtk-devel
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-ocaml >= 1.3
%global libname %(sed -e 's/^ocaml-//' <<< %name)
%add_ocaml_req_skip Sig

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

%package tools
Summary: Graph editing tools for %name
Requires: %name = %version-%release
Group: Development/ML

%description tools
The %name-tools package contains graph editing tools for use with
%name.

%prep
%setup

# Fix encoding
for fil in CHANGES COPYING CREDITS; do
  iconv -f latin1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
autoreconf -fisv
%configure
make depend
make OCAMLBEST=opt OCAMLOPT='ocamlopt.opt -g'
make doc

%install
mkdir -p %buildroot%ocamldir
make OCAMLFIND_DESTDIR=%buildroot%ocamldir install-findlib
install -m 0755 -p graph.cmxs %buildroot%ocamldir/%libname

# Include all code and examples in the docs
mkdir -p dox-devel/examples
mkdir -p dox-devel/API
cp -p examples/*.ml dox-devel/examples
cp -p doc/* dox-devel/API

# Install the graph editing tools
mkdir -p %buildroot%_bindir
install -m 0755 -p editor/editor.opt %buildroot/%_bindir/ocaml-graph-editor
install -m 0755 -p dgraph/dgraph.opt %buildroot%_bindir/ocaml-graph-viewer
install -m 0755 -p view_graph/viewgraph.opt \
    %buildroot%_bindir/ocaml-viewgraph

%files
%doc CREDITS FAQ COPYING LICENSE
%ocamldir/%libname/
%exclude %ocamldir/*/*.a
%exclude %ocamldir/*/*.cmxa
%exclude %ocamldir/*/*.cmx
%exclude %ocamldir/*/*.o
%exclude %ocamldir/*/*.mli

%files devel
%doc CHANGES README.adoc dox-devel/*
%ocamldir/*/*.a
%ocamldir/*/*.cmxa
%ocamldir/*/*.cmx
%ocamldir/*/*.o
%ocamldir/*/*.mli

%files tools
%_bindir/*

%changelog
* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 1.8.7-alt1%ubt
- first build for ALT
