%define oname json_resource

Name: python3-module-%oname
Version: 0.2.11
Release: alt2

Summary: JSON resources are dict, and list, etc. types
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/json_resource/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-json_pointer
BuildRequires: python3-module-pymongo
BuildRequires: python3-module-json_patch

%description
JSON resources are dict, and list, etc. types. They behave like oridnary
python dicts and lists, but have extra functionality from several json
standards.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
py.test3 json_resource/tests/test_instance.py \
    json_resource/tests/test_resource.py

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.11-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.11-alt1
- Updated to upstream version 0.2.11.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

