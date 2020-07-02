%define oname rjsmin

Name: python-module-%oname
Version: 1.0.12
Release: alt2
Summary: Javascript Minifier
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/rjsmin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ndparker/rjsmin.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-epydoc python-modules-xml
BuildPreReq: python-modules-logging python-module-sphinx-devel

%py_provides %oname

%description
rJSmin is a javascript minifier written in python.

%prep
%setup

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
epydoc --config=epydoc.conf
popd

%files
%doc %_docdir/%oname
%python_sitelibdir/*

%changelog
* Thu Jul 02 2020 Stanislav Levin <slev@altlinux.org> 1.0.12-alt2
- Built Python3 package from its own src package.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt3.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 1.0.10-alt3.git20141116
- Python compilation for 3.5.

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.10-alt2.git20141116
- Documentation creation disabled

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20141116
- Initial build for Sisyphus

