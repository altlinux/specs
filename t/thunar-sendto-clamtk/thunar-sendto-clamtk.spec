Name: thunar-sendto-clamtk
Version: 0.08
Release: alt1
Summary: Simple virus scanning extension for Thunar
License: (GPL-1.0+ or Artistic-1.0) and BSD-3-Clause
Group: Graphical desktop/XFce
Url: https://bitbucket.org/davem_/thunar-sendto-clamtk
Vcs: git://gitlab.com/dave_m/thunar-sendto-clamtk.git

Source: https://bitbucket.org/davem_/thunar-sendto-clamtk/downloads/thunar-sendto-clamtk-%version.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: thunar, clamtk >= 5.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup

%build
%install
desktop-file-install --vendor "" \
	--dir %buildroot%_datadir/Thunar/sendto \
	%name.desktop

%files
%doc CHANGES DISCLAIMER LICENSE README.md
%_datadir/Thunar/sendto/%name.desktop

%changelog
* Mon Jul 29 2024 Leontiy Volodin <lvol@altlinux.org> 0.08-alt1
- New version (0.08).

* Mon Nov 15 2021 Leontiy Volodin <lvol@altlinux.org> 0.07-alt1
- New version (0.07).

* Wed Sep 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.06-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

