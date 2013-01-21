# Warning: polkit-agent-helper-1 hardcoded in src/bin/pka.c
%define _libexecdir %_prefix/libexec

Name: empower
Version: 2.0.999
Release: alt0.1

Summary: The Enlightenment PolicyKit authentication agent
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve
# VCS: git://git.enlightenment.fr/vcs/svn/ephoto.git

Source: %name-%version.tar

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

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.999-alt0.1
- first preview for Sisyphus (2dad9dc6)


