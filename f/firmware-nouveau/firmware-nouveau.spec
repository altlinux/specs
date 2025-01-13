%define _firmwaredir /lib/firmware

Name: firmware-nouveau
Version: 340.108
Release: alt2

Summary: This package provides video & pgraph firmwares for all NVIDIA chipsets that need them
License: NVIDIA
Group: System/Kernel and hardware

BuildArch: noarch

Url: https://nouveau.freedesktop.org/VideoAcceleration.html#firmware
# Source-url: https://github.com/envytools/firmware.git
Source: envytools-extractor.tar

#http://us.download.nvidia.com/XFree86/Linux-x86_64/340.108/NVIDIA-Linux-x86_64-340.108.run
Source1: NVIDIA-Linux-x86_64-340.108.run

#http://us.download.nvidia.com/XFree86/Linux-x86_64/325.15/NVIDIA-Linux-x86_64-325.15.run
Source2: NVIDIA-Linux-x86_64-325.15.run

BuildRequires: %_bindir/python3

%description
%summary

%prep
%setup -n envytools-extractor

%build
sh %SOURCE1 --extract-only
sh %SOURCE2 --extract-only
python3 extract_firmware.py
mkdir -p firmware
mv nv* vuc* firmware/
mv NVIDIA-Linux-x86_64-325.15/README.txt README.NVIDIA-325.15.txt
mv NVIDIA-Linux-x86_64-340.108/README.txt README.NVIDIA-340.108.txt

%install
mkdir -p %buildroot%_firmwaredir/nouveau
cp -v firmware/* %buildroot%_firmwaredir/nouveau

%files
# NVIDIA-Linux-x86_64-340.108/LICENSE same file
%doc NVIDIA-Linux-x86_64-325.15/LICENSE
%doc README.NVIDIA-325.15.txt README.NVIDIA-340.108.txt
%_firmwaredir/nouveau/

%changelog
* Sat Jan 11 2025 Boris Yumankulov <boria138@altlinux.org> 340.108-alt2
- Add NVIDIA license file (ALT bug: 52669)
- Add NVIDIA README files

* Sat Jul 06 2024 Boris Yumankulov <boria138@altlinux.org> 340.108-alt1
- initial build for ALT Sisyphus (ALT bug: 50851)

