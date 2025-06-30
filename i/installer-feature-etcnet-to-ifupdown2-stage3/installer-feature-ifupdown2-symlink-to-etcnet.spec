Name: installer-feature-etcnet-to-ifupdown2-stage3
Version: 0.1
Release: alt1

License: GPL-2.0-or-later
Group: System/Configuration/Other
Summary: Symlinks for compatiblity with installer-network step

BuildArch: noarch
AutoReqProv: no
Requires: alterator-net-ifupdown2

%description
%summary.

%install
mkdir -p %buildroot%_prefix/lib/alterator/backend3 \
	 %buildroot%_prefix/share/alterator/ui

ln -s net-ifupdown2 %buildroot%_prefix/lib/alterator/backend3/net-eth
ln -s net-ifupdown2 %buildroot%_prefix/share/alterator/ui/net-eth

%files
%_prefix/lib/alterator/backend3/net-eth
%_prefix/share/alterator/ui/net-eth

%changelog
* Fri Jun 27 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
