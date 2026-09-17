%define _unpackaged_files_terminate_build 1

Name: tzdata-zonetab-legacy
Version: 2024a
Release: alt1

Summary: Deprecated timezone data for compatibility
License: GPLv2+
Group: System/Base
URL: https://www.iana.org/time-zones
VCS: https://github.com/eggert/tz.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: tzdata-source = %EVR

%description
%summary.

%prep
%setup

%install
install -D -m 644 /usr/src/tzdata/zone.tab %buildroot%_datadir/zoneinfo/zone.tab

%files
%_datadir/zoneinfo/zone.tab

%changelog
* Wed Sep 16 2026 Vladimir Romanov <rirusha@altlinux.org> 2024a-alt1
- Initial build.
