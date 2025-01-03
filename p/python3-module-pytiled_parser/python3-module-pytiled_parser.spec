Name:           python3-module-pytiled_parser
Version:        2.2.6
Release:        alt1
License:        MIT
Source:         pytiled_parser-%version.tar.gz
Summary:        A Python Library for parsing Tiled Map Editor maps
Group:          Development/Python3
URL:            https://github.com/pythonarcade/pytiled_parser
BuildArch:      noarch

# Automatically added by buildreq on Fri Jan 03 2025
# optimized out: bash5 libgpg-error openssl-config python3 python3-base python3-dev python3-module-iniconfig python3-module-jaraco.collections python3-module-jaraco.context python3-module-jaraco.functools python3-module-jaraco.text python3-module-more-itertools python3-module-packaging python3-module-pkg_resources python3-module-platformdirs python3-module-pluggy python3-module-py3dephell python3-module-wheel sh5
BuildRequires: python3-module-attrs python3-module-build python3-module-pyproject-installer python3-module-pytest python3-module-setuptools python3-module-typing_extensions

%description
PyTiled Parser is a Python Library for parsing [Tiled Map
Editor](https://www.mapeditor.org/) maps and tilesets to be used as maps
and levels for 2D top-down (orthogonal, hexogonal, or isometric) or
side-scrolling games in a strictly typed fashion.

PyTiled Parser is not tied to any particular graphics library or game
engine. It parses map files and returns arbitrary Python types(like
`Path` objects for image files rather than a `Sprite` from any
particular engine). This means it can be used to aide in implementing
Tiled support into a wide variety of tools.

%prep
%setup -n pytiled_parser-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir_noarch/pytiled_parser*

%check
python3 -m pytest

%changelog
* Fri Jan 03 2025 Fr. Br. George <george@altlinux.org> 2.2.6-alt1
- Initial build for ALT
