# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global import_path github.com/OpenPrinting/ipp-usb
Name:    ipp-usb
Version: 0.9.23
Release: alt2

Summary: ipp-usb -- HTTP reverse proxy, backed by IPP-over-USB connection to device
License: BSD-2-Clause
Group:   System/Servers
Url:     https://github.com/OpenPrinting/ipp-usb

Source: %name-%version.tar
Patch:  %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(avahi-client)

%description
%summary.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

#%%golang_install

install -m 0755 -vd                        %buildroot%_sbindir
install -m 0755 -vp .build/bin/*           %buildroot%_sbindir/
install -m 0755 -vd                        %buildroot%_udevrulesdir
install -m 0644 -vp systemd-udev/*.rules   %buildroot%_udevrulesdir
install -m 0755 -vd                        %buildroot%_unitdir
install -m 0644 -vp systemd-udev/*.service %buildroot%_unitdir
install -m 0755 -vd                        %buildroot%_sysconfdir/ipp-usb
install -m 0644 -vp ipp-usb.conf           %buildroot%_sysconfdir/ipp-usb/
install -m 0755 -vd                        %buildroot%_sysconfdir/ipp-usb/quirks
install -m 0755 -vd                        %buildroot%_mandir/man8
install -m 0644 -vp ipp-usb.8              %buildroot%_mandir/man8
install -m 0755 -vd %buildroot%_datadir/ipp-usb
install -m 0755 -vd %buildroot%_datadir/ipp-usb/quirks
install -m 0644 -vp ipp-usb-quirks/* %buildroot%_datadir/ipp-usb/quirks

%files
%doc *.md
%_sbindir/ipp-usb
%dir %_datadir/ipp-usb
%dir %_datadir/ipp-usb/quirks
%_datadir/ipp-usb/quirks/*
%_man8dir/ipp-usb.8.*
%dir %_sysconfdir/ipp-usb/
%config(noreplace) %_sysconfdir/ipp-usb/ipp-usb.conf
%dir %_sysconfdir/ipp-usb/quirks
%_udevrulesdir/*.rules
%_unitdir/*.service

%changelog
* Fri Oct 20 2023 Anton Midyukov <antohami@altlinux.org> 0.9.23-alt2
- Add systemd units and config (Closes: 46497)
- ipp-usb.service: fix path in ExecStart
- Cleanup Packager
- Change Group: System/Servers

* Sun Feb 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.23-alt1
- Initial build for Sisyphus
