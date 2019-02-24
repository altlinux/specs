Name: arm-rootfs-installer
Version: 0.1
Release: alt1
Summary: Installer rootfs archive to any specified block device
License: GPLv2+
Group: System/Configuration/Other
Url:  https://git.altlinux.org/people/antohami/packages/arm-rootfs-installer.git
BuildArch: noarch
Source0: %name-%version.tar

%description
Allows one to first select a source rootfs archive installer. The rootfs must be
containing File Systems with u-boot for target board.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -d %buildroot%_datadir/%name/socs.d
install -pm 644 socs.d/* %buildroot%_datadir/%name/socs.d/
install -d %buildroot%_datadir/%name/boards.d
install -pm 644 boards.d/* %buildroot%_datadir/%name/boards.d/

install -d %buildroot%_bindir
install -pm 0755 %name %buildroot%_bindir/

install -d %buildroot%_docdir/%name
install -pm 644 AUTHORS COPYING README SUPPORTED-BOARDS \
        %buildroot%_docdir/%name

%files
%doc %_docdir/%name
%_bindir/%name
%_datadir/%name/

%changelog
* Sun Feb 24 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build

