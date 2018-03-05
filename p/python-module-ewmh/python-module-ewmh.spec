%def_with python3
%def_with test
%define modulename ewmh

Name: python-module-%modulename
Version: 0.1.6
Release: alt2
Summary: An implementation of EWMH (Extended Window Manager Hints) for python, based on Xlib

License: GPLv3
Group: Development/Python
Url: https://github.com/parkouss/pyewmh
Packager: Python Development Team <python@packages.altlinux.org>

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-xlib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-xlib
%endif
%py_provides %modulename

%description
An implementation of EWMH (Extended Window Manager Hints) for python, based on
Xlib. It allows EWMH-compliant window managers (most modern WMs) to be queried
and controlled.

%package -n python3-module-%modulename
Summary: Helpers for better testing
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
An implementation of EWMH (Extended Window Manager Hints) for python3, based on
Xlib. It allows EWMH-compliant window managers (most modern WMs) to be queried
and controlled.

%prep
%setup
%if_with python3
cp -fR . ../python3-module-%modulename
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%modulename
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%modulename
%python3_install
popd
%endif

%if_with test
%check
export LC_ALL=en_US.UTF-8
python setup.py test

%if_with python3
pushd ../python3-module-%modulename
python3 setup.py test
popd
%endif
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux.
