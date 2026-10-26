%define pypi_name wikiteam3

Name: wikiteam3
Version: 4.4.10
Release: alt1

Summary: Tools for downloading and preserving MediaWikis

License: GPL-3.0-or-later
Group: Archiving/Backup
URL: https://github.com/saveweb/wikiteam3

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
# https://github.com/saveweb/wikiteam3/pull/71
Patch1: wikiteam3-namespaced-unknown-content-model.patch

# wikiteam3uploader runs zstd and 7z via subprocess
Requires: /usr/bin/zstd /usr/bin/7z

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

%description
WikiTeam3 is a set of tools for archiving MediaWiki-based wikis,
from Wikipedia to the tiniest wikis. It contains:
 - wikiteam3dumpgenerator: dumps page texts (XML with full history),
   images and site info of a MediaWiki wiki;
 - wikiteam3uploader: uploads the dumps to the Internet Archive.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/wikiteam3dumpgenerator
%_bindir/wikiteam3uploader
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 26 2026 Vitaly Lipatov <lav@altlinux.ru> 4.4.10-alt1
- initial build for ALT Sisyphus

