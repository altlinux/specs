%define  modulename funcparserlib

Name:    python3-module-%modulename
Version: 0.3.6
Release: alt1

Summary: Recurisve descent parsing library for Python based on functional combinators
License: MIT
Group:   Development/Python3

URL:     https://github.com/vlasovskikh/funcparserlib

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

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
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README CHANGES

%changelog
* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.6-alt1
- Build new version for python3.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1
- Rebuild with Python-2.7

* Wed May 19 2010 Kirill Maslinsky <kirill@altlinux.org> 0.3.4-alt2
- fixed license: MIT, not GPL

* Wed May 19 2010 Kirill Maslinsky <kirill@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
