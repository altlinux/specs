%define pip_name rickslab_gpu_utils
%define _unpackaged_files_terminate_build 1

Name: rickslab-gpu-utils
Version: 3.9.0
Release: alt1
License: GPL-3.0-only
Group: System/Configuration/Hardware
Summary: A set of utilities for monitoring and customizing GPU performance
Url: https://github.com/Ricks-Lab/gpu-utils

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

Requires: python3-module-GPUmodules = %EVR

Source: %name-%version.tar

%description
A set of utilities for monitoring GPU performance and modifying control
settings.

In order to get maximum capability of these utilities, you should be running
with a kernel that provides support of the GPUs you have installed. If using
AMD GPUs, installing the latest amdgpu driver or ROCm package, may provide
additional capabilities. If you have Nvidia GPUs installed, you should have
nvidia-smi installed in order for the utility reading of the cards to be
possible.

%package -n python3-module-GPUmodules
Summary: A set of utilities for monitoring and customizing GPU performance
Group: Development/Python3

%description -n python3-module-GPUmodules
Python3 module for %name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%_datadir/%name/doc

%files
%doc LICENSE README.md docs/USER_GUIDE.md
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n python3-module-GPUmodules
%python3_sitelibdir/GPUmodules/
%python3_sitelibdir/%{pip_name}-%version.dist-info/

%changelog
* Wed Feb 25 2026 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt1
- Initial build for ALTLinux.


