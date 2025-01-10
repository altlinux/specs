%define oname curio

%def_with check

Name: python3-module-curio
Version: 1.6
Release: alt1.11.g5a64e81
Summary: Coroutine-based library for concurrent Python systems programming using async/await
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/dabeaz/curio
Vcs: https://github.com/dabeaz/curio.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Curio is a coroutine-based library for concurrent Python systems programming
using async/await. It provides standard programming abstractions such as
as tasks, sockets, files, locks, and queues as well as some advanced
features such as support for structured concurrency.
It works on Unix and Windows and has zero dependencies.
You'll find it to be familiar, small, fast, and fun.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/dabeaz/curio/issues/368
%pyproject_run_pytest -v -m 'not internet' -k 'not test_cpu'

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%doc README.rst CHANGES

%changelog
* Sat Jan 11 2025 Anton Vyatkin <toni@altlinux.org> 1.6-alt1.11.g5a64e81
- Update to 1.6.0.11.g5a64e81.

* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 1.6-alt1
- new version 1.6

* Sun Oct 16 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- Initial build.

