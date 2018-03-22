%def_with python3

%define oname keyutils

Name: python-module-%oname
Version: 0.4
Release: alt2.1

Summary: %oname bindings for Python
License: ASL 2.0
Group: Development/Python

%setup_python_module %oname

Url: https://pypi.python.org/pypi/%oname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/d9/76/0e4c11033c1ef297b38b2186097bc8d6433b457c16a34040ec6fc4a273ce/%oname-%version.tar.gz

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools libkeyutils-devel
%py_provides %oname

%description
python-keyutils is a set of python bindings for keyutils, a key management suite
that leverages the infrastructure provided by the Linux kernel for safely
storing and retrieving sensitive infromation in your programs.

%if_with python3
%package -n python3-module-%oname
Summary: %oname bindings for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
python-keyutils is a set of python bindings for keyutils, a key management suite
that leverages the infrastructure provided by the Linux kernel for safely
storing and retrieving sensitive infromation in your programs.
%endif

%prep
%setup -n %oname-%version

%if_with python3
rm -fR ../python3-module-%oname
cp -fR . ../python3-module-%oname
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%oname
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname
%python3_install
popd
%endif

%files
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.4-alt2
- srpm build

* Sun Dec 11 2016 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- new version (0.4) with rpmgs script

* Thu Apr 07 2016 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux Sisyphus.
