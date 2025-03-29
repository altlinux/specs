%define _unpackaged_files_terminate_build 1

Name: udisks-indicator
Version: 2.0
Release: alt1

Summary: Udisks Indicator to show disk usage
License: MIT
Group: System/Kernel and hardware
URL: https://github.com/SergKolo/udisks-indicator

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

Requires: typelib(AyatanaAppIndicator3)
Requires: typelib(Notify)
Requires: /usr/bin/gnome-disks

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
This indicator allows easily view information about your mounted 
partitions.

Entries are organized in order:
* Partition;
* Alias (if set by user);
* Disk Drive to which partition belongs;
* Mountpoint of the partition (directory);
* Filesystem type;
* Usage in percent and human readable format;
* Usage bar.

Preferences dialog allows removing Alias, Disk, Mountpoint and
Filesystem fields. Since the original purpose of this indicator was to
display partition usage information, Partition, Usage and Usage Bar are
kept and non-removable

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
mkdir -p %{buildroot}%{_bindir}
cp -pv udisks-indicator %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_desktopdir}
cp -pv udisks-indicator.desktop %{buildroot}%{_desktopdir}/

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop

%changelog
* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 2.0-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
