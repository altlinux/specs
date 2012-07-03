%define binaries growisofs dvd+rw-format dvd+rw-booktype dvd+rw-mediainfo dvd-ram-control

Name: dvdrwtools-control
Version: 1.2
Release: alt2

Summary: Facilities control for DVD+RW/+R/-R/-RW media tools
License: GPL
Group: System/Servers
BuildArch: noarch

PreReq: control
Conflicts: dvd+rw-tools < 5.17.4.8.6-alt5

Source: dvdrwtools.control

%description
This package contains control rules for DVD+RW/+R/-R/-RW media tools.
See control(8) for details.

%install
for n in %binaries; do
	%__install -pD -m755 %SOURCE0 "$RPM_BUILD_ROOT%_controldir/$n"
	%__subst -p "s/@NAME@/$n/" "$RPM_BUILD_ROOT%_controldir/$n"
done

%files
%config %_controldir/*

%changelog
* Sat Feb 25 2006 LAKostis <lakostis at altlinux.ru> 1.2-alt2
- remove suid from public mode and move old rights 
  to legacy mode.

* Mon Apr 25 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.2-alt1
- added dvd+rw-mediainfo, dvd-ram-control

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help.

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
