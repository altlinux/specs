%define _unpackaged_files_terminate_build 1

%define oname fastjsonschema

Name: python3-module-%oname
Version: 2.15.1
Release: alt1
Summary: Fast JSON schema validator for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/horejsek/python-fastjsonschema

BuildArch: noarch

# https://github.com/horejsek/python-fastjsonschema.git
Source: %name-%version.tar

# submodules
Source1: %name-%version-JSON-Schema-Test-Suite.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-benchmark

%description
Fast JSON schema validator for Python

%prep
%setup -a1

%build
%python3_build

%install
%python3_install

%check
# following tests don't work without network and there's no obvious way to disable them
rm -f tests/json_schema/test_draft04.py
rm -f tests/json_schema/test_draft06.py
rm -f tests/json_schema/test_draft07.py

PYTHONPATH=$(pwd) py.test3 -vv

%files
%doc LICENSE
%doc README.rst AUTHORS CHANGELOG.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.15.1-alt1
- Initial build for ALT.
