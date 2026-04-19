%define oname cvdupdate

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: ClamAV Private Database Mirror Updater Tool
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/Cisco-Talos/cvdupdate

# Source-url: https://github.com/Cisco-Talos/%oname.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%files -n %oname
%_bindir/cvd
%_bindir/cvdupdate

%changelog
* Thu Apr 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus
