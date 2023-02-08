%define _unpackaged_files_terminate_build 1

%def_with check

%define  modulename trio

Name:    python3-module-%modulename
Version: 0.22.0
Release: alt2

Summary: Trio - Pythonic async I/O for humans and snake people

License: MIT or Apache-2.0
Group:   Development/Python3
URL:     https://github.com/python-trio/trio

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
Buildrequires: python3-module-async_generator
Buildrequires: python3-module-idna
Buildrequires: python3-module-sniffio
Buildrequires: python3-module-outcome
Buildrequires: python3-module-sortedcontainers
Buildrequires: python3-module-astor
Buildrequires: python3-module-trustme
Buildrequires: python3-module-OpenSSL
Buildrequires: python3-module-jedi
Buildrequires: python3-module-pylint
%endif

# Self provides
%add_python3_req_skip _common simple_excepthook
# Only in ubuntu
%add_python3_req_skip apport_python_hook

BuildArch: noarch

Source:  %modulename-%version.tar

%description
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

%package tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: %name = %EVR

%description tests
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

# Upstream doesn't care about version
sed -i 's/0.21.0+dev/%version/' trio/_version.py

%build
%python3_build

%install
%python3_install

%check
%tox_create_default_config
# Seems that upstream checks this project with very old pytest
%tox_check -- -k" \
not test_simple_cancel_scope_usage_doesnt_create_cyclic_garbage \
and not test_cancel_scope_exit_doesnt_create_cyclic_garbage \
and not test_nursery_cancel_doesnt_create_cyclic_garbage \
and not test_locals_destroyed_promptly_on_cancel"

%files
%doc *.md *.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%modulename/tests
%exclude %python3_sitelibdir/%modulename/testing
%exclude %python3_sitelibdir/%modulename/_core/tests

%files tests
%python3_sitelibdir/%modulename/tests
%python3_sitelibdir/%modulename/testing
%python3_sitelibdir/%modulename/_core/tests
%doc *.md *.rst

%changelog
* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.22.0-alt2
- Fixed packaging tests.

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.22.0-alt1
- Automatically updated to 0.22.0.
- Bring tests back as separate subpackage.

* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.0-alt1
- Updated to upstream version 0.19.0 to fix python-3.10 compatibility issues

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- don't pack tests (ALT bug 39239)

* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
