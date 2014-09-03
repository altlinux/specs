%define tarname mastertickets
Name: python-module-trac-mastertickets
%define r_minor r13684
Version: 3.0.5
Release: alt1.%r_minor

Summary: Adds basic ticket dependencies for Trac

Group: Development/Python
License: BSD
Url: http://trac-hacks.org/wiki/MasterTicketsPlugin

# http://trac-hacks.org/svn/masterticketsplugin/trunk/
Source: trac-%{tarname}-%r_minor.tar.gz

BuildArch: noarch

BuildRequires: python-module-setuptools

Requires: graphviz

%description
This plugin adds "blocks" and "blocked by" fields to each ticket, enabling you
to express dependencies between tickets. It also provides a graphviz-based
dependency-graph feature for those tickets having dependencies specified,
allowing you to visually understand the dependency tree. The dependency graph
is viewable by clicking 'depgraph' in the context (in the upper right corner)
menu when viewing a ticket that blocks or is blocked by another ticket.

%prep
%setup -n coderanger-trac-%tarname-%r_minor

%build
%python_build

%install
%python_install

#Fix rights
#chmod -R a+r %buildroot%python_sitelibdir/tracrpc/htdocs
#chmod -R a+r %buildroot%python_sitelibdir/tracrpc/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.r13684
- Version 3.0.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1.6543.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.1-alt1.6543
- Build for ALT
