%def_with check

Name:    clickgen
Version: 2.2.5
Release: alt2

Summary: The hassle-free cursor building toolbox
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/clickgen

BuildArch: noarch
Source: %name-%version.tar

BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-numpy
BuildRequires: python3-module-toml
BuildRequires: python3-module-yaml
BuildRequires: python3-module-attrs
%endif

%description
%summary.

%package -n python3-module-%name
Group:  Development/Python3
Summary: Python3 module for clickgen
%description -n python3-module-%name
Clickgen is cross-platform python library for building XCursor and Windows Cursors.

%prep
%setup
%python3_fix_shebang *

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_clickgen_raises'

%files
%_bindir/clickgen
%_bindir/ctgen

%files -n python3-module-%name
%doc LICENSE *.md
%python3_sitelibdir/clickgen
%python3_sitelibdir/clickgen-*.dist-info

%changelog
* Wed Nov 13 2024 Alexander Kovalev <alexvk@altlinux.org> 2.2.5-alt2
- fix build requires
- fix python3 shebang
- add docs
- build with check

* Wed Nov 06 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.2.5-alt1
- initial build
