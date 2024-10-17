%define _unpackaged_files_terminate_build 1
%define ns_root svg
%define pypi_name %ns_root.path
%define pypi_nname %ns_root-path
%define mod_name path

%def_with check

Name: python3-module-%pypi_nname
Version: 6.3
Release: alt1
Summary: SVG path objects and parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/svg.path/
Vcs: https://github.com/regebro/svg.path
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
Requires: python3-module-%ns_root-alt-namespace
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter check-manifest$
%add_pyproject_deps_check_filter pyroma$
%add_pyproject_deps_check_filter zest-releaser$
%pyproject_builddeps_metadata_extra test
%endif

%description
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# failures with pillow 10.1.0+: https://github.com/regebro/svg.path/issues/103
%pyproject_run_pytest -vra \
--deselect=tests/test_boundingbox_image.py::BoundingBoxImageTest::test_image \
--deselect=tests/test_image.py::ImageTest::test_image \

%files
%doc README.rst CHANGES.txt CONTRIBUTORS.txt
%python3_sitelibdir/%ns_root/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Oct 16 2024 Stanislav Levin <slev@altlinux.org> 6.3-alt1
- 4.1 -> 6.3.

* Thu Feb 03 2022 Anton Midyukov <antohami@altlinux.org> 4.1-alt1
- new version (4.1) with rpmgs script

* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 2.2-alt3
- rename srpm to python3-module-svg-path
- drop python2 subpackage
- drop tests subpackage
- cleanup spec

* Fri Jul 28 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt2
- New subpackages tests

* Wed Jul 26 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt1
- Initial build for ALT Sisyphus
