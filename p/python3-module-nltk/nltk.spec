%define _unpackaged_files_terminate_build 1
%define oname nltk

%def_with check

Name: python3-module-%oname
Version: 3.6.1
Release: alt1

Summary: Python modules for Natural Language Processing (NLP)
License: Apache-2.0
Group: Development/Python3
Url: http://www.nltk.org

Source: %name-%version.tar
# apply only for tests on RPM build
Patch0: skip_nltk_data_tests.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(click)
BuildRequires: python3(joblib)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(regex)
BuildRequires: python3(scipy)
BuildRequires: python3(sklearn)
BuildRequires: python3(sqlite3)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tqdm)
%endif

BuildArch: noarch
# direct dep
%py3_requires joblib

# optional deps, not packaged yet
%filter_from_requires /python3\(\.[[:digit:]]\)\?(twython\(\..*\)\?)/d

%description
NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in
Natural Language Processing.

%prep
%setup

# upstream applied major.minor.patch only for pypi releases
sed -i 's/^[0-9]\.[0-9]$/%version/' nltk/VERSION
echo '%version' | diff nltk/VERSION -

%build
%python3_build

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/*/test

%check
patch -p1 < %PATCH0
export PIP_NO_INDEX=YES
export TOXENV=py3
export NO_INTERNET=YES
export MPLBACKEND=Agg
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc LICENSE.txt
%_bindir/nltk
%python3_sitelibdir/nltk/
%python3_sitelibdir/nltk-%version-py%_python3_version.egg-info/

%changelog
* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.2.1 -> 3.6.1.

* Mon Dec 19 2016 Kirill Maslinsky <kirill@altlinux.org> 3.2.1-alt1
- Update to 3.2.1
- Drop nltk_contrib from this package

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt3
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Fixed build

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.beta7.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.beta7
- Rebuilt with python 2.6

* Thu Nov 12 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta7
- 2.0 beta7
- nltk and nltk_contrib packaged together

* Tue Sep 15 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta5
- 2.0 beta5
- nltk and nltk_contrib now are separate packages
- correct License tag: Apache license
- do not build java interface
- spec cleanup (use proper macros for python build and install)

* Sun May 24 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.9-alt1
- 0.9.9

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1.1
- fixed packaging
    - build as noarch
    - fix pythonic pseudo-unmets
    - do not package copy of PyYAML
    - use description from PKG-INFO

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

