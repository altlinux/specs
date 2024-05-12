%define oname Kivy

%def_without check

Name: python3-module-kivy
Version: 2.2.1
Release: alt2

Summary: Open source UI framework written in Python

License: MIT
Group: System/Servers
Url: https://pypi.org/project/Kivy

Source: %name-%version.tar
Patch1: kivy-2.2.1-cython3-support.patch
Patch2: kivy-2.2.1-alt-do_not_use_ffpyplayer.patch

Requires: python3-module-docutils
Requires: python3-module-Pygments
Requires: python3-module-enchant
Requires: xclip

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-packaging
BuildRequires: libSDL2_image-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libgstreamer1.0
BuildRequires: libpango-devel
BuildRequires: libglvnd-devel
BuildRequires: mesa-dri-drivers

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-xvfb
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-responses
BuildRequires: libmtdev
BuildRequires: python3-module-certifi
%endif

%add_python3_req_skip AppKit PyInstaller.depend android android.runnable gimpfu picamera pyobjus pyobjus.dylib_manager
# pyjnius means we are running on Android
%add_python3_req_skip jnius

%add_python3_self_prov_path %buildroot%python3_sitelibdir/kivy/tools/pep8checker/

%description
Kivy - Open source Python library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip project project.widget

%description tests
This package contains tests for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i 's/distutils.cmd/setuptools/' kivy/tools/packaging/factory.py

# remove the legacy garden install script as python requirement, get it from PyPI
# or https://github.com/kivy-garden/garden/ if you need it
sed -i '/Kivy-Garden/d' setup.cfg

# remove benchmark from tests
sed -i '/addopts/d' pyproject.toml

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export KIVY_SPLIT_EXAMPLES=1
%pyproject_build

%install
%pyproject_install
rm -vrf %buildroot/usr/share/kivy-examples/

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# avoid collection errors
mv kivy kivy.notinpath
py.test-3 -k "\
not benchmark \
and not test_urlrequest_urllib \
and not test_remote_zipsequence \
and not test_audio \
and not test_local_zipsequence"

%files
%python3_sitelibdir/kivy/
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/kivy/tests

%files tests
%python3_sitelibdir/kivy/tests

%changelog
* Sun May 12 2024 Alexey Appolonov <alexey@altlinux.org> 2.2.1-alt2
- Fixed build;
- There is no support for ffpyplayer, which cannot be built using the current
  version of Cython (3.0.7).

* Fri Dec 22 2023 Anton Vyatkin <toni@altlinux.org> 2.2.1-alt1.1
- Build without check for python3.12.
- Add tests subpackage.

* Tue Dec 12 2023 Anton Vyatkin <toni@altlinux.org> 2.2.1-alt1
- new version 2.2.1
- backported fix for build agains Cython 3.0

* Tue Oct 24 2023 Anton Vyatkin <toni@altlinux.org> 2.1.0-alt1.2
- NMU: Dropped dependency on distutils.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.1.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- drop pyjnius requires (it is Android related)

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- initial build for ALT Sisyphus

* Sat Apr 17 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 2.0.0-alt1
- initial build for ALT Sisyphus
