%define _unpackaged_files_terminate_build 1

Name: drinfo
Version: 1.2.0
Release: alt1
Summary: A Linux CLI tool for physical and network drive information.
License: MIT
Group: Monitoring
Url: https://github.com/Lennart1978/drinfo

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

%description
A lightweight command-line tool to monitor disk usage on Linux systems with
beautiful colored progress bars.

%prep
%setup
%patch -p1
sed -i 's|/usr/local|%prefix|g' Makefile

%make
%make_build

%install
mkdir -p %buildroot%_bindir
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_man1dir
install -Dm644 %name.1* %buildroot/%_man1dir

%files
%doc README.md LICENSE
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.2.0-alt1
- 1.0.4 -> 1.2.0

* Sun Jul 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.4-alt1
- 1.0.2 -> 1.0.4

* Wed Jul 2 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
