%define oname dictdiffer

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1
Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dictdiffer
BuildArch: noarch

# https://github.com/inveniosoftware/dictdiffer.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest-runner
BuildRequires: python2.7(check_manifest)
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(isort)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(pydocstyle)
BuildRequires: python2.7(pytest_cache)
BuildRequires: python2.7(pytest_cov)
BuildRequires: python2.7(pytest_pep8)
BuildRequires: python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest-runner
BuildRequires: python3(check_manifest)
BuildRequires: python3(coverage)
BuildRequires: python3(isort)
BuildRequires: python3(mock)
BuildRequires: python3(pydocstyle)
BuildRequires: python3(pytest_cache)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_pep8)
BuildRequires: python3(pytest)
%endif

%description
Dictdiffer is a library that helps you to diff and patch dictionaries.

%if_with python3
%package -n python3-module-%oname
Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
Group: Development/Python3

%description -n python3-module-%oname
Dictdiffer is a library that helps you to diff and patch dictionaries.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_build_install
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
%doc *.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
