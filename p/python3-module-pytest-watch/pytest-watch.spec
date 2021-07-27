%define oname pytest-watch

Name: python3-module-%oname
Version: 4.2.0
Release: alt2
Summary: Local continuous test runner with pytest and watchdog
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-watch/

# https://github.com/joeyespo/pytest-watch.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python3-module-watchdog
BuildRequires: python3-module-colorama
BuildRequires: python3-module-docopt

%py3_provides pytest_watch

%description
pytest-watch a zero-config CLI tool that runs pytest, and reruns it when
a file in your project changes.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc *.md
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt2
- Rename package, spec cleanup.

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- 4.2.0
- removed python-2.7 support

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2.git20150206.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.git20150206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt2.git20150206
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150206
- Version 1.0.0

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150111
- Initial build for Sisyphus

