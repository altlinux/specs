Name: python3-module-luma-core
Version: 2.4.0
Release: alt2

Summary: Small display library core
License: MIT
Group: Development/Python
Url: https://pypi.org/project/luma.core/

Requires: python3(smbus2)

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
luma.core is a component library providing a Pillow-compatible drawing canvas
for Python 3, and other functionality to support drawing primitives and
text-rendering capabilities for small displays on single board computers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/luma
%python3_sitelibdir/luma.core-%version.dist-info

%changelog
* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt2
- require smbus2

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released
