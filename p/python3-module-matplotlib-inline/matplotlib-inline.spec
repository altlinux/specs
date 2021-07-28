%define _unpackaged_files_terminate_build 1

Name: python3-module-matplotlib-inline
Version: 0.1.2
Release: alt1
Summary: Inline Matplotlib backend for IPython and Jupyter
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/ipython/matplotlib-inline

BuildArch: noarch

# https://github.com/ipython/matplotlib-inline.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Inline Matplotlib backend for IPython and Jupyter

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/matplotlib_inline
%python3_sitelibdir/matplotlib_inline-%version-py%{_python3_version}.egg-info

%changelog
* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Initial build for ALT.
