%def_with python3
%define mname sphinxcontrib
%define oname %mname-asyncio

Name: python-module-%oname
Version: 0.2.0
Release: alt1
Summary: Sphinx extension for adding asyncio-specific markups

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-asyncio
#Url: https://github.com/aio-libs/sphinxcontrib-asyncio
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif
BuildPreReq: python-devel python-module-setuptools-tests
%py_provides %mname.asyncio
%py_requires %mname

%description
Sphinx extension for adding asyncio-specific markups.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx extension for adding asyncio-specific markups
Group: Development/Python
%py3_provides %mname.asyncio
%py3_requires %mname

%description -n python3-module-%oname
Sphinx extension for adding asyncio-specific markups.
Python 3 version.
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
%doc LICENSE
%doc README.*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%doc README.*
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for ALT Linux Sisyphus.
