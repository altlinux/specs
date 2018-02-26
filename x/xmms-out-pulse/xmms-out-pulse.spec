Name: xmms-out-pulse
Version: 0.9.4
Release: alt1

Summary: xmms-pulse is an XMMS output plugin for the PulseAudio sound server
Group: Sound
License: GPL
Url: http://0pointer.de/lennart/projects/xmms-pulse/

Source0: xmms-pulse-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: pulseaudio >= 0.9.2
Requires: xmms

# Automatically added by buildreq on Wed Mar 05 2008
BuildRequires: gcc-c++ libpulseaudio-devel libxmms-devel lynx

%description
xmms-pulse is an XMMS output plugin for the PulseAudio sound server.

%prep
%setup -q -n xmms-pulse-%version

%build
%configure \
	--libdir=%xmms_outputdir \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README
%xmms_outputdir/*.so
%xmms_outputdir/*.la

%changelog
* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- 0.9.3 -> 0.9.4
- buildreq

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
