%define _unpackaged_files_terminate_build 1
%define pypi_name spyder

# TODO: find a way to run tests properly
%def_without check

Name: spyder
Version: 5.5.0
Release: alt1

Summary: The Scientific Python Development Environment
License: MIT
Group: Editors
Url: https://www.spyder-ide.org/
Vcs: https://github.com/spyder-ide/spyder

ExclusiveArch: %qt5_qtwebengine_arches

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires(pre): rpm-macros-qt5-webengine
%pyproject_builddeps_build

# to resize png
BuildRequires: convert

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: xvfb-run
BuildRequires: git-core
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-matplotlib-testing
BuildRequires: python3-module-pylint
%endif

%description
%summary.

%package -n python3-module-%pypi_name
Summary: The Scientific Python Development Environment (python package)
Group: Development/Python3
Url: https://pypi.org/project/spyder/

%description -n python3-module-%pypi_name
%summary.

%prep
%setup

# do not use vendored packages
%__rm -r external-deps

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# remove wrong-installed png icon
%__rm %buildroot%_iconsdir/%pypi_name.png

%__mkdir_p %buildroot/%_iconsdir/hicolor/{512x512,scalable}/

# resize png from 500x500 to 512x512
%_bindir/convert \
  img_src/%pypi_name.png -resize 512x512 \
  %buildroot%_iconsdir/hicolor/512x512/%pypi_name.png

# also install svg icon
%__install -m0644 -pD \
  img_src/%pypi_name.svg \
  %buildroot%_iconsdir/hicolor/scalable/%pypi_name.svg

# move python-module to arch-directory
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
%__mkdir_p %buildroot%python3_sitelibdir
%__mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
%_bindir/xvfb-run -- \
    %__python3 -m pyproject_installer run -- \
    %__python3 -m pytest -vra -Wignore

%files
%_bindir/%pypi_name
%_desktopdir/%pypi_name.desktop
%_iconsdir/hicolor/*/%pypi_name.*
%_datadir/metainfo/*.appdata.xml

%files -n python3-module-%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 08 2023 Anton Zhukharev <ancieg@altlinux.org> 5.5.0-alt1
- Built for ALT Sisyphus.

