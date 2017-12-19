%define _unpackaged_files_terminate_build 1
%define oname haven

%def_with python3

Name: python-module-%oname
Version: 1.1.111
Release: alt1
Summary: flask's style binary server framework
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/haven/

# https://github.com/dantezhu/haven.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-events python-module-netkit python2.7(setproctitle)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-events python3-module-netkit python3(setproctitle)
BuildRequires: python-tools-2to3 python3(gevent) python3(geventwebsocket)
%endif

%py_provides %oname
%py_requires events netkit

%description
flask's style binary server framework.

%package -n python3-module-%oname
Summary: flask's style binary server framework
Group: Development/Python3
%py3_provides %oname
%py3_requires events netkit

%description -n python3-module-%oname
flask's style binary server framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.111-alt1
- Updated to upstream version 1.1.111.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.88-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.65-alt1.git20141127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.65-alt1.git20141127.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.65-alt1.git20141127
- Version 1.1.65

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.60-alt1.git20141120
- Initial build for Sisyphus

