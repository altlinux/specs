%define _libexecdir %_prefix/libexec

Name: emprint
Version: 0.1.0
Release: alt0.1

Summary: The Enlightenment Screenshot Tool
Group: Graphical desktop/Enlightenment
License: GPLv3+
URL: http://trac.enlightenment.org/e/wiki/Eve
# VCS: git://git.enlightenment.fr/vcs/svn/ephoto.git

Source: %name-%version.tar

# from configure.ac
BuildRequires: libecore-devel libevas-devel

%description
Screenshot Tool for Enlightenment desktop.

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
%_datadir/%name/
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.1
- first preview for Sisyphus (73ca85a4)


