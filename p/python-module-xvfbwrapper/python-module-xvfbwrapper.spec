%global pypi_name xvfbwrapper
%define version 0.2.4

%def_with python3

Name:           python-module-%{pypi_name}
Version:        %{version}
Release:        alt1.1
Group:          Development/Python
Summary:        run headless display inside X virtual framebuffer (Xvfb)

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        %{name}-%{version}.tar

BuildArch:      noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

#BuildRequires:  python-module-setuptools

%description
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%if_with python3
%package -n python3-module-%pypi_name
Summary:        run headless display inside X virtual framebuffer (Xvfb)
Group:          Development/Python
BuildRequires(pre): rpm-build-python3 python3-module-setuptools
#BuildRequires:  python3-devel

%description -n python3-module-%pypi_name
Python wrapper for running a display inside X virtual framebuffer (Xvfb)
%endif

%prep
%setup

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
%doc README.rst
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}-%{version}-py%{_python_version}.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.rst
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/__pycache__/%{pypi_name}.*
%{python3_sitelibdir}/%{pypi_name}-%{version}-py%{_python3_version}.egg-info
%endif # with_python3

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 0.2.4-alt1
- First build for ALT (based on Fedora 0.2.4-2.fc24.src)
