%define oname summary

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: Extractor to get main content from the web page
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/summary/
# https://github.com/after12am/summary.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires chardet lxml nltk numpy networkx

BuildRequires: python3-module-chardet python3-module-html5lib python3-module-networkx-core python3-module-nltk python3-module-pydot python3-module-pygraphviz
BuildRequires: python3-module-numpy-testing python-tools-2to3

%description
A python script provides content extraction and summarization of the web
page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip html

%description tests
A python script provides content extraction and summarization of the web
page.

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*

%files tests
%python3_sitelibdir/*/test.*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- disable python2

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150209.1.1.1.1
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150209.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150209
- Initial build for Sisyphus

