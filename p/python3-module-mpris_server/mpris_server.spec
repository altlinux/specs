%define nameD mpris_server

Name: python3-module-%nameD
Version: 0.9.6
Release: alt1

Summary: Integrate MPRIS Media Player support into your app
License: LGPL-3.0-only
Group: Development/Python3

Url: https://pypi.org/project/mpris-server

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar
#Fixed GLib.Variant extraction. 
#It's certainly strange that gi.repository.GLib isn't provided...
#in any case, it seems to work.
Patch: metadata-0.9.6-alt-fixes.patch

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%nameD
%python3_sitelibdir/%{pyproject_distinfo %nameD}

%changelog
* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.6-alt1
- Initial build for ALT Linux.

