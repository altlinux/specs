%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx-paramlinks
%define mod_name sphinx_paramlinks

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Allows param links in Sphinx function/method descriptions to be linkable
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sphinx-paramlinks
Vcs: https://github.com/sqlalchemyorg/sphinx-paramlinks
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

# PEP503 name
%py3_provides %pypi_name

%description
A Sphinx extension which allows :param: directives within Python
documentation to be linkable.

This is an experimental extension that's used by the SQLAlchemy project
and related projects.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# tests not exist in upstream

%files
%doc README.*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%mod_name-%version.dist-info


%changelog
* Mon Oct 16 2023 Anton Vyatkin <toni@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.2-alt2
- Porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

