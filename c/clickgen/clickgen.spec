Name:    clickgen
Version: 2.2.5
Release: alt1

Summary: The hassle-free cursor building toolbox
License: MIT
Group:   Development/Python
URL:     https://pypi.org/project/clickgen

BuildArch: noarch
Source: %name-%version.tar

BuildRequires:  rpm-build-python3
BuildRequires:  python3-devel python3-module-pyyaml python3-module-Pillow python3-module-attrs python3-module-toml python3-module-numpy python3-module-setuptools

%description
%summary.

%package -n python3-module-%name
Group:  Development/Python
Summary: Python3 module for clickgen
%description -n python3-module-%name
Clickgen is cross-platform python library for building XCursor and Windows Cursors.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir/clickgen
%python3_sitelibdir/clickgen-*.dist-info

%changelog
* Wed Nov 06 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.2.5-alt1
- initial build
