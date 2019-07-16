Name:     sandbox
Version:  2.18
Release:  alt1

Summary:  Run programs in a "sandboxed" environment.
License:  GPLv2
Group:    Development/Other
Url:      https://wiki.gentoo.org/wiki/Project:Sandbox

Packager: Nikita Ermakov <arei@altlinux.org>

Source:   %name-%version.tar

BuildRequires: autoconf-archive /proc

%description
Sandbox is a library (and helper utility) to run programs
in a "sandboxed" environment. This is used as a QA measure to try and prevent
applications from modifying files they should not.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/sandbox
%_libdir/libsandbox.so
%_datadir/sandbox/sandbox.bashrc
%_sysconfdir/sandbox.conf
%dir %_sysconfdir/sandbox.d/
%_sysconfdir/sandbox.d/*
%doc INSTALL COPYING README AUTHORS ChangeLog

%changelog
* Tue Jul 16 2019 Nikita Ermakov <arei@altlinux.org> 2.18-alt1
Initial build for ALT Sisyphus.
