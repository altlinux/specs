%define _unpackaged_files_terminate_build 1

Name: qtile-extras
Version: 0.25.0
Release: alt1

Summary: A collection of mods made by elParaguayo for Qtile
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/elParaguayo/qtile-extras

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%description
%summary

%prep
%setup
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

rm -rf %buildroot%python3_sitelibdir_noarch/test

# remove strava for now
rm -r %buildroot%python3_sitelibdir_noarch/qtile_extras/resources/stravadata
rm %buildroot%python3_sitelibdir_noarch/qtile_extras/widget/strava.py
sed -i '/strava/d' %buildroot%python3_sitelibdir_noarch/qtile_extras/widget/__init__.py

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/qtile_extras
%python3_sitelibdir_noarch/qtile_extras-*.dist-info

%changelog
* Fri Apr 19 2024 Egor Ignatov <egori@altlinux.org> 0.25.0-alt1
- First build for ALT.
