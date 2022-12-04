Name: python3-module-pep440
Version: 0.1.2
Release: alt1
Summary: A simple package with utils to check whether versions number match Pep 440
Group: Development/Python
License: MIT
Url: https://pypi.org/pypi/pep440
VCS: https://github.com/Carreau/pep440
Source0: %name-%version.tar
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-pytest
BuildRequires: python3-module-wheel
BuildRequires: python3-module-flit-core
BuildArch: noarch

%description 
%summary

%prep
%setup 

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -svv -k "not test_cli"

%files
%doc readme.md 
%_bindir/pep440
%python3_sitelibdir/*

%changelog
* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- fisrt build fot ALT
