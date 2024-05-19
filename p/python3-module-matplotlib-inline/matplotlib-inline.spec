Name: python3-module-matplotlib-inline
Version: 0.1.7
Release: alt1
Summary: Inline Matplotlib backend for IPython and Jupyter
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/matplotlib-inline
VCS: https://github.com/ipython/matplotlib-inline

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Inline Matplotlib backend for IPython and Jupyter

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/matplotlib_inline
%python3_sitelibdir/matplotlib_inline-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.1.7-alt1
- Automatically updated to 0.1.7.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Initial build for ALT.
