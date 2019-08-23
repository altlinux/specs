Name: rpi-firmware
Version: 0.1
Release: alt1
Group: System/Base
Summary: Raspberry Pi firmware blobs
License: Redistributable
URL: https://github.com/raspberrypi/firmware
Source0: %name-%version.tar.xz
BuildArch: noarch
# most build environments would safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%add_verify_elf_skiplist %_datadir/%name/*
%add_findreq_skiplist %_datadir/%name/*


%description
%summary for booting Linux kernel


%prep
%setup


%install
rm -rf -- %buildroot
umask 022
mkdir -pm755 \
  %buildroot%_datadir/%name
cp -a boot extra %buildroot%_datadir/%name/
chmod a+rX %buildroot%_datadir/%name


%files
%_datadir/%name/*


%changelog
* Fri Aug 23 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- cloned, cleaned, packaged
