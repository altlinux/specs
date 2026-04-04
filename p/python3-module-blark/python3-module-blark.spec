%define pypi_name blark

Name: python3-module-blark
Version: 0.8.3
Release: alt1

Summary: Beckhoff TwinCAT IEC 61131-3 parsing tools

License: GPL-2.0
Group: Development/Python3
URL: https://github.com/klauer/blark
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools python3-module-wheel


%description
Blark is a Lark-based parsing toolkit for Beckhoff TwinCAT IEC 61131-3
Structured Text code. It provides tools for parsing TwinCAT source code
files (.TcPOU, .TcGVL, .tsproj, .sln) and plain .st files into Python
dataclasses with introspection capabilities. Supports code reformatting,
refactoring, and project dependency analysis.

%package -n blark
Summary: CLI tools for IEC 61131-3 Structured Text parsing
Group: Development/Python3
BuildArch: noarch

%description -n blark
Command-line tools for parsing and formatting Beckhoff TwinCAT
IEC 61131-3 Structured Text code. Provides 'blark parse' and
'blark format' commands.

%package sphinx
Summary: Sphinx domain for IEC 61131-3 Structured Text
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR
Requires: python3-module-sphinx python3-module-docutils

%description sphinx
Sphinx domain extension for documenting IEC 61131-3 Structured Text code.
Add 'blark.sphinxdomain' to your Sphinx extensions to use.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune
# apischema_compat.py requires python3-module-apischema (not packaged yet)
# To restore: package apischema from https://pypi.org/project/apischema/ and remove this rm
rm -f %buildroot%python3_sitelibdir/blark/apischema_compat.py

%files
%python3_sitelibdir/blark/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/blark/sphinxdomain.py
%exclude %python3_sitelibdir/blark/__pycache__/sphinxdomain.*

%files -n blark
%_bindir/blark

%files sphinx
%python3_sitelibdir/blark/sphinxdomain.py
%python3_sitelibdir/blark/__pycache__/sphinxdomain.*

%changelog
* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- initial build for ALT Sisyphus

