%def_with python3

%define oname fusepy

Name: python-module-%oname
Version: 2.0.4
Release: alt2

Summary: %oname bindings for Python
License: ISC
Group: Development/Python

Url: https://pypi.python.org/pypi/%oname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/70/aa/959d781b7ac979af1a9fbea0faffe06677c390907b56b8ce024eb9320451/%oname-%version.tar.gz

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools
%py_provides %oname
Conflicts: python3-module-fuse

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 2.0.4-alt2
- srpm build

* Fri Apr 15 2016 Anton Midyukov <antohami@altlinux.org> 2.0.4-alt1
- Initial build for Alt Linux Sisyphus.
