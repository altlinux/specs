%define  modulename memory_profiler

Name:    python3-module-%modulename
Version: 0.57
Release: alt2

Summary: Monitor Memory usage of Python code
License: BSD
Group:   Development/Python3
URL:     https://github.com/fabianp/memory_profiler

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3

%py3_provides %modulename

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This is a python module for monitoring memory consumption of a process
as well as line-by-line analysis of memory consumption for python
programs. It is a pure python module and has the psutil module as
optional (but highly recommended) dependencies.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/mprof
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.57-alt2
- Drop python2 support.

* Fri Jan 17 2020 Andrey Cherepanov <cas@altlinux.org> 0.57-alt1
- New version.

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 0.56-alt1
- New version.
- Build only for Python 3.x.
- Package mprof executable.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 0.55-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.53.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.50-alt1
- New version.

* Sat Apr 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.46-alt1
- New version

* Fri Mar 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.45-alt1
- New version

* Wed Mar 22 2017 Andrey Cherepanov <cas@altlinux.org> 0.44-alt1
- New version

* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.43-alt1
- new version 0.43

* Fri Jul 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.41-alt2
- Do not package executable in module
- Add documentation to python2 module

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.41-alt1
- Initial build for ALT Linux
