%define oname figleaf

%def_without python3

Name: python-module-%oname
Version: 0.6.1
Release: alt2.1
Summary: figleaf code coverage tool
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/figleaf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires nose

%description
figleaf is a Python code coverage analysis tool, built somewhat on the
model of Ned Batchelder's fantastic coverage module. The goals of
figleaf are to be a minimal replacement of 'coverage.py' that supports
more configurable coverage gathering and reporting.

%if_with python3
%package -n python3-module-%oname
Summary: figleaf code coverage tool
Group: Development/Python3
%py3_provides %oname
%py3_requires nose

%description -n python3-module-%oname
figleaf is a Python code coverage analysis tool, built somewhat on the
model of Ned Batchelder's fantastic coverage module. The goals of
figleaf are to be a minimal replacement of 'coverage.py' that supports
more configurable coverage gathering and reporting.
%endif

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
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc IDEAS TODO *.html *.txt doc examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc IDEAS TODO *.html *.txt doc examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Fixed build

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

