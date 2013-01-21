%define _libexecdir %_prefix/libexec

Name: ephoto
Version: 0.1.1
Release: alt0.1

Summary: The Enlightenment Photo Viewer
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve
# VCS: git://git.enlightenment.fr/vcs/svn/ephoto.git

Source: %name-%version.tar

# from configure.ac
BuildRequires: libeio-devel libefreet-devel libelementary-devel
BuildRequires: edje embryo_cc

%description
Photo Viewer for Enlightenment desktop.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%{name}_ql
%_libdir/%{name}_ql.so
%exclude %_libdir/%{name}_ql.la
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt0.1
- first preview for Sisyphus (2dad9dc6)


