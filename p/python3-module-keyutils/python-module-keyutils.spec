%define oname keyutils

Name: python3-module-%oname
Version: 0.4
Release: alt3

Summary: %oname bindings for Python
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.python.org/pypi/%oname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/d9/76/0e4c11033c1ef297b38b2186097bc8d6433b457c16a34040ec6fc4a273ce/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: libkeyutils-devel
%py3_provides %oname

%description
python-keyutils is a set of python bindings for keyutils, a key management suite
that leverages the infrastructure provided by the Linux kernel for safely
storing and retrieving sensitive infromation in your programs.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.4-alt3
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.4-alt2
- srpm build

* Sun Dec 11 2016 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- new version (0.4) with rpmgs script

* Thu Apr 07 2016 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux Sisyphus.
