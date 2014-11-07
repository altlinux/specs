%define oname hg-git

%def_without python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20141029
Summary: Push to and pull from a Git repository using Mercurial
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/hg-git/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schacon/hg-git.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-ordereddict
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dulwich mercurial mercurial-hgext git unzip
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dulwich
%endif

%py_provides hggit

%description
This extension lets you communicate (push and pull) with a Git server.
This way you can use Git hosting for your project or collaborate with a
project that is in Git. A bridger of worlds, this plugin be.

%package -n python3-module-%oname
Summary: Push to and pull from a Git repository using Mercurial
Group: Development/Python3
%py3_provides hggit

%description -n python3-module-%oname
This extension lets you communicate (push and pull) with a Git server.
This way you can use Git hosting for your project or collaborate with a
project that is in Git. A bridger of worlds, this plugin be.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
#make tests
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CONTRIBUTING *.txt *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTING *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141029
- Initial build for Sisyphus

