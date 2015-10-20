%define scriptpath /usr/lib/systemd/system-shutdown/debug.sh

Name: systemd-shutdown-debug-script
Version: 0.1
Release: alt1

Summary: %scriptpath
License: public domain
Group: System/Configuration/Boot and Init

Url: http://www.freedesktop.org/wiki/Software/systemd/Debugging/#index2h1
BuildArch: noarch

%description
This is the script described at
%url
which should facilitate systemd hangs at shutdown.

%prep

%install
cat >> debug.sh << EOF
#!/bin/sh
mount -o remount,rw /
dmesg > /shutdown-log.txt
mount -o remount,ro /
EOF
install -pDm755 debug.sh %buildroot%scriptpath

%files
%scriptpath

%changelog
* Tue Oct 20 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

