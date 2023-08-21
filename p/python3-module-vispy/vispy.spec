%def_disable check

Name: python3-module-vispy
Version: 0.13.0
Release: alt1.1
Summary: Interactive visualization in Python 3
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/vispy/vispy
# Source-url: https://github.com/vispy/vispy/archive/refs/tags/v%version.tar.gz
Source: vispy-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel

%if_disabled check
%else
BuildRequires: pytest3
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
BuildRequires: python3-module-hsluv
#BuildRequires: python3-module-pypng
BuildRequires: python3-module-six
%endif
# Nobody provides this module
%add_python3_req_skip vispy.util.geometry.triangulation

%description
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

%prep
%setup -n vispy-%version

%build
export CFLAGS="%optflags -fno-strict-aliasing"
%pyproject_build

%install
%pyproject_install

# fix version
mv %buildroot/%python3_sitelibdir/vispy-{0.0.0,%version}.dist-info
sed -i 's/^Version: .*/Version: %version/' %buildroot/%python3_sitelibdir/vispy-%version.dist-info/METADATA

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%doc *.rst *.md
%python3_sitelibdir/vispy
%python3_sitelibdir/vispy-%version.dist-info

%changelog
* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.13.0-alt1.1
- NMU: ignored unmet dependency

* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version (0.13.0) with rpmgs script

* Sun Aug 14 2022 Anton Midyukov <antohami@altlinux.org> 0.6.6-alt2
- Migration to PEP517
- Update Source-url

* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 0.6.6-alt1
- initial build
