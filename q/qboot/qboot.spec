%global optflags_lto %nil

Name: qboot
Version: 0.0
Release: alt2.gita5300c4949
Summary: A simple x86 firmware that can boot Linux
Group: Emulators
BuildArch: noarch

License: GPL-2.0+
Url: https://github.com/bonzini/qboot
Source: %name-%version.tar
#Patch: %name-%version.patch
ExclusiveArch: %ix86 x86_64

BuildRequires(pre): meson

%description
A simple x86 firmware that can boot Linux.

%prep
%setup
#%patch -p1

%build
%meson
%meson_build

%install
#%%meson_install
mkdir -p %buildroot%_datadir/%name
install -m 0644 %__builddir/bios.bin %buildroot%_datadir/%name/bios.bin
ln -r -s %buildroot%_datadir/%name/bios.bin %buildroot%_datadir/%name/bios-microvm.bin

%files
%doc LICENSE README
%_datadir/%name

%changelog
* Wed Oct 27 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.0-alt2.gita5300c4949
- FTBFS: disable LTO
- update to a5300c4949 from upstream

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.0-alt1.git96842c5a6
- Initial packaging

