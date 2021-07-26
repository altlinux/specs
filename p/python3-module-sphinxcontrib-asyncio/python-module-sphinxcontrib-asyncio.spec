%define mname sphinxcontrib
%define oname %mname-asyncio

Name: python3-module-%oname
Version: 0.2.0
Release: alt4
Summary: Sphinx extension for adding asyncio-specific markups

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxcontrib-asyncio
BuildArch: noarch

Source: https://pypi.python.org/packages/03/52/14e11f82a263a6b4c3c66738952f557ee78cde51077cbd949fbf739fa9b4/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %mname.asyncio
%py3_requires %mname

%description
Sphinx extension for adding asyncio-specific markups.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/%mname/*
%exclude %python3_sitelibdir/%mname/__init__.py*
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*
%python3_sitelibdir/*.egg-info

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt4
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3.2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt3
- srpm build

* Sat Sep 24 2016 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt2
- Fixed a conflict with the package python-module-sphinxcontrib.

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for ALT Linux Sisyphus.
