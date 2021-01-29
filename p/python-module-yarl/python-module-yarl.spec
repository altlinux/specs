%define oname yarl

Name: python-module-%oname
Version: 1.6.3
Release: alt1
Summary: Yet another URL library http://yarl.readthedocs.io
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/yarl

Source: %oname-%version.tar

%description
The module provides handy URL class for url parsing and changing.

%package -n python3-module-%oname
Summary: Yet another URL library http://yarl.readthedocs.io
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython

%description -n python3-module-%oname
The module provides handy URL class for url parsing and changing.

%prep
%setup -n %oname-%version

%build
python3 -mcython -3 -o yarl/_quoting_c.c yarl/_quoting_c.pyx
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- 1.4.2 released

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0
- switch to git

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar at altlinux.org> 0.11.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev at altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1
- New version 0.11.0

* Mon May 8 2017 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus.
