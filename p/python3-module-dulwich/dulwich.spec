%define _unpackaged_files_terminate_build 1
%define pypi_name dulwich
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.7
Release: alt1

Summary: Python Git Library
License: Apache-2.0 or GPL-2.0-or-later
Group: Development/Python3
Url: https://www.dulwich.io

Vcs: https://github.com/dulwich/dulwich.git
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-semantic_version
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: python3-module-setuptools-rust
%if_with check
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-fastimport
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
BuildRequires: git
BuildRequires: gnupg
BuildRequires: gnupg2
%endif

%description
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

%package tests
Summary: Tests for dulwich
Group: Development/Python3
Requires: %name = %EVR

%description tests
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

This package contains tests for dulwich.

%prep
%setup -a1

%build
mkdir -p .cargo
cat > .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF
%pyproject_build

%install
%pyproject_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
# tests/compat/ requires network access (git daemon via TCP), unavailable
#   in the isolated build environment (NO_INTERNET=YES).
# contrib/ fails due to error in dulwich/contrib/swift.py
#   (NameError: ObjectFormat is not defined).
# fuzzing/ requires 'atheris' (fuzzing framework), not available at build time.
# test_apply_delta_only_raises_apply_delta_error: apply_delta() raises TypeError
#   instead of ApplyDeltaError when a copy command (cmd & 0x80) references bytes
#   beyond the end of the delta buffer (ord() on empty slice b'').
%pyproject_run_pytest --ignore=tests/compat --ignore=contrib --ignore=fuzzing \
    --deselect property_tests/test_pack.py::PackPropertyTests::test_apply_delta_only_raises_apply_delta_error

%files
%_bindir/dulwich.py3
%_bindir/dul-upload-pack.py3
%_bindir/dul-receive-pack.py3
%python3_sitelibdir/%module_name/
%exclude %python3_sitelibdir/%module_name/tests
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc COPYING NEWS docs/*.txt
%doc docs/tutorial README.rst examples

%files tests
%python3_sitelibdir/%module_name/tests

%changelog
* Wed Jun 17 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.2.7-alt1
- NMU: updated to 1.2.7.

* Wed Jun 09 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.2.1-alt1
- NMU: updated to 1.2.1.

* Wed Apr 01 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.1.0-alt1
- NMU: updated to 1.1.0.

* Wed Jan 22 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.22.7-alt1
- NMU: 0.22.7 (Closes: #52703).

* Wed Sep 04 2024 L.A. Kostis <lakostis@altlinux.ru> 0.22.1-alt2
- Fix FTBFS: add semantic_version to BR.

* Thu May 09 2024 L.A. Kostis <lakostis@altlinux.ru> 0.22.1-alt1
- NMU:
  + 0.22.1.
  + added rust BR.

* Thu May 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.21.5-alt2
- Bootstrap for python3.11.

* Wed May 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.21.5-alt1
- 0.21.5

* Tue Mar 28 2023 Yuri N. Sedunov <aris@altlinux.org> 0.21.3-alt1
- 0.21.3

* Sat Dec 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.50-alt1
- 0.20.50
- fixed Url, Vcs, Source and License tags
- ported to %%pyproject* macros
- enabled %%check

* Mon Aug 12 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.19.11-alt1
- Release 0.19.11

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20120327.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20120327
- Initial build for Sisyphus

