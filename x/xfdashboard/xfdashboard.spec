Name: xfdashboard
Version: 0.1.5
Release: alt1

Summary: A Gnome shell like dashboard for Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://xfdashboard.froevel.de/

# Upstream: https://github.com/gmc-holle/xfdashboard.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel libgarcon-devel
BuildRequires: libwnck-devel libclutter-devel libdbus-glib-devel

%description
xfdashboard provides a GNOME shell dashboard like interface for use with
Xfce desktop. It can be configured to run to any keyboard shortcut and
when executed provides an overview of applications currently open
enabling the user to switch between different applications. The search
feature works like Xfce's app finder which makes it convenient to search
for and start applications.

%prep
%setup
%patch -p1
mkdir m4

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
%_datadir/themes/%name/

%changelog
* Wed Mar 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated url and description.
- Updated to 0.1.5.

* Tue Feb 25 2014 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Wed Feb 12 2014 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Mon Jan 27 2014 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon Jan 13 2014 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20131125
- Initial build.

