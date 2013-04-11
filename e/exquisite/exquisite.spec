%define _libexecdir %_prefix/libexec

Name: exquisite
Version: 1.0.0
Release: alt0.1

Summary: Enlightenment bootsplash program
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

# from configure.ac
BuildRequires: libeet-devel libecore-devel libevas-devel libedje-devel edje

%description
Bootsplash program able to render in Framebuffer, or X11 that is easy to
integrate with existing boot setups (sysvinit or systemd) bia messaging
(pipe or socket) as well as customise look and feel via Edje.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/%name-write
%_datadir/%name/
%doc AUTHORS README demo/run-demo.sh

%changelog
* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1
- first preview for Sisyphus



