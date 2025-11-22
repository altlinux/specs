Name: alt-mirror-switcher
Version: 0.4.4.1
Release: alt1

Summary: Simple local mirror switcher for ALT

License: GPLv2+
Group: Other

Url: https://altlinux.space/aleksandershad/alt-mirror-switcher

BuildArch: noarch

Source: %name-%version.tar

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-build-python3

%description
%summary.

%package lists-sisyphus
Summary: Additional mirrors for %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Conflicts: %name-lists-branch
%description lists-sisyphus
Additional mirrors for %name.

%package lists-branch
Summary: Additional mirrors for %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Conflicts: %name-lists-sisyphus
%description lists-branch
Additional mirrors for %name.

%prep
%setup
rm -v mirrors/ams.sh

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    PREFIXBIN=%buildroot%_bindir

install -d %buildroot%_sysconfdir/apt/sources.list.d
mv %buildroot%_datadir/%name/mirrors/*.list \
  %buildroot%_sysconfdir/apt/sources.list.d/
rm -r %buildroot%_datadir/%name/mirrors

%find_lang %name --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%doc README.md

%files lists-sisyphus
%_sysconfdir/apt/sources.list.d/ams_*_sisyphus.list

%files lists-branch
%_sysconfdir/apt/sources.list.d/ams_*_branch.list

%changelog
* Sat Nov 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4.1-alt1
- Splitting additional mirrors into sub-packages.
- Added mirrors:
  + download.etersoft.ru
  + mirror.datacenter.by (p11)
  + mirror.mephi.ru

* Wed Nov 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4-alt1
- added mirror: download.basealt.ru

* Tue Nov 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- 0.4.2 -> 0.4.3 (ALT #56880)

* Mon Nov 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2:
  + added: localization
  + disable system *.list and enable /etc/apt/sources.list

* Sat Nov 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1 (ALT #56850)

* Fri Nov 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.0-alt1
- 0.3.1 -> 0.4.0 (ALT #56850)

* Sat Nov 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Wed Oct 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.0-alt1
- 0.2.1 -> 0.3.0:
  + add: labels and protocols
  + change for branch [p1*

* Wed Oct 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.1-alt1
- 0.2 -> 0.2.1

* Mon Oct 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- 0.1 -> 0.2

* Sun Oct 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1-alt1
- Initial build for ALT Linux.
