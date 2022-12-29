# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: chirp
Version: 20221229
Release: alt1
Summary: A tool for programming two-way radio equipment

Group: Communications
License: GPLv3+
Url: https://github.com/kk7ds/chirp

Source: %name-%version.tar
Patch: %name-%version-alt.diff

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(future)
BuildRequires: python3(importlib_resources)
BuildRequires: python3(libxml2)
BuildRequires: python3(requests)
BuildRequires: python3(serial)
BuildRequires: python3(setuptools)
BuildRequires: python3(suds)
BuildRequires: python3(wheel)
BuildRequires: python3(wx)
BuildRequires: python3(yattag)

%description
Chirp is a tool for programming two-way radio equipment
It provides a generic user interface to the programming
data and process that can drive many radio models under
the hood.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc COPYING
%_bindir/chirp
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}-py3dev.dist-info/

%changelog
* Thu Dec 29 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 20221229-alt1
- revived chirp (from upstream py3 branch snapshot)

* Mon Jul 30 2018 Anton Midyukov <antohami@altlinux.org> 20180707-alt1
- new version (20180707) with rpmgs script

* Tue Nov 14 2017 Anton Midyukov <antohami@altlinux.org> 20171104-alt1
- Initial build for ALT Sisyphus.
