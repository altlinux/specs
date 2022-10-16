
Summary: Coroutine-based library for concurrent Python systems programming using async/await
Name: python3-module-curio
Version: 1.5
Release: alt1
Url: https://github.com/dabeaz/curio
Vcs: https://github.com/dabeaz/curio.git
Source: %name-%version.tar
License: BSD
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
# For check
BuildRequires: pytest3

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
%python3_build

%install
%python3_install

%check
python3 -m pytest -v

%files
%python3_sitelibdir/*
%doc README.rst CHANGES

%changelog
* Sun Oct 16 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- Initial build.

