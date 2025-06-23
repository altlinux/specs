Name: livecd-alt-metadata
Version: 0.0.1
Release: alt1

Summary: Create and mount alt-metadata partition
License: GPL-3.0-or-later
Group: System/Configuration/Other

URL: https://www.altlinux.org/LiveCD

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%build

%install
install -Dpm755 livecd-alt-metadata.sh \
	%buildroot%_prefix/libexec/livecd-alt-metadata
install -Dpm644 livecd-alt-metadata.service \
	%buildroot/lib/systemd/system/livecd-alt-metadata.service

%files
%_prefix/libexec/livecd-alt-metadata
/lib/systemd/system/livecd-alt-metadata.service

%changelog
* Sun Jun 22 2025 Anton Midyukov <antohami@altlinux.org> 0.0.1-alt1
- Initial build.
