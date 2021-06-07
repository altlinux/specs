%define _unpackaged_files_terminate_build 1

%define oname check-manifest

Name: python3-module-%oname
Version: 0.37
Release: alt2
Summary: Check MANIFEST.in in a Python source package for completeness
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/check-manifest
BuildArch: noarch

# https://github.com/mgedmin/check-manifest.git
Source: %name-%version.tar

BuildRequires: git-core
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(mock)

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
Are you a Python developer?
Have you uploaded packages to the Python Package Index?
Have you accidentally uploaded broken packages with some files missing?
If so, check-manifest is for you.

%prep
%setup

%build
%python3_build

%install
%python3_build_install

%check
export LC_ALL=en_US.UTF-8
sed -i -e "s|python='python'|python='python3'|g" tests.py
python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.37-alt2
- Drop python2 support.

* Fri Sep 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.37-alt1
- Updated to upstream version 0.37.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36-alt1
- Initial build for ALT.
