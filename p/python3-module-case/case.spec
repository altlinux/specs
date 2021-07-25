%define _unpackaged_files_terminate_build 1
%define oname case

Name: python3-module-%oname
Version: 1.5.3
Release: alt2
Summary: Python unittest utilities
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/celery/case

# https://github.com/celery/case.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Python unittest utilities.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.3-alt2
- Drop python2 support.

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.3-alt1
- Updated to upstream version 1.5.3.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.0-alt1
- Initial build for ALT.
