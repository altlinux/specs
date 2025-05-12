Name:    cttesta
Version: 1.0
Release: alt3

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
install -Dm 0755 script.py %buildroot%_datadir/cttestA/script.py
install -Dm 0644 cttestA.desktop %buildroot%_desktopdir/cttestA.desktop
install -Dm 0644 cttestA.png %buildroot%_pixmapsdir/cttestA.png
install -Dm 0644 questions.csv %buildroot%_datadir/cttestA/questions.csv

%files

%_desktopdir/cttestA.desktop
%_pixmapsdir/cttestA.png
%_datadir/cttestA/questions.csv
%_datadir/cttestA/script.py


%changelog
* Mon May 12 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt3
- Use data from file questions.csv.

* Mon Apr 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Fix path to executable in desktop file.

* Wed Apr 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial import to Sisyphus (thanks Gregory Dashko <freedoreme@yandex.by> for
  code).

