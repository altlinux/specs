Name:    termgraph
Version: 0.5.3
Release: alt1

Summary: A python command-line tool which draws basic graphs in the terminal
License: MIT
Group:   Other
URL:     https://github.com/mkaz/termgraph

Packager: Alexander Burmatov <thatman@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar

Patch1: fix-imports.patch

%description
A command-line tool that draws basic graphs in the terminal, written in Python.
Graph types supported:
* Bar Graphs
* Color charts
* Multi-variable
* Stacked charts
* Histograms
* Horizontal or Vertical
* Emoji!

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info
%doc *.md

%changelog
* Mon Dec 12 2022 Alexander Burmatov <thatman@altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus
