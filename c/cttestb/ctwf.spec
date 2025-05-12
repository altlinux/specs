Name:    cttestb
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
install -Dm 0755 ctwf.py %buildroot%_bindir/cttestB
install -Dm 0644 ctwf.desktop %buildroot%_desktopdir/ctwf.desktop
install -Dm 0644 ctwf.png %buildroot%_pixmapsdir/ctwf.png
install -Dm 0644 quiz_topics.json %buildroot%_datadir/cttestB/quiz_topics.json
install -Dm 0644 theory_content.json %buildroot%_datadir/cttestB/theory_content.json

%files
%_bindir/cttestB
%_desktopdir/ctwf.desktop
%_pixmapsdir/ctwf.png
%_datadir/cttestB/quiz_topics.json
%_datadir/cttestB/theory_content.json

%changelog
* Mon May 12 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
