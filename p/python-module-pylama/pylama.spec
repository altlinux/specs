%define oname pylama

%def_with python3

Name: python-module-%oname
Version: 6.1.1
Release: alt3.git20141029.1
Summary: pylama -- Code audit tool for python
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pylama/

# https://github.com/klen/pylama.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-ipdb python-tools-pep8 pyflakes
BuildPreReq: pylint python-module-nose git
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-ipdb python3-tools-pep8 python3-pyflakes
BuildPreReq: pylint-py3 python3-module-nose
%endif

%py_provides %oname

%description
pylama -- Code audit tool for python.

%package -n python3-module-%oname
Summary: pylama -- Code audit tool for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pylama -- Code audit tool for python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc AUTHORS Changelog *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Changelog *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.1.1-alt3.git20141029.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 6.1.1-alt3.git20141029
- Recompile for python3.5 changed place of site-packages.

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 6.1.1-alt2.git20141029
- Build back into sisyphus

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.git20141029
- Initial build for Sisyphus

