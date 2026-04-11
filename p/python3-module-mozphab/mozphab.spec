%define _unpackaged_files_terminate_build 1

Name: python3-module-mozphab
Version: 2.12.0
Release: alt1

Summary: Phabricator CLI from Mozilla to support submission of a series of commits
Group: Development/Python3
License: MPL-2.0
URL: https://pypi.org/project/MozPhab/
VCS: https://github.com/mozilla-conduit/review.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distro
BuildRequires: python3-module-wheel
BuildRequires: python3-module-packaging
BuildRequires: python3-module-hglib
BuildRequires: python3-module-sentry-sdk
BuildRequires: python3-module-colorama

%description
Phabricator CLI from Mozilla to support submission of a series of commits.

%prep
%setup
# Change dynamic version fetched from git tag to static version from spec.
sed -i 's/dynamic = \["version"\]/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%_bindir/moz-phab
%python3_sitelibdir_noarch/%{pyproject_distinfo mozphab}
%python3_sitelibdir_noarch/mozphab

%changelog
* Thu Apr 09 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2.12.0-alt1
- Initial build.
