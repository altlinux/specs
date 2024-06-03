%define _unpackaged_files_terminate_build 1
%define oname avro

%def_with check

Name: python3-module-%oname
Version: 1.11.3
Release: alt3

Summary: Avro is a serialization and RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/avro/

Source: %name-%version.tar
Patch: avro-alt-test-timeout.patch
Patch1: drop-distutils.patch
Patch2: avro-tests-make-test_server_with_path-conditional.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/test

%files tests
%python3_sitelibdir/%oname/test


%changelog
* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 1.11.3-alt3
- Fixed FTBFS (Pytest 8.2.0).

* Thu Oct 12 2023 Anton Vyatkin <toni@altlinux.org> 1.11.3-alt2
- drop distutils dependency

* Tue Sep 26 2023 Anton Vyatkin <toni@altlinux.org> 1.11.3-alt1
- new version 1.11.3

* Sat Aug 26 2023 Anton Vyatkin <toni@altlinux.org> 1.11.2-alt1
- new version 1.11.2

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

