%define oname yarl

Name: python-module-%oname
Version: 0.11.0
Release: alt1.1
Summary: Yet another URL library http://yarl.readthedocs.io
License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname

Source: %oname-%version.tar.gz
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-pytest-runner python3-module-multidict

%description
The module provides handy URL class for url parsing and changing.

%package -n python3-module-%oname
Summary: Yet another URL library http://yarl.readthedocs.io
Group: Development/Python3

%description -n python3-module-%oname
The module provides handy URL class for url parsing and changing.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

#check
#python3 setup.py test

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1
- New version 0.11.0

* Mon May 8 2017 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus.
