%define _libexecdir %_prefix/libexec

Name: eve
Version: 0.3.0
Release: alt0.1

Summary: The Enlightenment Web Browser
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve
# VCS: git://git.enlightenment.fr/vcs/svn/eve.git

Source: %name-%version.tar

# from configure.ac
BuildRequires: libwebkit-efl-devel libedbus2-devel libelementary-devel
BuildRequires: edje embryo_cc

%description
Web Browser for Enlightenment desktop.

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
%_libdir/eve_ql.so
%exclude %_libdir/eve_ql.la
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt0.1
- first preview for Sisyphus (449a1604)


