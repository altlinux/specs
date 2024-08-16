%define git 22210ca
%define name speedtest-cli
%define version 2.1.4
%define release alt0.3.g%{git}

Name: %name
Version: %version
Release: %release

Summary: Network bandwidth testing tool
License: Apache-2.0
Group: System/Configuration/Networking
Url: https://github.com/sivel/speedtest-cli
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Command line interface for testing internet bandwidth using
speedtest.net

%prep
%setup -q

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%install
mkdir -p %buildroot%_bindir
install -m755 speedtest.py %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=speedtest-cli
Comment=CLI for speedtest.net
Icon=%name
Exec=%name
Terminal=true
Categories=Settings;HardwareSettings;
EOF

%files
%_bindir/*
%doc README.rst CONTRIBUTING.md
%_desktopdir/%name.desktop

%changelog
* Fri Jul 12 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.4-alt0.3.g22210ca
- Update deprecated method in datetime call (upstream PR #803).

* Sat Oct 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2.1.4-alt0.2.g22210ca
- set secure connection by default (upstream PR #800)

* Wed Sep 28 2022 L.A. Kostis <lakostis@altlinux.ru> 2.1.4-alt0.1.g22210ca
- GIT 22210ca (w/ python 3.10 support).

* Thu Jun 03 2021 L.A. Kostis <lakostis@altlinux.ru> 2.1.3-alt2
- spec:
   + update BR (add rpm-build-python3);
   + fix License tag.

* Mon Apr 12 2021 Alexander Makeenkov <amakeenk@altlinux.org> 2.1.3-alt1
- Updated to version 2.1.3

* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt1
- Version updated to 2.1.2

* Thu Oct 31 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt1
- python2 -> python3

* Sun Oct 30 2016 L.A. Kostis <lakostis@altlinux.ru> 0.3.4-alt2
- Use correct naming during install.

* Wed Oct 19 2016 L.A. Kostis <lakostis@altlinux.ru> 0.3.4-alt1
- 0.3.4.

* Mon Sep 14 2015 L.A. Kostis <lakostis@altlinux.ru> 0.3.2-alt1
- initial build for ALTLinux.
