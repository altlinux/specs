%define _unpackaged_files_terminate_build 1

Name: qtile-extras
Version: 0.36.0
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

# pyproject.toml backward compatibility with old setuptools
setuptools_version="$(python3 -c 'import setuptools; print(setuptools.__version__)')"
if [ "$(rpmvercmp "$setuptools_version" 77.0.3)" = -1 ]; then
    sed -i.orig -e '/license-files/d' \
        -e 's/^\(license = \)\(".*"\)$/\1{text = \2}/' ./pyproject.toml
fi

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
* Thu May 28 2026 Egor Ignatov <egori@altlinux.org> 0.36.0-alt1
- New version 0.36.0.

* Mon Mar 23 2026 Egor Ignatov <egori@altlinux.org> 0.35.0-alt1
- New version 0.35.0.

* Wed Dec 24 2025 Egor Ignatov <egori@altlinux.org> 0.34.1-alt1
- New version 0.34.1.

* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 0.34.0-alt1
- New version 0.34.0.

* Fri Aug 01 2025 Egor Ignatov <egori@altlinux.org> 0.33.0-alt1
- New version 0.33.0.

* Mon Jun 23 2025 Egor Ignatov <egori@altlinux.org> 0.32.0-alt1
- New version 0.32.0.

* Fri Mar 14 2025 Egor Ignatov <egori@altlinux.org> 0.31.0-alt1
- 0.31.0

* Wed Jan 29 2025 Egor Ignatov <egori@altlinux.org> 0.30.0-alt1
- 0.30.0

* Wed Oct 30 2024 Egor Ignatov <egori@altlinux.org> 0.29.0-alt1
- 0.29.0

* Tue Aug 13 2024 Egor Ignatov <egori@altlinux.org> 0.28.0-alt1
- 0.28.0

* Thu Jun 06 2024 Egor Ignatov <egori@altlinux.org> 0.26.0-alt1
- 0.26.0

* Fri Apr 19 2024 Egor Ignatov <egori@altlinux.org> 0.25.0-alt1
- First build for ALT.
