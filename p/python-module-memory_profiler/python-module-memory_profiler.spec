%define  modulename memory_profiler
%def_with python3

Name:    python-module-%modulename
Version: 0.43
Release: alt1

Summary: Monitor Memory usage of Python code
License: BSD
Group:   Development/Python
URL:     https://github.com/fabianp/memory_profiler

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
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
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.rst
#_bindir/mprof
%python_sitelibdir/%modulename.*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.43-alt1
- new version 0.43

* Fri Jul 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.41-alt2
- Do not package executable in module
- Add documentation to python2 module

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.41-alt1
- Initial build for ALT Linux
