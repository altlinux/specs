%define pulseaudio_version 16.1

Name:     pulseaudio-module-xrdp
Version:  0.7
Release:  alt1

Summary:  xrdp sink / source pulseaudio modules
License:  Apache-2.0
Group:    Other
Url:      https://github.com/neutrinolabs/pulseaudio-module-xrdp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Source1:  pulseaudio-src.tar

BuildRequires: libpulseaudio-devel

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: intltool jackit-devel libalsa-devel libasyncns-devel
BuildRequires: libavahi-devel libbluez-devel
BuildRequires: libcap-devel libdbus-devel libgdbm-devel libudev-devel
BuildRequires: liblirc-devel libltdl7-devel libsoxr-devel
BuildRequires: libsndfile-devel libspeex-devel libspeexdsp-devel libwebrtc-devel
BuildRequires: libSM-devel libX11-devel libXtst-devel libxcbutil-devel
BuildRequires: libGConf-devel
BuildRequires: libfftw3-devel libsbc-devel liborc-devel orc xmltoman
BuildRequires: libcheck-devel libssl-devel libsystemd-devel

%description
xrdp implements Audio Output redirection using PulseAudio, which is a
sound system used on POSIX operating systems.

%prep
%setup
tar xf %SOURCE1

%build
# Check currect pulseaudio version
pa_ver="$(pkg-config --modversion libpulse)"
if [ "$pa_ver" != "%pulseaudio_version" ]; then
    echo "Package builds with different version of Pulseaudio in repository."
    exit 1
fi

%undefine _configure_gettext
# Configure Pulseaudio like pulseaudio.spec
pushd pulseaudio-src
echo "%pulseaudio_version" > .tarball-version
%meson \
    -Ddoxygen=false \
    -Ddatabase=gdbm \
    -Daccess_group=audio \
    -Dadrian-aec=true \
    -Dbluez5=enabled \
    -Dgsettings=enabled \
    -Djack=enabled
popd
# Build pulseaudio-module-xrdp
%autoreconf
%configure PULSE_DIR=`pwd`/pulseaudio-src CFLAGS="-I`pwd`/pulseaudio-src/%_host_alias"
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/pulseaudio/modules/*.la

%check
%make_build check

%files
%doc README.md
%_libdir/pulseaudio/modules/*.so
%_sysconfdir/xdg/autostart/pulseaudio-xrdp.desktop
%_libexecdir/pulseaudio-module-xrdp/load_pa_modules.sh

%changelog
* Tue Feb 28 2023 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- New version.

* Sun Jul 31 2022 Andrey Cherepanov <cas@altlinux.org> 0.6-alt3
- FTBFS: rebuilt with Pulseaudio 16.1.

* Sun Jun 12 2022 Andrey Cherepanov <cas@altlinux.org> 0.6-alt2
- FTBFS: rebuilt with Pulseaudio 16.0.

* Fri Nov 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- New version.

* Thu Jul 29 2021 Andrey Cherepanov <cas@altlinux.org> 0.5-alt3
- Rebuild with pulseaudio 15.0.

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 0.5-alt2
- Add hook to check current pulseaudio version in repository.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- New version.
- Rebuild woth Pulseaudio 14.2.

* Mon Oct 28 2019 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- New version.

* Mon Jun 17 2019 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
