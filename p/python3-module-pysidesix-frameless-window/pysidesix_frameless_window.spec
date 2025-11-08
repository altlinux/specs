%define nameS pysidesix_frameless_window
%define nameL qframelesswindow

Name: python3-module-pysidesix-frameless-window

Version: 0.7.4
Release: alt1.1

Summary: A cross-platform frameless window based on PySide6

License: LGPLv3
Group: Development/Python3

URL: https://pypi.org/project/PySideSix-Frameless-Window

ExcludeArch: i586

Source: %name-%version.tar

Patch: setup-0.7.4-alt-fixes.patch

Provides: python3-module-pyqt-frameless-window = %EVR
Obsoletes: python3-module-pyqt-frameless-window < %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup
%patch -p1
rm -r %nameL/mac
rm -r %nameL/windows
rm -v %nameL/utils/mac_utils.py
rm -v %nameL/utils/win32_utils.py

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%_prefix/lib/python3/site-packages/* %buildroot%python3_sitelibdir/
rm -r %buildroot%_prefix/lib

%files
%python3_sitelibdir/%nameL/
%python3_sitelibdir/%{pyproject_distinfo %nameS}/
%doc *.md LICENSE

%changelog
* Sat Nov 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.4-alt1.1
- rename package

* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.4-alt1
- Initial build for ALT Linux.
