#define _unpackaged_files_terminate_build 1

Name: kwin-mcp
Version: 0.12.0
Release: alt2

Group: Graphical desktop/KDE
Summary: MCP server for KDE Plasma Wayland GUI automation
Url: https://github.com/isac322/kwin-mcp
License: MIT

BuildArch: noarch

#Requires: python3 >= 3.12
#Requires: python3-module-mcp >= 2.2.0
#Requires: python3-module-mcp < 3
#Requires: python3-module-pygobject3 >= 3.42.0
#Requires: python3-module-dbus >= 1.3.2
#Requires: python3-module-pillow >= 10.0.0
Requires: kwin
Requires: spectacle
Requires: at-spi2-core
Requires: libei
Requires: wl-clipboard wtype wayland-utils

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-devel
BuildRequires: python3-module-uv-build >= 0.12.19
BuildRequires: python3-module-uv-build < 0.14

%description
kwin-mcp exposes KDE Plasma Wayland desktop automation through the Model
Context Protocol. It supports isolated virtual KWin sessions and live desktop
sessions, including accessibility inspection, screenshots and input injection.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/kwin-mcp
%_bindir/kwin-mcp-cli
%python3_sitelibdir/kwin_mcp/
%python3_sitelibdir/%{pyproject_distinfo kwin-mcp}/

%changelog
* Tue Nov 03 2026 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt2
- update package description

* Mon Nov 02 2026 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- initial build
