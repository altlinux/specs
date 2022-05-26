%define _unpackaged_files_terminate_build 1

Name: python3-module-treelib
%define treelib_version 1.6.1
Version: %treelib_version
Release: alt1

Summary: Tree implementation in python.
License: %asl
Group: Development/Python
BuildArch: noarch

Url: http://treelib.readthedocs.io/en/latest/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/treelib-%treelib_version-py*.egg-info/
%python3_sitelibdir_noarch/treelib/
%doc HISTORY
%doc PKG-INFO
%doc LICENSE



%changelog
* Wed May 04 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
