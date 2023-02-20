%define _unpackaged_files_terminate_build 1

%define oname dropbox

Name: python3-module-%oname
Version: 11.36.0
Release: alt1

Summary: A Python SDK for integrating with the Dropbox API v2
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dropbox/

Vcs: https://github.com/dropbox/dropbox-sdk-python
Source: %name-%version.tar
Patch0: setup-alt-fix.patch
Patch1: req-alt-fix.patch
Patch2: test-req-alt-fix.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
%summary.

%prep
%setup
%patch0
%patch1
%patch2

%build
%python3_build

%install
%python3_install

# Tests require an access token

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info


%changelog
* Thu Feb 16 2023 Anton Vyatkin <toni@altlinux.org> 11.36.0-alt1
- new version 11.36.0 (Closes #44637).

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 9.4.0-alt2
- Build fixed.

* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 9.4.0-alt1
- Initial build.

