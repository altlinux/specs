%def_with python3

%global modname logutils

Name:               python-module-%{modname}
Version:            0.3.3
Release:            alt1.1
Summary:            Logging utilities

Group:              Development/Python
License:            BSD
URL:                http://pypi.python.org/pypi/logutils
Source0:            %{name}-%{version}.tar

BuildArch:          noarch

BuildRequires:      python-devel

%if_with python3
BuildRequires:      rpm-build-python3
%endif

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and so
they are packaged here. Others are updated versions which have appeared in
recent Python releases, but are usable with older versions of Python and so
are packaged here.

%if_with python3
%package -n python3-module-logutils
Summary:            Logging utilities
Group:              Development/Python

%description -n python3-module-logutils
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and so
they are packaged here. Others are updated versions which have appeared in
recent Python releases, but are usable with older versions of Python and so
are packaged here.
%endif

%prep
%setup

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
%{__python} setup.py test
%if_with python3
pushd ../python3
%{__python3} setup.py test
popd
%endif

%files
%doc README.txt LICENSE.txt NEWS.txt doc/
%{python_sitelibdir}/%{modname}/
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-%{modname}
%doc README.txt LICENSE.txt NEWS.txt doc/
%{python3_sitelibdir}/%{modname}/
%{python3_sitelibdir}/%{modname}-%{version}-*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.3-alt1
- First build for ALT (based on Fedora 0.3.3-3.fc21.src)

