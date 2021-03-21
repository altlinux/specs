%define systemd_override %_sysconfdir/sysctl.d/90-override.conf

Name: fsprot-control
Version: 1.0
Release: alt1

Summary: Facilities control for shared and mounted partitions
License: GPLv3+
Group: System/Configuration/Other
BuildArch: noarch

Source0: fstab.control
Source1: fsprot.control

Packager: Leonid Krivoshein <klark@altlinux.org>

%description
This package contains control(8) scripts, used for change in /etc/fstab
mounting options, such as exec/noexec, suid/nosuid on separate /tmp and
/home partitions. Also they nesessary for change at the system startup
and on-the-fly sysctl variables fs.protected_*.

%install
:> EMPTYCONF
sed -e 's/ executable / SUID /' \
    -e 's/exec/suid/g' -- %SOURCE0 >suid.control
mkdir -p -m755 -- "%buildroot%_controldir"
sed -E 's,^(FSPART)=.*$,\1=/tmp,' %SOURCE0 >"%buildroot%_controldir/tmpdir"
sed -E 's,^(FSPART)=.*$,\1=/home,' %SOURCE0 >"%buildroot%_controldir/homedir"
sed -E 's,^(FSPART)=.*$,\1=/tmp,' suid.control >"%buildroot%_controldir/tmpsec"
sed -E 's,^(FSPART)=.*$,\1=/home,' suid.control >"%buildroot%_controldir/homesec"
sed -E 's,^(FACILITY_NAME)=.*$,\1=symlinks,' %SOURCE1 >"%buildroot%_controldir/symlinks"
sed -E 's,^(FACILITY_NAME)=.*$,\1=hardlinks,' %SOURCE1 >"%buildroot%_controldir/hardlinks"
install -pD -m644 -- EMPTYCONF "%buildroot%systemd_override"
chmod -- 755 "%buildroot%_controldir"/*

%files
%ghost %config(noreplace) %systemd_override
%config %_controldir/*

%changelog
* Sun Mar 21 2021 Leonid Krivoshein <klark@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

