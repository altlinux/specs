%define  modulename funcparserlib

%def_with check

Name:    python3-module-%modulename
Version: 1.0.1
Release: alt1

Summary: Recurisve descent parsing library for Python based on functional combinators

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/funcparserlib
VCS:     https://github.com/vlasovskikh/funcparserlib

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

BuildArch: noarch

Source:  %name-%version.tar

%description
Parser combinators are just higher-order functions that take parsers as their
arguments and return them as result values. Parser combinators are:

    * First-class values
    * Extremely composable
    * Tend to make the code quite compact
    * Resemble the readable notation of xBNF grammars

Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that
it's very easy to write them without thinking about look-aheads and all that
hardcore parsing stuff. But the recursive descent parsing is a rather slow
method compared to LL(k) or LR(k) algorithms.

So the primary domain for funcparserlib is parsing little languages or external
DSLs (domain specific languages).

The library itself is very small. Its source code is only 0.5 KLOC, with lots
of comments included. It features the longest parsed prefix error reporting, as
well as a tiny lexer generator for token position tracking.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 0.3.6-alt2
- Backported 2to3 changes (fixed FTBFS due to new setuptools 58).

* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.6-alt1
- Build new version for python3.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1
- Rebuild with Python-2.7

* Wed May 19 2010 Kirill Maslinsky <kirill@altlinux.org> 0.3.4-alt2
- fixed license: MIT, not GPL

* Wed May 19 2010 Kirill Maslinsky <kirill@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
