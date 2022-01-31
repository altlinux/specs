%define _unpackaged_files_terminate_build 1

%def_without check
%def_without docs

Name: qtile
Version: 0.20.0
Release: alt2

Summary: A full-featured, hackable tiling window manager written and configured in Python
License: MIT
Group: Graphical desktop/Other

#https://github.com/qtile/qtile
Url: http://www.qtile.org/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: python3-module-cairocffi
BuildRequires: python3-module-xcffib
BuildRequires: python3-module-setuptools_scm
BuildRequires: libcairo-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpango-devel
BuildRequires: libXcursor-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pygobject3
#BuildRequires: python3-module-bowler
BuildRequires: python3-modules-curses
BuildRequires: libgdk-pixbuf-gir
BuildRequires: libgtk+3-gir
BuildRequires: ImageMagick
BuildRequires: xorg-xephyr
BuildRequires: xorg-xvfb
%endif

%if_with docs
BuildRequires: graphviz
BuildRequires: libgdk-pixbuf
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib-seqdiag
BuildRequires: python3-module-webcolors
BuildRequires: python3-module-numpydoc
%endif

%description
%summary

%prep
%setup
%patch0 -p1

sed -i "s/version = .*/version = '%version'/"  docs/conf.py

%build
./scripts/ffibuild
%python3_build

%if_with docs
pushd docs
make html
popd
%endif

%install
%python3_install

install -Dm 644 resources/qtile.desktop -t %buildroot%_datadir/xsessions/
install -Dm 644 resources/qtile-wayland.desktop -t %buildroot%_datadir/wayland-sessions/

# FIXME
mv %buildroot%python3_sitelibdir/libqtile/widget/_pulse_audio.abi3.so %buildroot%python3_sitelibdir/libqtile/widget/_pulse_audio.so

%check
%__python3 -m pytest test

%files
%if_with docs
%doc docs/_build/html
%endif
%doc LICENSE README.rst libqtile/resources/default_config.py
%_bindir/qtile
%python3_sitelibdir/libqtile
%python3_sitelibdir/*.egg-info
%_datadir/xsessions/qtile.desktop
%_datadir/wayland-sessions/qtile-wayland.desktop

%changelog
* Thu Jan 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.20.0-alt2
- Build without docs for python3.10.

* Wed Jan 26 2022 Egor Ignatov <egori@altlinux.org> 0.20.0-alt1
- new version 0.20.0

* Thu Dec 23 2021 Egor Ignatov <egori@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Dec 17 2021 Egor Ignatov <egori@altlinux.org> 0.18.1-alt2
- Build with docs

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.18.1-alt1
- First build for ALT
