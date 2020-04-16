%define oname dictdiffer

Name: python3-module-%oname
Version: 0.7.0
Release: alt2

Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dictdiffer

BuildArch: noarch

# https://github.com/inveniosoftware/dictdiffer.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
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

%description
Dictdiffer is a library that helps you to diff and patch dictionaries.

%prep
%setup

%build
%python3_build

%install
%python3_build_install

%check
%__python3 setup.py test

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- Build for python2 disabled.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
