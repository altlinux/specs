%define  modulename trimesh

%ifarch %ix86 %arm
%def_disable check
%endif

Name:    python3-module-%modulename
Version: 4.0.7
Release: alt1

Summary: Python library for loading and using triangular meshes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/mikedh/trimesh

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pytest3
BuildRequires: python3(xdist)
BuildRequires: python3(httpx)
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: python3-module-rtree
BuildRequires: python3-module-lxml
BuildRequires: python3-module-shapely
BuildRequires: python3-module-networkx
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-svg
BuildRequires: python3-module-svg-path
BuildRequires: python3-module-msgpack

BuildArch: noarch

# Source-url: https://github.com/mikedh/trimesh/archive/%version/trimesh-%version.tar.gz
Source:  %modulename-%version.tar

%add_python3_req_skip glooey pyembree pyembree.mesh_construction

%description
%summary

%prep
%setup -n %modulename-%version

# Stub out unavailable pyinstrument test dependency; we don’t really need to do
# profiling anyway. Note that this does mean that API function
# trimesh.viewer.windowed.SceneViewer(…) will not work with “profile=True”.
#
# Packaging pyinstrument would be difficult due to a vue.js-based HTML
# renderer. Since guidelines forbid pre-built minified or compiled JS or CSS,
# this would have to be patched out, or the web asset pipeline would have to be
# somehow executed in the RPM build environment. (Or, of course, we can
# continue to do without pyinstrument.)
mkdir -p _stub
cat > _stub/pyinstrument.py <<'EOF'
class Profiler(object):
    def __enter__(self, *args, **kwds):
        return self

    def __exit__(self, *args, **kwds):
        return False

    def output_text(self, *args, **kwds):
        return """
Profiling output would be here if pyinstrument were available.
"""
EOF

# Patch out unavailable or dependencies from extras:
#
#   embreex: not packaged, https://github.com/mikedh/embreeX; this would
#            require version 2.x of embree, which was once available in a
#            compat package (https://src.fedoraproject.org/rpms/embree2) but
#            was retired; the current version was 4.x.
#   glooey: not yet packaged, https://github.com/kxgames/glooey; needs fonts
#           that are not currently packaged unbundled from its assets
#   manifold3d: not yet packaged, https://github.com/elalish/manifold/
#   meshio: not yet packaged, https://github.com/nschloe/meshio
#   pymeshlab: not yet packaged, https://github.com/cnr-isti-vclab/PyMeshLab/;
#              bundles MeshLab, which is a nontrivial package that has its own
#              bundling; see “Support a system/external copy of meshlab?”
#              https://github.com/cnr-isti-vclab/PyMeshLab/issues/309
#   python-fcl: not yet packaged; upstream is not compatible with the current
#               release of fcl,
#               https://github.com/BerkeleyAutomation/python-fcl/issues/19
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
#
# Those listed below are test-only dependencies: some are unavailable; the rest
# are unwanted under
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
#
#   black: linters/coverage/etc.
#   coveralls: linters/coverage/etc.
#   mypy: linters/coverage/etc.
#   pyinstrument: not packaged; see preceding “stub” patch
#   pytest-cov: linters/coverage/etc.
#   ruff: linters/coverage/etc.
for pkg in \
    black \
    coveralls \
    embreex \
    glooey \
    manifold3d \
    meshio \
    mypy \
    pyinstrument \
    pymeshlab \
    pytest-cov \
    python-fcl \
    ruff \
    %{?without_skimage:scikit-image} \
    xatlas \
    %{nil}
do
  sed -r -i "s/^([[:blank:]])*(\"${pkg}\",?)/\\1# \\2/" pyproject.toml
done

%build
%pyproject_build

%install
%pyproject_install
#rm %buildroot%python3_sitelibdir/%modulename/resources/templates/blender_boolean.py

%check
export PYTHONPATH="${PWD}/_stub:%buildroot%python3_sitelibdir"
pytest3 -v -k "not ( DAETest and test_material_round ) and \
       not ( DAETest and test_obj_roundtrip ) and \
       not ( LightTests and test_scene ) and \
       not ( OBJTest and test_multi_nodupe ) and \
       not ( SliceTest and test_slice_onplane )"

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.dist-info
%doc *.md

%changelog
* Thu Dec 21 2023 Anton Midyukov <antohami@altlinux.org> 4.0.7-alt1
- new version (4.0.7) with rpmgs script

* Tue Dec 19 2023 Anton Midyukov <antohami@altlinux.org> 4.0.6-alt1
- new version (4.0.6) with rpmgs script

* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 3.22.0-alt1
- new version (3.22.0) with rpmgs script

* Tue Jan 10 2023 Anton Midyukov <antohami@altlinux.org> 3.17.1-alt1
- new version (3.17.1) with rpmgs script

* Fri Mar 04 2022 Anton Midyukov <antohami@altlinux.org> 3.9.42-alt1
- Initial build for Sisyphus
