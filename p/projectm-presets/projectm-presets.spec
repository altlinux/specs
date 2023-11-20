%define rname projectm
Name: projectm-presets
Version: 3.1.13
Release: alt1

Group: System/Libraries
Summary: Presets for ProjectM
Url: http://projectm.sourceforge.net/
License: LGPL-2.1-or-later

BuildArch: noarch

Requires: projectm-common

Source: %rname-%version.tar

%description
Milkdrop presets for ProjectM.

%prep
%setup -n %rname-%version

%install
mkdir -p %buildroot/%_datadir/projectM/presets/
cp -ar presets/* %buildroot/%_datadir/projectM/presets/
rm -rf %buildroot/%_datadir/projectM/presets/tests
find %buildroot/%_datadir/projectM/presets -type f | \
while read f; do chmod 0644 "$f"; done

%files
%_datadir/projectM/presets/*

%changelog
* Fri Nov 17 2023 Sergey V Turchin <zerg@altlinux.org> 3.1.13-alt1
- initial build
