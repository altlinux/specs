Name: vlc-npapi
Version: 2.0.0
Release: alt2
Summary: VLC Web Plugin
License: LGPLv2.1
Group: Video
Url: http://git.videolan.org/git/npapi-vlc.git

Source: %name-%version.tar

%description
VLC Web Plugin

%package -n mozilla-plugin-vlc
Group: Video
Summary: VLC Web Plugin
BuildRequires(Pre): browser-plugins-npapi-devel
BuildRequires: gcc-c++ libvlc-devel xulrunner-devel libgtk+2-devel

%description -n mozilla-plugin-vlc
VLC media player is a free network-aware MPEG1, MPEG2, MPEG4 (aka DivX),
DVD and many-many-more-player-and-streamer.

This package contains VLC web browser plugin.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -pD -m644 npapi/.libs/libvlcplugin.so %buildroot%browser_plugins_path/libvlcplugin.so

%files -n mozilla-plugin-vlc
%doc AUTHORS ChangeLog COPYING NEWS README
%browser_plugins_path/libvlcplugin.so

%changelog
* Thu Apr 19 2012 Dmitry Derjavin <dd@altlinux.org> 2.0.0-alt2
- 2.0.0 release.

* Mon Jan 30 2012 Dmitry Derjavin <dd@altlinux.org> 2.0.0-alt1rc
- 2.0.0-rc.

* Fri Jan 27 2012 Dmitry Derjavin <dd@altlinux.org> 1.2.0-alt2pre3
- plugin package name changed.

* Mon Jan 23 2012 Dmitry Derjavin <dd@altlinux.org> 1.2.0-alt1pre3
- Initial ALT Linux build.

