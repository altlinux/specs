%define  modulename trimesh

%ifarch %ix86 %arm
%def_disable check
%endif

Name:    python3-module-%modulename
Version: 3.9.42
Release: alt1

Summary: Python library for loading and using triangular meshes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/mikedh/trimesh

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: pytest3 python3-module-numpy python3-module-numpy-testing python3-module-scipy python3-module-rtree python3-module-lxml python3-module-shapely python3-module-networkx python3-module-jsonschema python3-module-svg python3-module-svg-path python3-module-msgpack

BuildArch: noarch

# Source-url: https://github.com/mikedh/trimesh/archive/%version/trimesh-%version.tar.gz
Source:  %modulename-%version.tar

%add_python3_req_skip glooey pyembree pyembree.mesh_construction

%description
%summary

%prep
%setup -n %modulename-%version

#   glooey: not yet packaged, https://github.com/kxgames/glooey; needs autoprop
#           (https://github.com/kalekundert/autoprop), review request
#           https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=2038330
sed -r -i "/^[[:blank:]]*'glooey',/d" setup.py
#   mapbox-earcut: not yet packaged,
#                  https://github.com/skogler/mapbox_earcut_python, review
#                  request: https://bugzilla.redhat.com/show_bug.cgi?id=2018705
sed -r -i "/^[[:blank:]]*'mapbox-earcut',/d" setup.py
#   meshio: not yet packaged, https://github.com/nschloe/meshio
sed -r -i "/^[[:blank:]]*'meshio',/d" setup.py
#   python-fcl: not yet packaged; upstream is not compatible with the current
#               release of fcl,
#               https://github.com/BerkeleyAutomation/python-fcl/issues/19
sed -r -i "/^[[:blank:]]*'python-fcl',/d" setup.py
#   triangle: has a nonfree dependency (Jonathan Richard Shewchuk’s “Triangle”
#             library, http://www.cs.cmu.edu/~quake/triangle.html, which
#             forbids commercial usage) so cannot be packaged
sed -r -i "/^[[:blank:]]*'triangle',/d" setup.py
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
sed -r -i "/^[[:blank:]]*'xatlas',/d" setup.py

# Patch out unavailable pyinstrument test dependency; we don’t really need to
# do profiling anyway. Note that this does mean that API function
# trimesh.viewer.windowed.SceneViewer(…) will not work with “profile=True”.
#
# Packaging pyinstrument would be difficult due to a vue.js-based HTML
# renderer. Since guidelines forbid pre-built minified or compiled JS or CSS,
# this would have to be patched out, or the web asset pipeline would have to be
# somehow executed in the RPM build environment. (Or, of course, we can
# continue to do without pyinstrument.)
sed -r -i "/'pyinstrument',/d" setup.py
sed -r -i 's/^([[:blank:]]*)(.*(pyinstrument|profiler)\b)/\1# \2/' \
    tests/regression.py

# Currently, python-ezdxf (https://pypi.org/project/ezdxf/,
# https://github.com/mozman/ezdxf) is not packaged. The tests are designed to
# fall back gracefully without it, but we must not generate the BuildRequires.
sed -r -i "s/'ezdxf'(\\]\\))/\\1/" setup.py

%build
%python3_build

%install
%python3_install
rm %buildroot%python3_sitelibdir/%modulename/resources/templates/blender_boolean.py

%check
pytest3 -v -k "not ( DAETest and test_material_round ) and \
	not ( DAETest and test_obj_roundtrip ) and \
	not ( LightTests and test_scene )"

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Fri Mar 04 2022 Anton Midyukov <antohami@altlinux.org> 3.9.42-alt1
- Initial build for Sisyphus
