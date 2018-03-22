%define oname http-parser

%def_with python3

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20150514.1.3.1
Summary: http request/response parser
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/http-parser/

# https://github.com/benoitc/http-parser.git
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-Cython python-module-html5lib python-module-notebook python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython python3-module-html5lib python3-module-notebook python3-module-pytest
%endif

%py_provides http_parser

%description
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%package -n python3-module-%oname
Summary: http request/response parser
Group: Development/Python3
%py3_provides http_parser

%description -n python3-module-%oname
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%prep
%setup

rm -f http_parser/parser.c

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3
popd
%endif

%files
%doc NOTICE *.rst *.md THANKS examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc NOTICE *.rst *.md THANKS examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.2
- Updated build spec

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20150514.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20150514.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150514
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20140925
- Initial build for Sisyphus

