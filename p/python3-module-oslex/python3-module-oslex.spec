%define pypi_name oslex
%define mod_name oslex

Name:    python3-module-%pypi_name
Version: 2.0.0
Release: alt2

Summary: OS-independent wrapper for shlex and mslex

License: MIT
Group:   Development/Python3
Url:     https://github.com/petamas/oslex

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Patch: oslex-import-mslex-lazily.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-wheel

# mslex is imported lazily only by the *_ms (Windows-style) functions, see patch
%add_python3_req_skip mslex

%description
oslex is an OS-independent wrapper for shlex and mslex.

Its main purpose is to provide functions similar in functionality to
shlex.quote(), shlex.split() and shlex.join() on both Windows and
POSIX-compatible platforms.

This goal is achieved by simply forwarding the calls to either shlex
(from the standard library) on POSIX-compatible systems, or the mslex
library on Windows.

In other words, oslex is to shlex/mslex what os.path is to
posixpath/ntpath.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- import mslex lazily: it is needed only by the *_ms functions (patch); do not require it

* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0

* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Sisyphus
