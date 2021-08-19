%define oname icdiff

Name: python3-module-icdiff
Version: 2.0.4
Release: alt1

Summary: Python module for Improved Colored Difference Tool

Url: http://www.jefftk.com/icdiff
License: PSF
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
Show differences between two files in a two column colored view.

Your terminal can display color, but most diff tools don't make good use of it.
By highlighting changes, icdiff can show you the differences between similar files without getting in the way.
This is especially helpful for identifying and understanding small changes within existing lines.

Instead of trying to be a diff replacement for all circumstances,
the goal of icdiff is to be a tool you can reach for to get a better picture
of what changed when it's not immediately obvious from diff.

%package -n icdiff
Summary: Improved Colored Difference Tool
Group: File tools
Requires: %name = %EVR

BuildArch: noarch

%description -n icdiff
Show differences between two files in a two column colored view.

Your terminal can display color, but most diff tools don't make good use of it.
By highlighting changes, icdiff can show you the differences between similar files without getting in the way.
This is especially helpful for identifying and understanding small changes within existing lines.

Instead of trying to be a diff replacement for all circumstances,
the goal of icdiff is to be a tool you can reach for to get a better picture
of what changed when it's not immediately obvious from diff.


%prep
%setup

%build
%python3_build

%install
%python3_install

#mkdir -p %buildroot%_bindir
#install -p -m755 %oname %buildroot%_bindir/%oname
#install -p -m755 git-%oname %buildroot%_bindir/git-%oname

%files
%python3_sitelibdir/*

%files -n %oname
%doc README.md
%_bindir/%oname
%_bindir/git-%oname


%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- cleanup spec
- new version (2.0.4) with rpmgs script

* Tue Mar 01 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt2
- Moved from binaries from %_sbindir to %_bindir (ALT #31848)

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt1
- New version

* Tue Dec 16 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.1-alt1
- Initial build for ALT

