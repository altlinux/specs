%define  oname mitogen

Name:    python3-module-%oname
Version: 0.2.8
Release: alt1

Summary: Distributed self-replicating programs in Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/dw/mitogen

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: %oname-%version.tar

Patch: remove-compat.patch

%description
%summary

%prep
%setup -n %oname-%version
%patch -p1
rm -r mitogen/compat ansible_mitogen/compat

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/ansible_%oname
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus.
