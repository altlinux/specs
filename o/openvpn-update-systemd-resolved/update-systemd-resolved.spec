
%define oname update-systemd-resolved
%define _unpackaged_files_terminate_build 1

%define _customdocdir %_defaultdocdir/%name
%define _libexecdir %_prefix/libexec

Name:    openvpn-%oname
Version: 1.3.0
Release: alt1.git17417199

BuildArch: noarch

Summary: Integrate OpenVPN with systemd-resolved
License: GPL-3.0-or-later
Group:   Networking/Other
Url:     https://github.com/jonathanio/update-systemd-resolved

# This package needs openvpn user
Requires(pre): openvpn

%filter_from_requires '/^info$/d'
%filter_from_requires '/^jq$/d'
%filter_from_requires '/^perl-base$/d'
%filter_from_requires '/^python3$/d'

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %oname-%version-%release.tar

# Tests, like most shell scripts, need /dev/fd
BuildRequires: /proc

%description
This is a helper script designed to integrate OpenVPN with the
systemd-resolved service via DBus instead of trying to override
/etc/resolv.conf, or manipulate systemd-networkd configuration
files.

Since systemd-229, the systemd-resolved service has an API
available via DBus which allows directly setting the DNS
configuration for a link. This script makes use of busctl from
systemd to send DBus messages to systemd-resolved to update the DNS
for the link created by OpenVPN.

%prep
%setup -n %oname-%version-%release

# use correct python executable
sed -i 's,\bpython[[:space:]]\+-c,python3 -c,g' \
  update-systemd-resolved

# use system path in documentation
sed -i 's,/usr/local/libexec/,%_libexecdir/,g' \
  update-systemd-resolved \
  update-systemd-resolved.conf \
  README.md

%install
%makeinstall_std PREFIX=%_prefix
rm -rf %buildroot%_defaultdocdir

%check
%make_build test

%files
%doc README.md CHANGELOG.md update-systemd-resolved.conf
%dir %_libexecdir/openvpn
%attr(0750,root,openvpn) %_libexecdir/openvpn/%oname
%_datadir/polkit-1/rules.d/*.rules

%changelog
* Tue Jun 25 2024 Ivan A. Melnikov <iv@altlinux.org> 1.3.0-alt1.git17417199
- Initial build for Sisyphus
