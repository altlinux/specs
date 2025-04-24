Name: clamtk-kde
Version: 0.20
Release: alt1
Summary: Simple virus scanning extension for Dolphin and Konqueror
License: Artistic-1.0 or GPL-1.0-or-later
Group: Graphical desktop/KDE
Url: https://github.com/dave-theunsub/clamtk-kde
Vcs: https://github.com/dave-theunsub/clamtk-kde.git

Source: %url/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch
BuildArch: noarch

Requires: kf5-filesystem, clamtk >= 5.00

%description
It allows for right-click virus scanning within the Konqueror or Dolphin file browsers.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup
%autopatch -p1

%build
%install
mkdir -p %buildroot%_datadir/kservices5/ServiceMenus
cp -a clamtk-kde.desktop %buildroot%_datadir/kservices5/ServiceMenus/

%files
%doc CHANGES LICENSE README.md
%_datadir/kservices5/ServiceMenus/%name.desktop

%changelog
* Thu Apr 24 2025 Leontiy Volodin <lvol@altlinux.org> 0.20-alt1
- New version 0.20.
- Updated url, source and vcs tags.

* Wed Sep 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.18-alt1
- Initial build for ALT Sisyphus.

