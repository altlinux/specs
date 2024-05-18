%define _unpackaged_files_terminate_build 1
%define oname mongoquery

%def_with check

Name: python3-module-%oname
Version: 1.4.2
Release: alt1

Summary: A python implementation of mongodb queries
License: Public domain
Group: Development/Python3
URL: https://pypi.org/project/mongoquery
VCS: https://github.com/kapouille/mongoquery
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(six)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
A utility library that provides a MongoDB-like query language for
querying python collections. It's mainly intended to parse objects
structured as fundamental types in a similar fashion to what is produced
by JSON or YAML parsers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Automatically updated to 1.4.2.

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Moved on modern pyproject macros.

* Tue Mar 29 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.5 -> 1.4.0.

* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.5-alt1
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.git20170921.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt1.git20170921
- Updated to current upstream version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150105
- Initial build for Sisyphus

