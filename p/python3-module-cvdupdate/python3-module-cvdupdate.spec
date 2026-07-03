%define oname cvdupdate

Name: python3-module-%oname
Version: 1.2.0
Release: alt2

Summary: ClamAV Private Database Mirror Updater Tool
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/Cisco-Talos/cvdupdate

# Source-url: https://github.com/Cisco-Talos/%oname.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
# For %check (top-level imports of __main__.py):
BuildRequires: python3-module-click python3-module-colorlog python3-module-colorama
BuildRequires: python3-module-rangehttpserver python3-module-packaging
BuildRequires: python3-module-requests python3-module-dns
# Runtime deps imported via try/except ImportError in cvdupdate.py (lines 40-51):
# hidden from autoreq, but cvd update fails hard without them
# (ModuleNotFoundError / "DNS TXT query failed").
Requires: python3-module-requests
Requires: python3-module-dns

%description
CVD-Update is a tool from Cisco Talos that downloads and maintains
a mirror of ClamAV's signature databases (CVD and CDIFF files),
intended for hosting your own private ClamAV database mirror.
It is the supported replacement for the deprecated cvdupdate.sh script.

%package -n %oname
Summary: ClamAV Private Database Mirror Updater CLI
Group: Development/Python3
Requires: %name = %EVR

%description -n %oname
Command-line interface (cvd, cvdupdate) for CVD-Update, a tool to
download and maintain a mirror of ClamAV signature databases.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%python3_sitelibdir/tests

%check
# Verify the try/except-imported runtime deps are actually importable
# (requests, dnspython) and that the cvd CLI wrapper starts up.
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -c "import requests; from dns import resolver"
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -m cvdupdate --help >/dev/null

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%files -n %oname
%_bindir/cvd
%_bindir/cvdupdate

%changelog
* Fri Jul  3 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- Add explicit Requires: python3-module-requests, python3-module-dns:
  these are imported via try/except in cvdupdate.py and were missed by
  autoreq, so "cvd update" failed with ModuleNotFoundError / DNS error.
- Add %%check to verify runtime deps importable and the cvd CLI starts up.

* Thu Apr 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus
