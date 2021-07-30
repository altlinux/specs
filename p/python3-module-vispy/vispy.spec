# needed more buildrequires
%def_disable check

Name: python3-module-vispy
Version: 0.6.6
Release: alt1
Summary: Interactive visualization in Python 3
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/vispy/vispy
# Source-url: https://files.pythonhosted.org/packages/source/v/vispy/vispy-%version.tar.gz
Source: vispy-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm_git_archive
BuildRequires: python3-module-Cython

BuildRequires: libnumpy-py3-devel

%if_disabled check
%else
BuildRequires: python3-module-sdl2
#BuildRequires: python3-module-glfw
BuildRequires: python3-module-imageio
BuildRequires: python3-module-networkx
BuildRequires: python3-module-OpenGL
BuildRequires: python3-module-pyglet
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-scipy
BuildRequires: python3-module-numpy-testing
BuildRequires: fontconfig
#BuildRequires: python3-module-cassowary
BuildRequires: python3-module-decorator
BuildRequires: python3-module-freetype
#BuildRequires: python3-module-husl
#BuildRequires: python3-module-pypng
BuildRequires: python3-module-six
%endif

%description
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

%prep
%setup -q -n vispy-%version
#rm -rf vispy/ext/_bundled
sed -i -e '/^#!\//, 1d' vispy/glsl/build-spatial-filters.py vispy/util/transforms.py vispy/visuals/collections/util.py

%build
export CFLAGS="%optflags -fno-strict-aliasing"
%python3_build

%install
%python3_install

# remove jupyter
rm -r %buildroot%_prefix%_sysconfdir/jupyter
rm -r %buildroot%_datadir/jupyter

# remove tests
rm -r %buildroot%python3_sitelibdir/vispy/app/backends/tests
rm -r %buildroot%python3_sitelibdir/vispy/app/tests
rm -r %buildroot%python3_sitelibdir/vispy/color/tests
rm -r %buildroot%python3_sitelibdir/vispy/geometry/tests
rm -r %buildroot%python3_sitelibdir/vispy/gloo/gl/tests
rm -r %buildroot%python3_sitelibdir/vispy/gloo/tests
rm -r %buildroot%python3_sitelibdir/vispy/io/tests
rm -r %buildroot%python3_sitelibdir/vispy/plot/tests
rm -r %buildroot%python3_sitelibdir/vispy/scene/cameras/tests
rm -r %buildroot%python3_sitelibdir/vispy/scene/tests
rm -r %buildroot%python3_sitelibdir/vispy/util/dpi/tests
rm -r %buildroot%python3_sitelibdir/vispy/util/fonts/tests
rm -r %buildroot%python3_sitelibdir/vispy/util/tests
rm -r %buildroot%python3_sitelibdir/vispy/visuals/graphs/tests
rm -r %buildroot%python3_sitelibdir/vispy/visuals/shaders/tests
rm -r %buildroot%python3_sitelibdir/vispy/visuals/tests
rm -r %buildroot%python3_sitelibdir/vispy/visuals/transforms/tests
rm -r %buildroot%python3_sitelibdir/vispy/testing

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 0.6.6-alt1
- initial build
