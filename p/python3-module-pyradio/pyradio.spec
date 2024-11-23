%define pypi_name pyradio

Name:    python3-module-%pypi_name
Version: 0.9.3.11.1
Release: alt2

Summary: Curses based internet radio player

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pyradio
VCS:	 https://github.com/coderholic/pyradio

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pypi_name.desktop

Patch: radio-0.9.3.11.1-alt-fixes.patch
Patch1: main-0.9.3.11.1-alt-fixes.patch
Patch2: win-0.9.3.11.1-alt-linux.patch
Patch3: config-0.9.3.11.1-alt-fixes.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools python3-module-wheel

%description
Command line internet radio player.

%package -n %pypi_name
Group:   Sound
Requires: python3-module-psutil python3-module-dns mpv 
Requires: python3-module-%pypi_name = %EVR
Summary: Curses based internet radio player
%description -n %pypi_name
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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%_desktopdir/%pypi_name.desktop

%changelog
* Thu Nov 21 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.1-alt2
- Changed main categorie in pyradio.desktop.

* Wed Nov 20 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.9.3.11.1-alt1
- Initial build.
