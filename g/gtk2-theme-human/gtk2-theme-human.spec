Name: gtk2-theme-human
Summary: A theme for GTK+ applications
Version: 20100916
Release: alt2
License: %ccbysa30
Group: Graphical desktop/GNOME
BuildArch: noarch
Url: https://launchpad.net/human-theme

Source0: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires: python-devel python-module-distutils-extra intltool

Requires: libgtk-engine-murrine libgtk-engine-clearlooks libgtk-engine-industrial

# Engines:
# murrine for Human & DarkRoom
# clearlooks for Human-Clearlooks
# industrial for HumanLogin

%description
This package contains Human themes for GTK+ applications

%prep
%setup

%build
%python_build

%install
%python_install
rm %buildroot%python_sitelibdir/human_theme-0.39.1-py%_python_version.egg-info

%files
%_datadir/themes/*
%_datadir/icons/*

%changelog
* Thu Dec 01 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 20100916-alt2
- Fix build

* Thu Jan 27 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 20100916-alt1
- Initial build

