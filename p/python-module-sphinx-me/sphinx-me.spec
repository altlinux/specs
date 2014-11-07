%define oname sphinx-me

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140803
Summary: Wraps your README-only projects in a Sphinx shell for hosting on http://readthedocs.org
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-me/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stephenmcd/sphinx-me.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sphinx
%endif

%py_provides sphinx_me
%py_requires sphinx

%description
sphinx-me is a BSD licensed tool that will create a Sphinx documentation
shell for your project and include the README file as the documentation
index. It handles extracting the required meta data such as the project
name, author and version from your project for use in your Sphinx docs.

Once you use sphinx-me to build your Sphinx docs, you can then add your
project to the Read The Docs site and have your project's README hosted
with an attractive Sphinx documentation theme.

NOTE
Your README file should be in a reStructuredText compatible format.

%package -n python3-module-%oname
Summary: Wraps your README-only projects in a Sphinx shell for hosting on http://readthedocs.org
Group: Development/Python3
%py3_provides sphinx_me
%py3_requires sphinx

%description -n python3-module-%oname
sphinx-me is a BSD licensed tool that will create a Sphinx documentation
shell for your project and include the README file as the documentation
index. It handles extracting the required meta data such as the project
name, author and version from your project for use in your Sphinx docs.

Once you use sphinx-me to build your Sphinx docs, you can then add your
project to the Read The Docs site and have your project's README hosted
with an attractive Sphinx documentation theme.

NOTE
Your README file should be in a reStructuredText compatible format.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140803
- Initial build for Sisyphus

