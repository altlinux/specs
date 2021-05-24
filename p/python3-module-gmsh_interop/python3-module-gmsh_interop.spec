%define  modulename gmsh_interop

Name:    python3-module-%modulename
Version: 2018.09.27
Release: alt2

Summary: Interoperability with Gmsh for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/inducer/gmsh_interop

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Mon May 24 2021 Anton Midyukov <antohami@altlinux.org> 2018.09.27-alt2
- rename srpm to python3-module-gmsh_interop
- drop python2 subpackage

* Mon Feb 11 2019 Anton Midyukov <antohami@altlinux.org> 2018.09.27-alt1
- Initial build for Sisyphus
