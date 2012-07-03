Name: xfce4-embed-plugin
Version: 0.8.0
Release: alt2

Summary: Embed arbitrary application windows into the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel

Requires: xfce4-panel >= 4.8

%description
This plugin enables the embedding of arbitrary application windows into
the Xfce panel. The window is resized into the panel space available,
and the associated program can be automatically launched if it is not
open.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Feb 06 2012 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Patch from upstream:
  + Install plugin to lib instead of libexec.
- Initial build.

