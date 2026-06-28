%define _unpackaged_files_terminate_build 1

Name: ducky
Version: 1.5.0
Release: alt1

Summary: Ducky - The Ultimate Networking Tool
License: MIT
Group: Networking/Other

Url: https://ducky.ge
Vcs: https://github.com/thecmdguy/Ducky

Requires: python3-module-telnetlib3
Requires: python3-module-pysnmp
Requires: traceroute

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Ducky is a powerful, open-source, all-in-one desktop application
built with Python and PySide6. It is designed to be the perfect
companion for network engineers, students, and tech enthusiasts,
combining several essential utilities into a single, intuitive
graphical interface. We welcome contributions from the community! 

%prep
%setup
cat >> %name.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Ducky
GenericName=The Ultimate Networking Tool
TryExec=/usr/bin/ducky
Exec=/usr/bin/ducky
Icon=/usr/lib/python3/site-packages/ducky_app/assets/ducky_icon.png
Terminal=false
Categories=Utility;Network;
EOF

%build
%pyproject_build

%install
%pyproject_install
pushd src/ducky_app
cp -p -r assets core ui utils %buildroot%python3_sitelibdir/%{name}_app
popd
install -Dm 644 %name.desktop %buildroot%_datadir/applications/%name.desktop

%files
%doc LICENSE *.md
%_bindir/%name
%python3_sitelibdir/%{name}*
%_datadir/applications/%name.desktop

%changelog
* Mon Jun 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5.0-alt1
- 1.3.0 -> 1.5.0

* Wed Feb 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.0-alt1
- Initial build for Alt Linux.

