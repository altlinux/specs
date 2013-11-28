Name: xfdashboard
Version: 0.0.1
Release: alt1.git20131125

Summary: A Gnome shell like dashboard for Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://github.com/gmc-holle/xfdashboard

# Upstream: https://github.com/gmc-holle/xfdashboard.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel libgarcon-devel
BuildRequires: libwnck-devel libclutter-devel libdbus-glib-devel

%description
Maybe a Gnome shell like dashboard for Xfce.
A quick'n'dirty guide:
http://gmc-holle.github.io/xfdashboard/

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfdashboard_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name

%changelog
* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20131125
- Initial build.

