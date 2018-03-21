Name:    weboob
Version: 1.3
Release: alt1

Summary: Weboob is a collection of applications able to interact with websites, without requiring the user to open them in a browser
License: AGPLv3+
Group:   Networking/WWW
URL:     http://weboob.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %name-%version.tar

%description
Weboob is a collection of applications able to interact with websites,
without requiring the user to open them in a browser.

%package -n python-module-weboob
Summary: Python module for Weboob
Group: Development/Python

%description -n python-module-weboob
Python module for Weboob.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/64x64/apps/*.png
%_man1dir/*

%files -n python-module-weboob
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Initial build in Sisyphus
