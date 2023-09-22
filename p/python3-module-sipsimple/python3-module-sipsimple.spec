%define modulename sipsimple

Name: python3-module-%modulename
Version: 5.3.0
Release: alt2

Summary: SIP SIMPLE implementation for Python
License: GPL-3.0+
Group: Development/Python3

Url: https://github.com/AGProjects/python3-sipsimple
Source: python3-%modulename-%version.tar
Source1: deps.tar
Patch: python-module-sipsimple-alt-add-arch-webrtc-defines.patch
Patch1: fix_ffmpeg.patch

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64 %e2k

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
BuildRequires: python3-module-Cython
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libopus-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libswscale-devel
BuildRequires: libv4l-devel
BuildRequires: libvpx-devel
BuildRequires: libwebrtc-devel
# TODO: Unable to detect /usr/include/silk/SKP_Silk_SDK_API.h
#BuildRequires: libsilk-devel

%description
SIP SIMPLE client SDK is a Software Development Kit for easy development
of SIP end-points that support rich media like Audio, Video, Instant
Messaging, File Transfers, Desktop Sharing and Presence.  Other media
types can be easily added by using an extensible high-level API.

%prep
%setup -n python3-%modulename-%version
tar xf %SOURCE1
%patch -p1
%patch1 -p1
cp -at deps/pjsip/ -- /usr/share/gnu-config/config.*
chmod +x deps/pjsip/*configure
%ifarch %e2k
# more 64-bit little endian arches
sed -i 's,^#elif defined(__aarch64__),& || defined(__e2k__),' \
	deps/pjsip/third_party/webrtc/src/webrtc/typedefs.h
%endif

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Sep 22 2023 Anton Vyatkin <toni@altlinux.org> 5.3.0-alt2
- (NMU) Fix FTBFS.

* Fri Jul 07 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version.

* Sun Feb 20 2022 Michael Shigorin <mike@altlinux.org> 5.2.6-alt3
- Buuild for %%e2k either.

* Thu Jan 20 2022 Stanislav Levin <slev@altlinux.org> 5.2.6-alt2
- Fixed FTBFS (setuptools 60+).

* Thu Sep 16 2021 Andrey Cherepanov <cas@altlinux.org> 5.2.6-alt1
- New version.

* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 5.2.3-alt1
- New version.

* Mon Jun 28 2021 Andrey Cherepanov <cas@altlinux.org> 5.2.2-alt1
- New version.
- Build only for x86_64.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.
- Build only python3 module.

* Sun May 23 2021 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt3
- Package module for python3.

* Fri Jan 15 2021 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt2
- Fix build by gcc10.
- Fix License tag.

* Wed Jun 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Sun Sep 01 2019 Michael Shigorin <mike@altlinux.org> 3.4.2-alt2
- Fixed build on %%e2k.

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version.

* Mon Feb 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3.0-alt2
- Fixed build on ppc64le.

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 3.1.1-alt2
- rebuilt for ffmpeg-4.0
- fixed built on aarch64

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
