%define nameD mpris_server

Name: python3-module-%nameD
Version: 0.10.0
Release: alt1

Summary: Integrate MPRIS Media Player support into your app
License: LGPL-3.0-only
Group: Development/Python3

Url: https://pypi.org/project/mpris-server
Vcs: https://github.com/alexdelorenzo/mpris_server

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar
#Fixed GLib.Variant extraction. 
#It's certainly strange that gi.repository.GLib isn't provided...
#in any case, it seems to work.
Patch: metadata-0.10.0-alt-fixes.patch
#Add '.' to valid characters for interface names.
Patch1: compat-0.10.0-Jeffser-fix.patch

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%nameD
%python3_sitelibdir/%{pyproject_distinfo %nameD}

%changelog
* Wed May 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- 0.9.6 -> 0.10.0 (updated to git.101daaaf)
- added patch for allow '.' in interface names (thnx Jeffser)
- added vcs

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.6-alt1
- Initial build for ALT Linux.

