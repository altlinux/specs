%define oname Smoothwall-Breeze

Name: xfwm4-theme-%oname                                                                
Version: 1.2
Release: alt1

Summary: Adapted original Smoothwall window theme from XFCE for Breeze GTK theme
License: GPL-3.0+
Group: Graphical desktop/XFce
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %oname-%version.tar

Requires: xfwm4

BuildArch: noarch

%description
Adapted original Smoothwall window theme from xfwm4-themes for Breeze GTK theme.

%prep
%setup -n %oname

%install
mkdir -p %buildroot/%_datadir/themes/%oname
cp -a xfwm4 %buildroot/%_datadir/themes/%oname

%files
%_datadir/themes/%oname

%changelog
* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Use grayed active window decoration.

* Thu May 06 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Fix inactive colors.
- Set lightgray for inactive title text.

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
