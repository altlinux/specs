Name: normcap
Version: 0.6.0
Release: alt2

Summary: OCR powered screen-capture tool to capture information instead of images

License: GPLv3
Group: Other
URL: https://github.com/dynobo/normcap
VCS: https://github.com/dynobo/normcap

BuildArch: noarch

Source: %name-%version.tar

Requires: tesseract xsel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel

%description
%summary.

%package -n python3-module-%name
Group:   Development/Python3
Summary: OCR powered screen-capture tool to capture information instead of images
%description -n python3-module-%name
%summary.

%prep
%setup
cat >> %name.desktop <<EOF
[Desktop Entry]
Categories=Utility;
Name=Normcap
Type=Application
Terminal=false
Exec=%name
Icon=%python3_sitelibdir/%name/resources/icons/%name.png
EOF

%build
%pyproject_build

%install
%pyproject_install
install -Dm 0644 %name.desktop %buildroot%_datadir/applications/%name.desktop

%files
%doc *.md
%_bindir/%name
%_datadir/applications/%name.desktop

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Thu Sep 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt2
- add requires xsel

* Tue Sep 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- Release: 0.6.0.

* Mon Sep 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt0.beta2
- Initial build for ALT Linux.
