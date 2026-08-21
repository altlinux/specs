Name:    simagic-ff
Version: 2.0.0
Release: alt1

Summary: Force feedback support on Simagic steering wheels (post firmware v159)
License: GPL-2.0
Group:   System/Configuration/Hardware
URL:     https://github.com/JacKeTUs/simagic-ff

Source: %name-%version.tar

BuildArch: noarch

Requires: dkms-%name = %EVR

%description
Force feedback support on Simagic steering wheels (post firmware v159).

%package -n dkms-%name
Summary: DKMS module sources for %name
Group: System/Configuration/Hardware
Requires: dkms
BuildArch: noarch

%description -n dkms-%name
%summary

%prep
%setup

%build

%install
install -dm755 %buildroot%_usrsrc/%name-%version
install -m644 Kbuild Makefile dkms.conf \
    hid-simagic.c hid-simagic.h \
    hid-simagic-settings.c hid-simagic-settings.h \
    hid-simagic-sysfs.c hid-simagic-sysfs.h \
    %buildroot%_usrsrc/%name-%version/

# %files
# %doc LICENSE README.md

%files -n dkms-%name
%_usrsrc/%name-%version/

%changelog
* Fri Aug 21 2026 Sergey Palcheh <minergenon@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
