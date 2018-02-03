%define _unpackaged_files_terminate_build 1
%define oname hg-git

%def_without python3

Name: python-module-%oname
Version: 0.8.5
Release: alt1.1
Summary: Push to and pull from a Git repository using Mercurial
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/hg-git/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schacon/hg-git.git
Source0: https://pypi.python.org/packages/1c/9c/63d9dbe06b087f152c4455d3c0d0757e63d68e9432c61a8298e81876043c/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-ordereddict
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-dulwich mercurial mercurial-hgext git unzip
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-dulwich
%endif

%py_provides hggit

%description
This extension lets you communicate (push and pull) with a Git server.
This way you can use Git hosting for your project or collaborate with a
project that is in Git. A bridger of worlds, this plugin be.

%if_with python3
%package -n python3-module-%oname
Summary: Push to and pull from a Git repository using Mercurial
Group: Development/Python3
%py3_provides hggit

%description -n python3-module-%oname
This extension lets you communicate (push and pull) with a Git server.
This way you can use Git hosting for your project or collaborate with a
project that is in Git. A bridger of worlds, this plugin be.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.md PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1
- automated PyPI update

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150811
- Version 0.8.2

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150226
- Version 0.8.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141029
- Initial build for Sisyphus

