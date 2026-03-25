Name: altlinux-repos-additional
Version: 1.1
Release: alt1
Summary: Additional local repository
Group: System/Configuration/Other
License: GPL-2.0-or-later

BuildArch: noarch

Requires: apt-repo-tools
Provides: alterator-mirror-additional-repo
Obsoletes: alterator-mirror-additional-repo < 0.7.1-alt2

%description -n altlinux-repos-additional
%summary.

%install
mkdir -p %buildroot%_sysconfdir/apt/repositories
cat > %buildroot%_sysconfdir/apt/repositories/additional.desktop << EOF
[Desktop Entry]
Type=Application
Icon=package
Terminal=false
Name=Additional repository
Name[ru]=Дополнительный репозиторий
X-Sign=
X-Path=/additional
X-Has-Noarch=yes
X-Has-Arepo=no
X-Components=classic
X-Has-Arches=aarch64 i586 x86_64
X-Order=90
X-Local=yes
EOF

%files
%_sysconfdir/apt/repositories/additional.desktop

%changelog
* Wed Mar 25 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 1.1-alt1
- Add support for noarch repo (ALT #58343).

* Mon Mar 16 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Iniitial build.
