%define _unpackaged_files_terminate_build 1

%def_without check

Name: autotiling
Version: 1.9.3
Release: alt1

Summary: Automatically switch the window split orientation in sway and i3
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/autotiling

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-argparse-manpage
BuildRequires: python3(i3ipc)

BuildArch: noarch

Source: %name-%version.tar

%description
This script uses the i3ipc-python library to switch the layout
splith/splitv depending on the currently focused window dimensions.
It works on both sway and i3 window managers.

%prep
%setup -n %name-%version

%build
%pyproject_build
# generate man-page
argparse-manpage.py3 --project-name=autotiling --author="Piotr Miller" --author-email="nwg.piotr@gmail.com" --url=https://github.com/nwg-piotr/autotiling/ --pyfile=autotiling/main.py --function get_parser --output autotiling.1

%install
%pyproject_install
# install man-page
install -pDm 644 %name.1 %buildroot%_man1dir/%name.1

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%name
%_man1dir/%name.*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sat May 10 2025 Nikolay Strelkov <snk@altlinux.org> 1.9.3-alt1
- Initial build for Sisyphus
