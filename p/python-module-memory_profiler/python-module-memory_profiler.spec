%define  modulename memory_profiler
%def_without python2
%def_with python3

Name:    python-module-%modulename
Version: 0.60
Release: alt1

Summary: Monitor Memory usage of Python code
License: BSD
Group:   Development/Python
URL:     https://github.com/fabianp/memory_profiler

Packager: Andrey Cherepanov <cas@altlinux.org>

%if_with python2
BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This is a python module for monitoring memory consumption of a process
as well as line-by-line analysis of memory consumption for python
programs. It is a pure python module and has the psutil module as
optional (but highly recommended) dependencies.

%if_with python3
%package -n python3-module-%modulename
Summary: Monitor Memory usage of Python code
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
This is a python module for monitoring memory consumption of a process
as well as line-by-line analysis of memory consumption for python
programs. It is a pure python module and has the psutil module as
optional (but highly recommended) dependencies.
%endif

%prep
%setup -n %modulename-%version
%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build
%endif
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python2
%python_install
%endif
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/%modulename.*
%python_sitelibdir/*.egg-info
%endif

%if_with python3
%files -n python3-module-%modulename
%doc *.rst
%_bindir/mprof
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 15 2022 Andrey Cherepanov <cas@altlinux.org> 0.60-alt1
- New version.

* Mon Dec 20 2021 Andrey Cherepanov <cas@altlinux.org> 0.59-alt1
- New version.

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
