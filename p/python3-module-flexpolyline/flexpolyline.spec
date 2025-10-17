%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-flexpolyline
Version: 0.1.0
Release: alt1

Summary: Lossy compressed representation of a list of coordinate pairs.
License: MIT
Group: Sciences/Geosciences
URL: https://github.com/heremaps/flexible-polyline
VCS: https://github.com/heremaps/flexible-polyline.git
BuildArch: noarch

%pyproject_runtimedeps_metadata

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: LICENSE

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
Flexible Polyline encoding: a lossy compressed representation
of a list of coordinate pairs or triples.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
cp %SOURCE2 .

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%python3_sitelibdir/flexpolyline/
%python3_sitelibdir/flexpolyline-%version.dist-info/
%doc LICENSE

%changelog
* Thu Oct 16 2025 Egor Shestakov <ved@altlinux.org> 0.1.0-alt1
- Initial build.
