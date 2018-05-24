Name: dm-secdel
Version: 1.0.0
Release: alt1

Summary: dm-linear with secure deletion on discard
License: GPLv2
Group: System/Kernel and hardware

Url: https://github.com/vt-alt/dm-secdel
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
Linear device-mapper target with secure deletion on discard.

%package -n kernel-source-%name
Summary: dm-linear with secure deletion on discard (source)
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Linear device-mapper target with secure deletion on discard (source).

%prep
%setup -q

%build

%install
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%changelog
* Thu May 24 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- Package for ALT.
