%define  modulename trimesh

%ifarch %ix86 %arm
%def_disable check
%endif

Name:    python3-module-%modulename
Version: 3.17.1
Release: alt1

Summary: Python library for loading and using triangular meshes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/mikedh/trimesh

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pytest3 python3-module-numpy python3-module-numpy-testing python3-module-scipy python3-module-rtree python3-module-lxml python3-module-shapely python3-module-networkx python3-module-jsonschema python3-module-svg python3-module-svg-path python3-module-msgpack

BuildArch: noarch

# Source-url: https://github.com/mikedh/trimesh/archive/%version/trimesh-%version.tar.gz
Source:  %modulename-%version.tar

%add_python3_req_skip glooey pyembree pyembree.mesh_construction

%description
%summary

%prep
%setup -n %modulename-%version

# Patch out unavailable dependencies from “extras”:
#
# [all]
#   glooey: not yet packaged, https://github.com/kxgames/glooey; needs fonts
#           that are not currently packaged unbundled from its assets
sed -r -i "/^[[:blank:]]*'glooey',/d" setup.py
#   meshio: not yet packaged, https://github.com/nschloe/meshio
sed -r -i "/^[[:blank:]]*'meshio',/d" setup.py
#   python-fcl: not yet packaged; upstream is not compatible with the current
#               release of fcl,
#               https://github.com/BerkeleyAutomation/python-fcl/issues/19
sed -r -i "/^[[:blank:]]*'python-fcl',/d" setup.py
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
sed -r -i "/^[[:blank:]]*'xatlas',/d" setup.py

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
sed -r -i "/'pyinstrument',/d" setup.py

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
* Tue Jan 10 2023 Anton Midyukov <antohami@altlinux.org> 3.17.1-alt1
- new version (3.17.1) with rpmgs script

* Fri Mar 04 2022 Anton Midyukov <antohami@altlinux.org> 3.9.42-alt1
- Initial build for Sisyphus
