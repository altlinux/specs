%define _unpackaged_files_terminate_build 1
%define oname pyaml

%def_with check

Name: python3-module-%oname
Version: 21.10.1
Release: alt2

Summary: PyYAML-based module to produce pretty and readable YAML-serialized data
License: WTFPL
Group: Development/Python3
Url: https://pypi.org/project/pyaml/
# https://github.com/mk-fg/pretty-yaml.git
BuildArch: noarch

Source0: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(yaml)

BuildRequires: python3(unidecode)

BuildRequires: python3(tox)
%endif

%description
PyYAML-based module to produce pretty and readable YAML-serialized data.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc COPYING PKG-INFO README README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/*/tests

%changelog
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

