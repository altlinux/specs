%define _unpackaged_files_terminate_build 1
%define oname nose_warnings_filters

Name: python3-module-%oname
Version: 0.1.5
Release: alt2
Summary: Allow to inject warning filters during ``nosetest``.
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose_warnings_filters

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%description
Allow to inject warning filters during ``nosetest``.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt2
- Drop python2 support.

* Wed Nov 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt1
- Initial build for ALT.
