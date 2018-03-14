%define modulename youtube_dl_gui

Name: youtube-dl-gui
Version: 0.4
Release: alt1

Summary: Youtube-dl media downloader with gui.
License: Public Domain
Group: Development/Python

Url: https://github.com/MrS0m30n3/youtube-dl-gui
Packager: Andrey Bychkov <mrdrew@altlinux.org>
BuildArch: noarch

Source0: youtube-dl-gui-%version.tgz
Source1: youtube-dl-gui.desktop

BuildPreReq: %py_dependencies setuptools
BuildRequires: desktop-file-utils
BuildRequires: python >= 2.7.3
BuildRequires: gettext
BuildRequires: python-module-wx >= 3
BuildRequires: python-module-twodict
BuildRequires: python-module-json

Requires: /usr/bin/xdg-open
Requires: python-module-%modulename = %EVR

%description
A cross platform front-end GUI of the popular youtube-dl media downloader written in wxPython.

%package -n python-module-%modulename
Summary: Youtube-dl-gui
Group: Development/Python
BuildArch: noarch

%py_requires twodict
Requires: python-module-wx >= 3

%description -n python-module-%modulename
Python module for youtube downloader with gui.

%prep
%setup -n youtube-dl-gui-%version

%build
%python_build

%install
%python_install
desktop-file-install \
--dir=${RPM_BUILD_ROOT}%{_desktopdir} \
%{SOURCE1}

%files
%doc AUTHORS LICENSE TODO
%_bindir/*
%{_desktopdir}/youtube-dl-gui.desktop
%{_datadir}/pixmaps/youtube-dl-gui.png

%files -n python-module-%modulename
%python_sitelibdir/%modulename
%python_sitelibdir/*.egg-info


%changelog
* Wed Mar 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt1
- Initial build for Sisyphus
