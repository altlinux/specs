# Warning: polkit-agent-helper-1 hardcoded in src/bin/pka.c
%define _libexecdir %_prefix/libexec

Name: empower
Version: 2.0.999
Release: alt0.2

Summary: The Enlightenment PolicyKit authentication agent
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://enlightenment.org
# VCS: git://git.enlightenment.fr/vcs/svn/empower.git

Source: %name-%version.tar
Source1: %name.desktop

# from configure.ac
BuildRequires: libedbus-devel libedje-devel libefreet-devel libelementary-devel
BuildRequires: libsystemd-login-devel
BuildRequires: edje embryo_cc

%description
A graphical PolicyKit authentication agent for Enlightenment desktop.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std
#install -pD -m644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/xdg/autostart/%name.desktop

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_sysconfdir/xdg/autostart/%name.desktop
#%_datadir/applications/%name.desktop
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.999-alt0.2
- aded desktop file

* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.999-alt0.1
- first preview for Sisyphus (2dad9dc6)


