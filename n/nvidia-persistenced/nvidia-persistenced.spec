Name: nvidia-persistenced
Version: 595.91.07
Release: alt1

Group: System/Configuration/Hardware
Summary: Daemon for maintaining persistent driver state
License: MIT and GPLv2+
Url: https://github.com/NVIDIA/nvidia-persistenced

ExclusiveArch: x86_64 aarch64

#Source0: https://download.nvidia.com/XFree86/%name/%name-%version.tar.bz2
Source0: %name-%version.tar

BuildRequires: gcc libtirpc-devel
#BuildRequires: systemd

%description
A daemon for maintaining persistent driver state,
specifically for use by the NVIDIA Linux driver.

%prep
%setup

%build
%make_build \
  NVDEBUG=1 \
  NV_VERBOSE=1 \
  STRIP_CMD=true \
  NV_KEEP_UNSTRIPPED_BINARIES=1 \
  X_LDFLAGS="-L%_libdir" \
  CC_ONLY_CFLAGS="%optflags" \
  #
pushd _out/Linux_*/
    mv nvidia-persistenced{.unstripped,}
popd

%install
%make NVIDIA_PERSISTENCED_install NV_VERBOSE=1 PREFIX=%prefix BINDIR=%buildroot/%_bindir
%make MANPAGE_install NV_VERBOSE=1 PREFIX=%prefix MANDIR=%buildroot/%_man1dir

mkdir -p %buildroot/%_unitdir
install -pm 0644 \
    init/systemd/%name.service.template \
    %buildroot/%_unitdir/%name.service
sed -i "s/__USER__/root/" %buildroot/%_unitdir/%name.service

%files
%doc README COPYING
%_bindir/%name
%_unitdir/%name.service
%_man1dir/*%{name}*

%changelog
* Thu Sep 03 2026 Sergey V Turchin <zerg@altlinux.org> 595.91.07-alt1
- initial build
