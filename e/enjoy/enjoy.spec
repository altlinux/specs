%define _libexecdir %_prefix/libexec

Name: enjoy
Version: 0.1.0
Release: alt0.1

Summary: The Enlightenment Music Player
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve
# VCS: git://git.enlightenment.fr/vcs/svn/enjoy.git

Source: %name-%version.tar

# from configure.ac
BuildRequires: libecore-devel libedbus2-devel libemotion-devel libelementary-devel
BuildRequires: liblightmediascanner-devel libsqlite3-devel
BuildRequires: edje embryo_cc

%description
Music Player for Enlightenment desktop.

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
%_libdir/%name/
%exclude %_libdir/%name/*.la
%_libdir/%{name}_ql.so
%exclude %_libdir/%{name}_ql.la
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/%name.png
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.1
- first preview for Sisyphus (82e54272)


