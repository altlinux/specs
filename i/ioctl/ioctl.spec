Name:           ioctl
Version:        0.4
Release:        alt1
License:        GPLv2+
URL:            https://github.com/jerome-pouiller/ioctl
Summary:        The missing tool to call arbitrary ioctl on devices
Group:          System/Base
Patch:          0001-Sync-May-17-2022.patch
Patch1:         0002-stdin.patch
Patch2:         0001-Powerpc-termios2.patch
Source:         %name-%version.tar.gz

%description
The missing tool to call arbitrary ioctl on devices.

Since most data associated with ioctls are not human readable, this tool
is intended for driver developers who want to do quick tests on their
drivers.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

%build
make

%install
install -D %name %buildroot%_bindir/%name

%files
%doc *.md
%_bindir/*

%changelog
* Sun Feb 25 2024 Fr. Br. George <george@altlinux.org> 0.4-alt1
- Initial build for ALT
- Provide ioctl() on already opened device
