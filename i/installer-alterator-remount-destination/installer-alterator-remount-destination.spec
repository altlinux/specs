Name: installer-alterator-remount-destination
Version: 0.1
Release: alt1

Summary: Alterator module for remount destination filesystem
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch

BuildRequires: alterator >= 5.0

Requires: installer-scripts-remount-stage2 >= 0.6.0-alt1
Conflicts: alterator-preinstall < 0.9-alt1

%description
%summary.

%prep
%setup -c

%build
make

%install
%makeinstall DESTDIR=%buildroot

%files
%_alterator_datadir/ui/remount-destination
%_alterator_libdir/backend3/remount-destination

%changelog
* Sat Apr 01 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
