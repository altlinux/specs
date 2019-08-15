%define _unpackaged_files_terminate_build 1
%define oname snuggs

%def_with check

Name: python-module-%oname
Version: 1.4.6
Release: alt1
Summary: Snuggs are s-expressions for Numpy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/snuggs

# https://github.com/mapbox/snuggs.git
Source: %name-%version.tar
Patch: snuggs-1.4.6-Skip-some-broken-assertions.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(hypothesis)
BuildRequires: python2.7(numpy)
BuildRequires: python2.7(pyparsing)
BuildRequires: python2.7(pytest)
BuildRequires: python3(hypothesis)
BuildRequires: python3(numpy)
BuildRequires: python3(pyparsing)
BuildRequires: python3(pytest)
%endif

%description
Snuggs are s-expressions for Numpy.

%package -n python3-module-%oname
Summary: Snuggs are s-expressions for Numpy
Group: Development/Python3

%description -n python3-module-%oname
Snuggs are s-expressions for Numpy.

%prep
%setup
%patch -p1

cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
py.test -vv
pushd ../python3
py.test3 -vv
popd

%files
%doc *.txt *.rst
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%python_sitelibdir/%oname/__init__.py
%python_sitelibdir/%oname/__init__.py[oc]

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/__init__.py
%python3_sitelibdir/%oname/__pycache__/__init__.cpython-*.py*

%changelog
* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 1.4.6-alt1
- 1.4.1 -> 1.4.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt3
- Updated build dependencies.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.git20150403.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20150403.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150403
- Initial build for Sisyphus

