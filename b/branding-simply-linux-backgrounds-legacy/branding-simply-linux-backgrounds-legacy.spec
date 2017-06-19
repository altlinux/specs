Name: branding-simply-linux-backgrounds-legacy
Version: 8.0
Release: alt1
BuildArch: noarch

BuildRequires(pre): rpm-macros-branding

Source: backgrounds-%version.tar

Group: Graphics
Summary: Legacy SL backgrounds
License: CC-BY-NC-SA-3.0+
%branding_add_conflicts simply-linux backgrounds-legacy

Conflicts: branding-simply-linux-xfce-settings < 7.98.1-alt1

%define _unpackaged_files_terminate_build 1

%description
This package contains legacy backgrounds from
Simply Linux versions 5, 6, 7.

%package -n branding-simply-linux-backgrounds-vladstudio
Summary: Backgrounds from vladstudio.com
License: CC-BY-NC-SA-3.0+
Group: Graphics
%branding_add_conflicts simply-linux backgrounds-vladstudio
Conflicts: branding-simply-linux-xfce-settings < 7.98.1-alt1

%description -n branding-simply-linux-backgrounds-vladstudio
This package contains backgrounds from vladstudio.com.

%prep
%setup -n backgrounds-%version

%install
mkdir -p %buildroot%_datadir/backgrounds/xfce/
cp -a vladstudio* %buildroot%_datadir/backgrounds/xfce/
install -m 644 slinux_*.{jpg,png} %buildroot%_datadir/backgrounds/xfce/

%files
%_datadir/backgrounds/xfce/slinux_*

%files -n branding-simply-linux-backgrounds-vladstudio
%_datadir/backgrounds/xfce/vladstudio*

%changelog
* Fri Jun 16 2017 Mikhail Efremov <sem@altlinux.org> 8.0-alt1
- Separated from branding-simply-linux-xfce-settings.

