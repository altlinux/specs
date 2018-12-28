%define  modulename more-itertools
%def_with python3

Name:    python-module-%modulename
Version: 5.0.0
Release: alt1

Summary: More routines for operating on iterables, beyond itertools
License: MIT
Group:   Development/Python
URL:     https://github.com/erikrose/more-itertools

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%if_with python3
%package -n python3-module-%modulename
Summary: More routines for operating on iterables, beyond itertools
Group: Development/Python3

%description -n python3-module-%modulename
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.
%endif

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%python_sitelibdir/more_itertools*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/more_itertools*
%endif

%changelog
* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Mon Aug 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version.

* Tue Jul 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus
