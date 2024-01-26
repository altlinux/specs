%define oname curio

%def_with check

Name: python3-module-curio
Version: 1.6
Release: alt1
Summary: Coroutine-based library for concurrent Python systems programming using async/await
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/dabeaz/curio
Vcs: https://github.com/dabeaz/curio.git

BuildArch: noarch

Source: %name-%version.tar
Patch: add-py312-support.patch

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
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m 'not internet'

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%doc README.rst CHANGES

%changelog
* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 1.6-alt1
- new version 1.6

* Sun Oct 16 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- Initial build.

