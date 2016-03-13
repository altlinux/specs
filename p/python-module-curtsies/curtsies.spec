%define modulename curtsies

%def_with python3

Name: python-module-%modulename
Version: 0.1.19
Release: alt1.1

%setup_python_module %modulename

Summary: Library for interacting with the terminal
License: MIT
Group: Development/Python

Url: https://github.com/thomasballinger/curtsies
BuildArch: noarch

Source: %modulename-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
Curtsies is a library for interacting with the terminal.

%package -n python3-module-%modulename
Summary: Library for interacting with the terminal
Group: Development/Python3

%description -n python3-module-%modulename
Curtsies is a library for interacting with the terminal.

%prep
%setup -n %modulename-%version

%if_with python3
rm -rf ../%name-python3
cp -fR . ../%name-python3
%endif

%build
%python_build

%if_with python3
pushd ../%name-python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../%name-python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.19-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.19-alt1
- Initial build.
