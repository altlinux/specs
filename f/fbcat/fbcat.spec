%define _unpackaged_files_terminate_build 1

Name: fbcat
Version: 0.5.2
Release: alt3
Summary: Framebuffer grabber
License:  GPL-2.0
Group: Terminals
Url: https://github.com/jwilk/fbcat

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Conflicts: fbgrab

%description
Fbcat takes a screenshot using the Linux framebuffer device.

%prep
%setup
%patch -p1
sed -i 's|/usr/local|%prefix|g' Makefile

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Wed Jul 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.2-alt3
- Update based on upstream.

* Tue Jul 22 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.2-alt2
-  Add Conflicts: fbgrab due to file overlap on /usr/bin/fbgrab.

* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 0.5.2-alt1
- initial build for Sisyphus
