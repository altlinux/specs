%define oname multidict

%def_with check

Name: python3-module-%oname
Version: 6.0.3
Release: alt1

Summary: Multidicts are useful for working with HTTP headers, URL query args etc

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/multidict
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

%description
HTTP Headers and URL query string require specific data structure: multidict.
It behaves mostly like a dict but it can have several values for the same key.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -vf %buildroot%python3_sitelibdir/%oname/*.{c,pyx}

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sun Dec 04 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.3-alt1
- Automatically updated to 6.0.3.

* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.2-alt1
- Automatically updated to 6.0.2.
- Build with check.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 4.5.2-alt2
- Rename package.
- Fix license.

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 4.5.2-alt1
- New version 4.5.2
- switch to git

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.3-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- New version 3.1.3

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt1
- New version 2.1.4

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux Sisyphus.
