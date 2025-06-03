%define _unpackaged_files_terminate_build 1
%define oname pyaml

%def_with check

Name: python3-module-%oname
Version: 25.5.0
Release: alt1

Summary: PyYAML-based module to produce pretty and readable YAML-serialized data
License: WTFPL
Group: Development/Python3
Url: https://pypi.org/project/pyaml
VCS: https://github.com/mk-fg/pretty-yaml
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(yaml)

BuildRequires: python3(unidecode)
%endif

%description
PyYAML-based module to produce pretty and readable YAML-serialized data.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc COPYING README.rst
%_bindir/pyaml
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%exclude %python3_sitelibdir/*/tests

%changelog
* Tue Jun 03 2025 Stanislav Levin <slev@altlinux.org> 25.5.0-alt1
- 25.1.0 -> 25.5.0.

* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 25.1.0-alt1.1
- NMU: fixed FTBFS (tox 4).

* Sun Jan 05 2025 Grigory Ustinov <grenka@altlinux.org> 25.1.0-alt1
- Automatically updated to 25.1.0.

* Tue Dec 31 2024 Grigory Ustinov <grenka@altlinux.org> 24.12.1-alt1
- Build new version.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 21.10.1-alt2
- Moved on modern pyproject macros.

* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 21.10.1-alt1
- 16.12.2 -> 21.10.1.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 16.12.2-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 16.12.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 16.12.2-alt1
- automated PyPI update

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.02.1-alt1.git20150216
- Version 15.02.1

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.12.10-alt1.git20141204
- Version 14.12.10

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.11.3-alt1.git20141110
- Version 14.11.3

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.7-alt1.git20140528
- Initial build for Sisyphus

