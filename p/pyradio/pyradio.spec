%define pypi_name pyradio

Name: %pypi_name
Version: 0.9.3.11.31
Release: alt2

Summary: Command line internet radio player

License: MIT
Group: Sound
URL: https://pypi.org/project/pyradio
VCS: https://github.com/coderholic/pyradio

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pypi_name.desktop

Patch: radio-0.9.3.11.28-alt-fixes.patch
Patch1: main-0.9.3.11.16-alt-fixes.patch
Patch2: win-0.9.3.11.22-alt-linux.patch
Patch3: config-0.9.3.11.16-alt-fixes.patch

Requires: python3-module-psutil python3-module-dns mpv
# added dependencies for TTS funtion
# https://bugzilla.altlinux.org/59027
Requires: speech-dispatcher speech-dispatcher-utils espeak

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Curses based internet radio player.

%package -n python3-module-%pypi_name
Group: Development/Python3
Summary: Curses based internet radio player
%description -n python3-module-%pypi_name
Command line internet radio player.

%prep
%setup
subst "s|from .install import get_a_linux_resource_opener|# from .install import get_a_linux_resource_opener|" pyradio/html_help.py
%autopatch -p0

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 %SOURCE1 %buildroot%_desktopdir/%pypi_name.desktop

%files
%doc *.md LICENSE
%_bindir/%pypi_name
%_bindir/%pypi_name-client
%_desktopdir/%pypi_name.desktop

%files -n  python3-module-%pypi_name 
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat May 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.31-alt2
- added dependencies for TTS funtion (ALT #59027)

* Tue May 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.31-alt1
- 0.9.3.11.30 -> 0.9.3.11.31

* Fri Apr 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.30-alt1
- 0.9.3.11.29 -> 0.9.3.11.30

* Sun Mar 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.29-alt1
- 0.9.3.11.28 -> 0.9.3.11.29

* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.28-alt1
- 0.9.3.11.27 -> 0.9.3.11.28

* Sat Feb 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.27-alt1
- 0.9.3.11.26 -> 0.9.3.11.27

* Sat Feb 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.26-alt1
- 0.9.3.11.25 -> 0.9.3.11.26

* Mon Jan 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.25-alt1
- 0.9.3.11.24 -> 0.9.3.11.25

* Sat Jan 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.24-alt1
- 0.9.3.11.23 -> 0.9.3.11.24

* Fri Jan 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.23-alt1
- 0.9.3.11.22 -> 0.9.3.11.23

* Mon Jan 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.22-alt1
- 0.9.3.11.21 -> 0.9.3.11.22

* Mon Nov 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.21-alt1
- 0.9.3.11.20 -> 0.9.3.11.21

* Fri Oct 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.20-alt1
- 0.9.3.11.19 -> 0.9.3.11.20

* Fri Oct 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.19-alt3
- fix: adding some stations to favorites (thx s-n-g)

* Sun Sep 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.19-alt2
- Renamed to pyradio.

* Sat Sep 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.19-alt1
- 0.9.3.11.18 -> 0.9.3.11.19

* Sat Sep 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.18-alt1
- 0.9.3.11.17 -> 0.9.3.11.18

* Wed Sep 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.17-alt1
- 0.9.3.11.16 -> 0.9.3.11.17

* Wed Sep 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.16-alt1
- 0.9.3.11.15 -> 0.9.3.11.16

* Thu Jun 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.15-alt1
- 0.9.3.11.14 -> 0.9.3.11.15

* Tue Jun 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.14-alt1
- 0.9.3.11.13 -> 0.9.3.11.14

* Tue May 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.13-alt1
- 0.9.3.11.12 -> 0.9.3.11.13

* Fri May 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.12-alt1
- 0.9.3.11.11 -> 0.9.3.11.12

* Sun May 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.11-alt1
- 0.9.3.11.10 -> 0.9.3.11.11

* Wed May 07 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.10-alt1
- 0.9.3.11.9 -> 0.9.3.11.10

* Sat Mar 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.9-alt1
- 0.9.3.11.8 -> 0.9.3.11.9

* Thu Mar 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.8-alt1
- 0.9.3.11.7 -> 0.9.3.11.8

* Fri Mar 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.7-alt1
- Update to version 0.9.3.11.7

* Tue Mar 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.6-alt1
- Update to version 0.9.3.11.6

* Fri Feb 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.5-alt1
- Update to version 0.9.3.11.5

* Sun Jan 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.4-alt1
- Update to version 0.9.3.11.4

* Sat Dec 07 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.3-alt1
- Update to version 0.9.3.11.3

* Thu Nov 21 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.1-alt2
- Changed main categorie in pyradio.desktop.

* Wed Nov 20 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.1-alt1
- Initial build.
