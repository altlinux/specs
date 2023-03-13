%define _unpackaged_files_terminate_build 1
%define oname avro

%def_with check

Name: python3-module-%oname
Version: 1.11.1
Release: alt2

Summary: Avro is a serialization and RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/avro/

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Apache Avro(tm) is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not
  required to read or write data files nor to use or implement RPC
  protocols. Code generation as an optional optimization, only worth
  implementing for statically typed languages.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Apache Avro(tm) is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not
  required to read or write data files nor to use or implement RPC
  protocols. Code generation as an optional optimization, only worth
  implementing for statically typed languages.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# test_server_with_path: tries to connect to apache.org
py.test-3 -k 'not test_server_with_path'

%files
%doc PKG-INFO
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/test

%files tests
%python3_sitelibdir/%oname/test
%doc PKG-INFO


%changelog
* Mon Mar 13 2023 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 1.11.1-alt2
- Increase tests timeout

* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 1.11.1-alt1
- new version 1.11.1

* Mon Oct 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.7-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.7-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.7-alt1
- Initial build for Sisyphus

