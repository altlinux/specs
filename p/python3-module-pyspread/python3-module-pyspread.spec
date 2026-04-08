%define _unpackaged_files_terminate_build 1

%define pypi_name pyspread

Name: python3-module-%pypi_name
Version: 2.4.4
Release: alt1

Summary: cross-platform Python spreadsheet application
License: GPL-3.0-or-later
Group: Office
URL: https://gitlab.com/pyspread/pyspread

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Requires: python3(markdown2)
Requires: python3(openpyxl)
Requires: python3(enchant)
Requires: python3(moneyed)
# NOTE: setuptools is really required for the app
Requires: python3(setuptools)

# TODO
%filter_from_requires /python3(lib.attrdict)/d
%filter_from_requires /python3(lib.selection)/d
%filter_from_requires /python3(model.model)/d
%filter_from_requires /python3(plotnine)/d
%filter_from_requires /python3(plotnine.data)/d
%filter_from_requires /python3(rpy2)/d
%filter_from_requires /python3(rpy2.interactive)/d
%filter_from_requires /python3(rpy2.robjects)/d
%filter_from_requires /python3(rpy2.robjects.lib)/d
%filter_from_requires /python3(rpy2.robjects.lib.ggplot2)/d
%filter_from_requires /python3(rpy2.robjects.packages)/d
%filter_from_requires /python3(rpy2.robjects.vectors)/d

Source: %pypi_name-%version.tar

%description
Pyspread is a cross-platform Python spreadsheet application. Instead of
spreadsheet formulas, Python expressions are entered into the spreadsheet
cells. Each expression returns a Python object that can be accessed from
other cells. These objects can represent anything including lists or
matrices.

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install --root=%buildroot --prefix=%_prefix --optimize=1

mkdir -pv %buildroot%_desktopdir
mv -v %buildroot/usr/pyspread/share/applications/io.gitlab.pyspread.pyspread.desktop %buildroot%_desktopdir/

install -D -m644 \
    "pyspread/share/icons/hicolor/svg/pyspread.svg" \
    "%buildroot%_iconsdir/hicolor/scalable/apps/pyspread.svg"

mkdir -pv %buildroot%python3_sitelibdir/%pypi_name/
cp -v AUTHORS %buildroot%python3_sitelibdir/%pypi_name/

%files
%doc AUTHORS changelog LICENSE README.md THANKS
%_bindir/pyspread
%_desktopdir/io.gitlab.pyspread.pyspread.desktop
%_iconsdir/hicolor/scalable/apps/pyspread.svg
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-*.egg-info/

%changelog
* Wed Apr 08 2026 Nikolay Strelkov <snk@altlinux.org> 2.4.4-alt1
- New version 2.4.4.

* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus
