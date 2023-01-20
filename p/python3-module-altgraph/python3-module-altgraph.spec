%define  modulename altgraph

Name:    python3-module-%modulename
Version: 0.17.3
Release: alt1

Summary: altgraph is a fork of graphlib: a graph (network) package for constructing graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with graphviz output
License: MIT
Group:   Development/Python3
URL:     https://github.com/ronaldoussoren/altgraph

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output. altgraph includes some additional usage of Python 2.3+
features and enhancements related to modulegraph and macholib.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 0.17.3-alt1
- New version.

* Sun Sep 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.17.2-alt1
- Initial build for Sisyphus.
