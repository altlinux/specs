%define systemdtmpfiles /sbin/systemd-tmpfiles

Name: sysvinit-tmpfiles
Version: 1.0
Release: alt1

Summary: Support tmpfiles.d for System V init tools
Group: System/Configuration/Boot and Init
License: %lgpl21plus
BuildArch: noarch

Source2: tmpfiles.cron.daily.in

BuildRequires(pre): rpm-build-licenses

Requires: %systemdtmpfiles
Requires: startup >= 0.9.9.0-alt1

%description
This package containing support for System V init tools,
automatically creating, deleting and cleaning up volatile
and temporary files and directories, based on the configuration
file format and location specified in tmpfiles.d.

When using the systemd this package not need it.

%prep
%setup -cT
cat > configure.sed <<EOF
#! /bin/sed -f

s@%%systemdtmpfiles@%systemdtmpfiles@g
EOF
chmod 755 configure.sed

%build
./configure.sed %SOURCE2 > tmpfiles.cron.daily

%install
install -pD -m755 tmpfiles.cron.daily %buildroot%_sysconfdir/cron.daily/tmpfiles

%files
%_sysconfdir/cron.daily/tmpfiles

%changelog
* Fri Feb 19 2016 Aleksey Avdeev <solo@altlinux.ru> 1.0-alt1
- Remove tmpfiles init script (is old)

* Wed Feb 10 2016 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux (ALT#31718)
