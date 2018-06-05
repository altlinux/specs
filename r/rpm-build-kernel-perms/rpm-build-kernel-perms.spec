Name: rpm-build-kernel-perms
Version: 1.0
Release: alt1

Summary: RPM helper to fix permissions for kernel and modules
License: GPL
Group: Development/Other

BuildArch: noarch

%description
RPM helper to make kernel and modules readable by user.

%files

%pre
[ -d /.host -a -d /.in -a -d /.out ]

%post
(
  find /boot -name 'System.map*' -print0
  find /boot -name 'vmlinu*'  -print0
  find /lib/modules -type f -print0
  find /bin/*mount -print0
) | xargs -0r chmod a+r
(
  find /lib/modules -type d -print0 
) | xargs -0r chmod a+rx
chmod a+rx /boot
chmod a+rwx /lib/modules/*/

%changelog
* Tue Jun 05 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1
- First version.
