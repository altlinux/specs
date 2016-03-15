# Created by pyp2rpm-1.0.1
%global pypi_name singledispatch

%def_with python3

Name:           python-module-%{pypi_name}
Version:        3.4.0.3
Release:        alt1.1.1
Summary:        This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3
Group:          Development/Python

License:        MIT
URL:            http://docs.python.org/3/library/functools.html#functools.singledispatch
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-ordereddict python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-six

Requires:       python-module-six
Requires:       python-module-ordereddict
#BuildRequires:  python-module-ordereddict
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:  python3-devel
#BuildRequires:  python3-module-setuptools
#BuildRequires:  python3-module-six
%endif

%description
PEP 443 proposed to expose a mechanism in the functools standard library
module in Python 3.4 that provides a simple form of generic programming 
known as single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%package -n python3-module-%pypi_name
Summary:        This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3
Group:          Development/Python3
Requires:       python3-module-six

%description -n python3-module-%pypi_name
PEP 443 proposed to expose a mechanism in the functools standard library
module in Python 3.4 that provides a simple form of generic programming 
known as single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove /usr/bin/env python from scripts
sed -i '1d' singledispatch.py
sed -i '1d' singledispatch_helpers.py

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

# %check
# %{__python} setup.py test

%files
%doc README.rst
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}_helpers.py*

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.4.0.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.3-alt1
- Version 3.4.0.3

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt1.1
- Added module for Python 3

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 3.4.0.2-alt1
- First build for ALT (based on Fedora 3.4.0.2-3.fc21.src)

