%define _unpackaged_files_terminate_build 1

Name: iwd
Version: 3.12
Release: alt2

Summary: Wireless daemon with optimized resource use and minimal dependencies
License: LGPL-2.1-or-later
Group: Security/Networking
Url: https://iwd.wiki.kernel.org/
Vcs: https://git.kernel.org/pub/scm/network/wireless/iwd.git

Source: %name-%version.tar
Source1: useful.h
Source2: asn1-private.h

BuildRequires: gcc
BuildRequires: libreadline-devel
BuildRequires: libell-devel
BuildRequires: openssl
BuildRequires: python3-module-docutils
BuildRequires: libdbus-devel
BuildRequires: libsystemd-devel

%description
iNet Wireless Daemon - wireless daemon by Intel. Main goal of the project is to
optimize resource utilization by minimizing external dependencies and instead
using only features provided by the Linux kernel.

%prep
%setup
# Two headers from ell are vendored here. Upstream states that those are special
# headers shared only between ell and iwd, and not available as part of public
# API. See:
# https://lore.kernel.org/ell/14a637ae-0f31-4429-963a-5f5012841ee0@gmail.com/
# https://lore.kernel.org/iwd/CF2B2F74-37AB-4BA6-B1B5-6E71D898A0C3@holtmann.org/
mkdir -p ell/
cp %SOURCE1 ell/
cp %SOURCE2 ell/

%build
./bootstrap
./configure \
  --enable-maintainer-mode \
  --enable-debug \
  --prefix=/usr \
  --localstatedir=/var \
  --enable-wired \
  --enable-hwsim \
  --enable-tools \
  --enable-ofono \
  --enable-external-ell \
  --enable-dbus-policy \
  --enable-systemd-service \
  #

%make_build

%install
%makeinstall_std

%check
# Runs files in unit folder that start with "test" and have no extension.
# I.e. executable test files.
cd unit
for test in test-*; do
[ "${test##*/}" = "${test%%.*}" ] || continue
./"$test"
done

%files
%_bindir/hwsim
%_bindir/iwctl
%_bindir/iwmon
%_prefix/libexec/ead
%_prefix/libexec/iwd
%_man1dir/*.1*
%_man5dir/iwd*.5*
%_man7dir/*.7*
%_man8dir/*.8*
%_unitdir/ead.service
%_unitdir/iwd.service
%_modules_loaddir/pkcs8.conf
%_systemd_dir/network/80-iwd.link
%_datadir/dbus-1/system-services/net.connman.ead.service
%_datadir/dbus-1/system-services/net.connman.iwd.service
%_datadir/dbus-1/system.d/ead-dbus.conf
%_datadir/dbus-1/system.d/hwsim-dbus.conf
%_datadir/dbus-1/system.d/iwd-dbus.conf

%changelog
* Thu Jun 25 2026 Pavel Petrykin <silverducks@altlinux.org> 3.12-alt2
- Reenable iwd interface management (Closes: 59562).

* Tue Mar 17 2026 Pavel Petrykin <silverducks@altlinux.org> 3.12-alt1
- Initial build for Alt Linux.
