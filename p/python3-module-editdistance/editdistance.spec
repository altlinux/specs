Name: python3-module-editdistance
Version: 0.8.1
Release: alt1
Group: Development/Python3
License: MIT
Url: https://github.com/roy-ht/editdistance
Summary: Fast implementation of the edit distance (Levenshtein distance)
Source: editdistance-%version.tar.gz

# Automatically added by buildreq on Wed Dec 25 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-anyio python3-module-babel python3-module-charset-normalizer python3-module-dep-logic python3-module-findpython python3-module-httpx python3-module-jaraco.collections python3-module-jaraco.context python3-module-jaraco.functools python3-module-jaraco.text python3-module-jinja2 python3-module-markdown-it python3-module-more-itertools python3-module-packaging python3-module-pbs-installer python3-module-pkg_resources python3-module-platformdirs python3-module-py3dephell python3-module-pyproject-metadata python3-module-pytest python3-module-pytest-mock python3-module-setuptools python3-module-sphinx python3-module-tomli_w python3-module-unearth python3-module-wheel sh5
BuildRequires: gcc-c++ python3-module-Cython python3-module-pdm python3-module-pdm-backend python3-module-pyproject-installer

#_scm python3-module-sphinxcontrib

%description
Fast implementation of the edit distance (Levenshtein distance).

This library simply implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by Heikki Hyyro,
"Explaining and extending the bit-parallel approximate string matching
algorithm of Myers", (2001).

%prep
%setup -n editdistance-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -s test

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed Dec 25 2024 Fr. Br. George <george@altlinux.org> 0.8.1-alt1
- Resurrect
- Autobuild version bump to 0.8.1
- Introduce check section

* Wed Dec 30 2020 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Initial build for ALT
