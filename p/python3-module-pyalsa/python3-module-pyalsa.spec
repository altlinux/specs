%define _unpackaged_files_terminate_build 1
%define oname pyalsa

Name: python3-module-%oname
Version: 1.2.7
Release: alt1

Summary: Official ALSA Python Binding
License: LGPLv2.1+
Group: Development/Python3

#https://github.com/alsa-project/alsa-python
Url: http://www.alsa-project.org
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: libalsa-devel

%description
Python binding for the ALSA library.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Fri Jun 03 2022 Egor Ignatov <egori@altlinux.org> 1.2.7-alt1
- new version 1.2.7

* Tue Dec 07 2021 Egor Ignatov <egori@altlinux.org> 1.2.6-alt1
- new version

* Tue Aug 24 2021 Egor Ignatov <egori@altlinux.org> 1.1.6-alt1
- First build for ALT
