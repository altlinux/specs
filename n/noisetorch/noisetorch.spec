Name: noisetorch
Version: 0.12.2
Release: alt4

Summary: Real-time microphone noise suppression on Linux

License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/NoiseTorch/NoiseTorch

# Source-url: https://github.com/noisetorch/NoiseTorch/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-development-%version.tar

# Source2-url: https://github.com/noisetorch/c-ringbuf/archive/refs/heads/master.zip
Source2: %name-c-ringbuf-%version.tar

Patch1: noisetorch-rnnoise.patch
Patch2: noisetorch-system-ladspa.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

BuildRequires: hicolor-icon-theme

BuildRequires: librnnoise-devel

%description
NoiseTorch is an easy to use open source application for Linux with PulseAudio.
It creates a virtual microphone that suppresses noise, in any application. Use
whichever conferencing or VOIP application you like and simply select the
NoiseTorch Virtual Microphone as input to torch the sound of your mechanical
keyboard, computer fans, trains and the likes.

%prep
%setup -a2
%patch1 -p2
%patch2 -p1

%build
pushd c/ladspa
%make_build CFLAGS="%optflags"
ldd rnnoise_ladspa.so
popd
go generate
# -tags release would enable the auto-updater (update.go)

%gobuild \
    -ldflags '-X main.version=%version -X main.distribution=rpm' .

%install
install -D -m 644 assets/icon/noisetorch.png %buildroot/%_iconsdir/hicolor/256x256/apps/noisetorch.png
install -D -m 644 assets/noisetorch.desktop %buildroot/%_desktopdir/noisetorch.desktop
install -D -m 755 noisetorch %buildroot/%_bindir/noisetorch
install -D -m 755 c/ladspa/rnnoise_ladspa.so %buildroot/%_libdir/ladspa/rnnoise_ladspa.so

%files
%doc LICENSE
%doc README.md
#caps(cap_sys_resource+ep) %_bindir/noisetorch
%_bindir/noisetorch
%_desktopdir/noisetorch.desktop
%_iconsdir/hicolor/256x256/apps/noisetorch.png
%_libdir/ladspa/rnnoise_ladspa.so

%changelog
* Tue Feb 03 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12.2-alt4
- install LADSPA plugin as system library instead of embedding
  (this adds automatic dependency on librnnoise) (ALT bug 57603)
- cleanup build: drop CGO_ENABLED=0, GOOS, -a, -w

* Mon May 13 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.12.2-alt3
- NMU: fixed FTBFS (enable cgo if required for PIE)

* Sat Nov 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.12.2-alt2
- NMU: fixed FTBFS on LoongArch

* Mon May 08 2023 Vitaly Lipatov <lav@altlinux.ru> 0.12.2-alt1
- initial build for ALT Sisyphus (thanks, OpenSUSE)
