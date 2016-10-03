Name: lxmenu-data
Version: 0.1.5
Release: alt1

Summary: Freedesktop.org application menu definition files
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu May 08 2014
# optimized out: libcloog-isl4 perl-Encode perl-XML-Parser
BuildRequires: intltool

BuildRequires: gettext glib2-devel rpm-build-xdg

BuildArch: noarch

Provides: lxde-lxmenu-data = %version-%release
Obsoletes: lxde-lxmenu-data < 0.1.4
Conflicts: altlinux-freedesktop-menu-lxde

%description
%summary

%prep
%setup

%build
# https://github.com/lxde/lxde-qt/issues/80
aclocal
libtoolize -c --automake --force
intltoolize -c --automake --force
automake --add-missing --copy --include-deps
autoconf
%configure
%make_build

%install
%makeinstall_std

%files
%_datadir/desktop-directories/*
%_xdgconfigdir/*/*
%doc AUTHORS README TODO

%changelog
* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.1.5-alt1
- 0.1.5

* Wed Mar 04 2015 Michael Shigorin <mike@altlinux.org> 0.1.4-alt3
- C: altlinux-freedesktop-menu-lxde (see also #30405)

* Tue Oct 21 2014 Michael Shigorin <mike@altlinux.org> 0.1.4-alt2
- P:/O: lxde-lxmenu-data (closes: #30405)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.4-alt1
- 0.1.4

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.0.0-alt1
- initial release

