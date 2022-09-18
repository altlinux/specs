%define _unpackaged_files_terminate_build 1
%define oname nelsnmp

%def_with check

Name: python3-module-%oname
Version: 0.2.9
Release: alt1

Summary: A wrapper module for pysnmp

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nelsnmp/

BuildArch: noarch

# https://github.com/networklore/nelsnmp.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pysnmp4

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-yaml
%endif

%py3_provides %oname
Requires: python3-module-pysnmp4

%description
%summary.

%prep
%setup

# https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
sed -i 's/yaml.load/yaml.safe_load/' tests/test_device_versions.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sun Sep 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1
- Build new version.
- Build with check.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150315.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150315
- Initial build for Sisyphus

