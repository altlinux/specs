%define _unpackaged_files_terminate_build 1
%define   oname wavemon

Name:   %oname
Version: 0.9.6
Release: alt2

Summary: ncurses-based monitoring application for wireless network devices on Linux.

License: GPL-3.0-or-later
Group:   Networking/Other
VCS:     https://github.com/uoaerg/wavemon

Source:  %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: libnl-devel

%description
wavemon is a wireless device monitoring application that allows
you to watchsignal and noise levels, packet statistics, device
configuration and network parameters of your wireless network
hardware. It should work (though with varying features) with
all devices supported by the Linux kernel.


%prep
%setup

%build
sed -i '/$(INSTALL) -m 0755 -d $(DESTDIR)$(datadir)/d'      Makefile.in
sed -i '/$(INSTALL) -m 0644 $(DOCS) $(DESTDIR)$(datadir)/d' Makefile.in
%autoreconf
%configure
unset CFLAGS
%make_build

%install
%makeinstall_std


%files
%doc  LICENSE  README.md
%_bindir/%oname
%_man1dir/*
%_man5dir/*


%changelog
* Mon Apr 28 2025 Yaroslav Karpov <hellkar@altlinux.org> 0.9.6-alt2
- dependencies cleanup

* Sun Apr 27 2025 Yaroslav Karpov <hellkar@altlinux.org> 0.9.6-alt1
- updated to 0.9.6 version
- spec cleanup

* Wed Nov 15 2023 Yaroslav Karpov <hellkar@altlinux.org> 0.9.5-alt1
- initial build for ALT

