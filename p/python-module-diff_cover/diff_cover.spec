%define oname diff_cover

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.0
Release: alt1.git20150602
Summary: Automatically find diff lines that need test coverage
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/diff_cover
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Bachmann1234/diff-cover.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-jinja2 python-module-lazy
BuildPreReq: python-module-six python-module-jinja2_pluralize
BuildPreReq: python-module-Pygments pylint
BuildPreReq: python-module-mock python-module-nose
BuildPreReq: python-module-coverage python-tools-pep8
BuildPreReq: python-module-flake8 pyflakes
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-lazy
BuildPreReq: python3-module-six python3-module-jinja2_pluralize
BuildPreReq: python3-module-Pygments pylint-py3
BuildPreReq: python3-module-mock python3-module-nose
BuildPreReq: python3-module-coverage python3-tools-pep8
BuildPreReq: python3-module-flake8 python3-pyflakes
%endif

%py_provides %oname
%py_requires jinja2 lazy six pygments

%description
Automatically find diff lines that need test coverage. Also finds diff
lines that have violations (according to tools such as pep8, pyflakes,
flake8, or pylint). This is used as a code quality metric during code
reviews.

%if_with python3
%package -n python3-module-%oname
Summary: Automatically find diff lines that need test coverage
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 lazy six pygments

%description -n python3-module-%oname
Automatically find diff lines that need test coverage. Also finds diff
lines that have violations (according to tools such as pep8, pyflakes,
flake8, or pylint). This is used as a code quality metric during code
reviews.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
export LC_ALL=en_US.UTF-8
python setup.py test
coverage run -m nose -vv
%if_with python3
pushd ../python3
python3 setup.py test
coverage3 run -m nose -vv
popd
%endif

%files
%doc AUTHORS CHANGELOG NOTICE *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG NOTICE *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150602
- Initial build for Sisyphus

