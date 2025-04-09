Name:    cttesta
Version: 1.0
Release: alt1

Summary: CT test trainer
License: GPL-3.0+
Group:   Education
Url:     http://altlinux.org

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
%{summary}.

%prep
%setup

%install
install -Dm 0755 script.py %buildroot%_bindir/cttestA
install -Dm 0644 cttestA.desktop %buildroot%_desktopdir/cttestA.desktop
install -Dm 0644 cttestA.png %buildroot%_pixmapsdir/cttestA.png

%files
%_bindir/cttestA
%_desktopdir/cttestA.desktop
%_pixmapsdir/cttestA.png

%changelog
* Wed Apr 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial import to Sisyphus (thanks Gregory Dashko <freedoreme@gmail.com> for
  code).
