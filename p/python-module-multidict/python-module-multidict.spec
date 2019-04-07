%define oname multidict

Name: python-module-%oname
Version: 4.5.2
Release: alt1
Summary: Multidicts are useful for working with HTTP headers, URL query args etc

License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/multidict
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-Cython

%description
HTTP Headers and URL query string require specific data structure: multidict.
It behaves mostly like a dict but it can have several values for the same key.

%package -n python3-module-%oname
Summary: Multidicts are useful for working with HTTP headers, URL query args etc
Group: Development/Python

%description -n python3-module-%oname
HTTP Headers and URL query string require specific data structure: multidict.
It behaves mostly like a dict but it can have several values for the same key.
Python 3 version.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
rm -vf %buildroot%python3_sitelibdir/%oname/*.{c,pyx}

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
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
