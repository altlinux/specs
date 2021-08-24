%define _unpackaged_files_terminate_build 1

%define oname threadpoolctl

Name: python3-module-%oname
Version: 2.2.0
Release: alt1
Summary: Thread-pool Controls
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/joblib/threadpoolctl

BuildArch: noarch

# https://github.com/joblib/threadpoolctl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit python3-module-pip
BuildRequires: /usr/bin/py.test3

%description
Python helpers to limit the number of threads used in the threadpool-backed
of common native libraries used for scientific computing and data science
(e.g. BLAS and OpenMP).

Fine control of the underlying thread-pool size can be useful in workloads
that involve nested parallelism so as to mitigate oversubscription issues.

%prep
%setup

%build
flit build

%install
pip%{_python3_version} install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%check
py.test3 -vv

%files
%doc LICENSE
%doc README.md CHANGES.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled tests.

* Sat Jul 17 2021 Michael Shigorin <mike@altlinux.org> 2.1.0-alt2
- added explicit BR: python3-module-pip

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
