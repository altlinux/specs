%def_with python3
%define mname sphinxcontrib
%define oname %mname-asyncio

Name: python-module-%oname
Version: 0.2.0
Release: alt3.1
Summary: Sphinx extension for adding asyncio-specific markups

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-asyncio
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/03/52/14e11f82a263a6b4c3c66738952f557ee78cde51077cbd949fbf739fa9b4/%oname-%version.tar.gz
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools
%py_provides %mname.asyncio
%py_requires %mname

%description
Sphinx extension for adding asyncio-specific markups.

%package -n python3-module-%oname
Summary: Sphinx extension for adding asyncio-specific markups
Group: Development/Python
%py3_provides %mname.asyncio
%py3_requires %mname

%description -n python3-module-%oname
Sphinx extension for adding asyncio-specific markups.
Python 3 version.

%prep
%setup -n %oname-%version

%if_with python3
rm -fR ../python3-module-%oname-%version
cp -fR . ../python3-module-%oname-%version
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%oname-%version
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/*
%exclude %python_sitelibdir/%mname/__init__.py*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%exclude %python3_sitelibdir/%mname/__init__.py*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt3
- srpm build

* Sat Sep 24 2016 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt2
- Fixed a conflict with the package python-module-sphinxcontrib.

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for ALT Linux Sisyphus.
