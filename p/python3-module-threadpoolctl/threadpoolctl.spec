%define _unpackaged_files_terminate_build 1

%define oname threadpoolctl

Name: python3-module-%oname
Version: 2.1.0
Release: alt1
Summary: Thread-pool Controls
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/joblib/threadpoolctl

BuildArch: noarch

# https://github.com/joblib/threadpoolctl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

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

%files
%doc LICENSE
%doc README.md CHANGES.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
