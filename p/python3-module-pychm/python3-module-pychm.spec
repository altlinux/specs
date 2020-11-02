%define  modulename chm

Name:    python3-module-pychm
Version: 0.8.6
Release: alt1

Summary: Python bindings for CHMLIB
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/dottedmag/pychm

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: libchm-devel

Source: pychm-%version.tar

%description
%summary

%prep
%setup -n pychm-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc AUTHORS NEWS README

%changelog
* Mon Nov 02 2020 Anton Midyukov <antohami@altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus
