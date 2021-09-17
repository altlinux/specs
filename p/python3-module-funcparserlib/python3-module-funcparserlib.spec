%define _unpackaged_files_terminate_build 1
%define  modulename funcparserlib

%def_with check

Name:    python3-module-%modulename
Version: 0.3.6
Release: alt2

Summary: Recurisve descent parsing library for Python based on functional combinators
License: MIT
Group:   Development/Python3

URL:     https://github.com/vlasovskikh/funcparserlib

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%if_with check
BuildRequires: python3(tox)
%endif

BuildArch: noarch

Source:  %modulename-%version.tar
Patch0: 0001-Tweak-to-oneplus-to-make-it-act-the-same-as-many-wit.patch
Patch1: 0002-Drop-support-for-EOL-Pythons-Add-support-for-modern-.patch

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
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
# setuptools' `test` command is deprecated
sed -i 's/python setup.py test/python -m unittest discover/' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/
%doc README CHANGES

%changelog
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
