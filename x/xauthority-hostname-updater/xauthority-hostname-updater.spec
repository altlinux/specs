%define _unpackaged_files_terminate_build 1

#%%def_enable debug_output

Name: xauthority-hostname-updater
Version: 0.4
Release: alt1

Summary: Daemon that keeps hostname in the Xauthority files up-to-date
Group: System/X11
License: GPLv3

Source: %name-%version.tar

BuildRequires: gcc
BuildRequires: libsystemd-devel
BuildRequires: libXau-devel libX11-devel
BuildRequires: txt2man

%description
xauthority-hostname-updater watches org.freedesktop.hostname1 for hostname
changes, and update hostnames in Xauthority files for all active displays.

%prep
%setup

%build
gcc \
    ${CFLAGS:-%optflags} \
    %{?_enable_debug_output:-DENABLE_DEBUG_OUTPUT} \
    %name.c \
    -lsystemd -lXau -lX11 \
    -o %name

sed "s|@NAME@|%name|g;s|@BIN_PATH@|%_bindir/%name|g" man8.in | \
    txt2man -t %name | xz > %name.8.xz

cat > 60-start-%name.sh <<EOF
#!/bin/sh

exec %_bindir/%name -d
EOF

%install
install -m 755 -d %buildroot%_bindir/
cp %name %buildroot/%_bindir/

install -m 755 -d %buildroot%_x11sysconfdir/xinit.d/
install -m 755 60-start-%name.sh %buildroot%_x11sysconfdir/xinit.d/

install -m 755 -d %buildroot%_man8dir/
install -m 644 %name.8.xz %buildroot%_man8dir/

%files
%_x11sysconfdir/xinit.d/*
%_bindir/*
%_man8dir/*

%changelog
* Tue Feb 08 2022 Slava Aseev <ptrnine@altlinux.org> 0.4-alt1
- Daemonize properly (thx zerg@)

* Mon Jan 17 2022 Slava Aseev <ptrnine@altlinux.org> 0.3-alt1
- Fix build with glibc < 2.32 (thx ilyakurdyukov@)

* Thu Dec 23 2021 Slava Aseev <ptrnine@altlinux.org> 0.2-alt1
- Shutdown gracefully on SIGHUP
- Do not become "zombie" after external kill signal

* Tue Dec 14 2021 Slava Aseev <ptrnine@altlinux.org> 0.1-alt1
- Initial build for ALT

