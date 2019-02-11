%define  modulename gmsh_interop

Name:    python-module-%modulename
Version: 2018.09.27
Release: alt1

Summary: Interoperability with Gmsh for Python
License: MIT
Group:   Development/Python
URL:     https://github.com/inducer/gmsh_interop

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%description
%summary

%package -n python3-module-%modulename
Summary: Interoperability with Gmsh for Python3
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description -n python3-module-%modulename
%summary

%prep
%setup
rm -fR ../python3-module-%modulename
cp -fR . ../python3-module-%modulename

%build
%python_build
pushd ../python3-module-%modulename
%python3_build
popd

%install
%python_install
pushd ../python3-module-%modulename
%python3_install
popd

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc *.rst

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Mon Feb 11 2019 Anton Midyukov <antohami@altlinux.org> 2018.09.27-alt1
- Initial build for Sisyphus
