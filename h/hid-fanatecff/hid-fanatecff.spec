Name:    hid-fanatecff
Version: 0.2.3
Release: alt1

Summary: Linux kernel module for FANATEC wheels
License: GPL-2.0-only
Group:   System/Configuration/Hardware
URL:     https://github.com/gotzl/hid-fanatecff

Source:  %name-%version.tar

Requires: dkms-%name = %EVR
Requires: joyutils

BuildArch: noarch

%description
Driver to support FANATEC input devices, in particular ForceFeedback
of various wheel-bases. The hid-fanatec kernel module is built and
installed via DKMS.

%package -n dkms-%name
Summary: %name DKMS package
Group:   System/Configuration/Hardware
Requires: dkms

%description -n dkms-%name
%summary

%prep
%setup
# dkms.conf carries a #VERSION# placeholder, keep it in sync
sed -e 's/^PACKAGE_VERSION=.*/PACKAGE_VERSION="%version"/' -i dkms.conf

%build

%install
install -dm755 %buildroot%_usrsrc/hid-fanatec-%version

install -m644 dkms.conf Kbuild Makefile \
	hid-ftec.c hid-ftec.h hid-ftec-pid.h hid-ftecff.c hid-ftecff-tuning.c \
	%buildroot%_usrsrc/hid-fanatec-%version/

install -Dm644 fanatec.rules %buildroot%_udevrulesdir/99-fanatec.rules

%files
%doc LICENSE README.md
%_udevrulesdir/99-fanatec.rules

%files -n dkms-%name
%_usrsrc/hid-fanatec-%version/

%changelog
* Tue Aug 04 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
