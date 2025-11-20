Name: noctalia-shell
Version: 3.1.1
Release: alt1

Summary: A sleek and minimal desktop shell thoughtfully crafted for Wayland
License: MIT
Group:   Graphical desktop/Other

URL: https://docs.noctalia.dev
VCS: https://github.com/noctalia-dev/noctalia-shell.git

Source0: %name-%version.tar
Source1: README-quickstart.md

BuildArch: noarch

BuildRequires(pre): rpm-build-xdg

# https://docs.noctalia.dev/getting-started/installation/#dependencies-explained
Requires: quickshell
Requires: fonts-ttf-roboto fonts-ttf-inter
Requires: gpu-screen-recorder-cli
Requires: brightnessctl

# Required for icons (and maybe smth else):
Requires: xdg-desktop-portal-gtk

# Calendar events are optional (requires python3 and evolution-data-server):
%add_findreq_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/calendar-events.py
%add_findreq_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/check-calendar.py
%add_findreq_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/list-calendars.py
%add_findprov_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/calendar-events.py
%add_findprov_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/check-calendar.py
%add_findprov_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Bin/list-calendars.py

# False positive
%filter_from_requires /kitty/d

%description
A beautiful, minimal desktop shell for Wayland that actually gets out of your
way. Built on Quickshell with a warm lavender aesthetic that you can easily
customize to match your vibe.

%prep
%setup
install -Dm644 %SOURCE1 .

%install
install -dm755 %buildroot%_xdgconfigdir/quickshell/noctalia-shell
cp -r ./*      %buildroot%_xdgconfigdir/quickshell/noctalia-shell
install -Dm644 Assets/Services/systemd/noctalia.service \
               %buildroot%_userunitdir/noctalia.service

%preun
%preun_service noctalia.service

%files
%doc README.md LICENSE README-quickstart.md
%_xdgconfigdir/quickshell/noctalia-shell
%_userunitdir/noctalia.service

%changelog
* Tue Nov 18 2025 Ilya Sorochan <k0tran@altlinux.org> 3.1.1-alt1
- Initial build.
