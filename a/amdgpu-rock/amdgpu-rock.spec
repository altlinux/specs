%define src_dir %_usrsrc/%name-%version

Name: amdgpu-rock
Version: 6.3.6
Release: alt1

Summary: AMDGPU Driver with KFD used by the ROCm project

License: GPL-2.0
Group: System/Configuration/Hardware
Url: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver

Source0: %name-%version.tar

Requires: dkms-%name = %EVR

BuildArch: noarch

%description
AMDGPU Driver with KFD used by the ROCm project.

Compatible kernels versions: everything <= 6.5

%package -n dkms-%name
Summary: %name DKMS package
Group: System/Configuration/Hardware
Requires: dkms
BuildArch: noarch

%description -n dkms-%name
%summary

%prep
%setup

find . -type f \( -name dkms.conf -o -name '*.c' \) -exec sed -i "s/#VERSION#/%version/" {} +

%build

%install
install -Dm 644 install/modprobe.conf %buildroot/etc/modprobe.d/%name-blacklist.conf

mkdir -p %buildroot%src_dir
cp -rv . %buildroot%src_dir

%files
/etc/modprobe.d/%name-blacklist.conf

%files -n dkms-%name
%src_dir/

%changelog
* Mon Jan 01 2024 L.A. Kostis <lakostis@altlinux.ru> 6.3.6-alt1
- Initial build for ALTLinux.
- Use sources from roc-6.0.x branch (tag: rocm-6.0.0).
