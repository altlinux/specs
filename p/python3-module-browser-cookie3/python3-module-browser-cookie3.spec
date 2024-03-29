%define oname browser-cookie3
%define pname browser_cookie3

Name: python3-module-browser-cookie3
Version: 0.17.1
Release: alt2

Summary: Loads cookies from your browser into a cookiejar object

License: LGPLv3
Group: Development/Python3
Url: https://github.com/borisbabic/browser_cookie3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

Patch1: %name-import.patch

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
Loads cookies from your browser into a cookiejar object
so can download with urllib and other libraries
the same content you see in the web browser.

%prep
%setup
%patch1 -p2

%build
%python3_build

%install
%python3_install


%files
%doc README.md
%python3_sitelibdir/%pname/
%python3_sitelibdir/%pname-%version-py%_python3_version.egg-info/

%changelog
* Sat Apr 01 2023 Vitaly Lipatov <lav@altlinux.ru> 0.17.1-alt2
- fix requires search (make sqlite3 require visible) (ALT bug 45728)

* Thu Mar 16 2023 Vitaly Lipatov <lav@altlinux.ru> 0.17.1-alt1
- initial build for ALT Sisyphus
