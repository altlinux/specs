Name: clawsker
Version: 1.1.1
Release: alt1

Summary: Clawsker is an applet to edit Claws Mail's hidden preferences
License: %gpl3plus
Group: Networking/Mail
URL: http://www.claws-mail.org/clawsker.php
BuildArch: noarch

# git://github.com/mones/clawsker.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-podlators perl-Locale-gettext perl-Gtk2
BuildRequires: desktop-file-utils

Requires: claws-mail >= 3.14.1

%define _unpackaged_files_terminate_build 1

%description
Clawsker is a Perl-GTK2 applet to edit hidden preferences
for Claws Mail, and to do it in a safe and user friendly way,
preventing users from raw editing of configuration files.

%prep
%setup

%build
sed -i -e 's|^all: build|all: build/clawsker|' \
       -e 's|^build:|build/clawsker:|' Makefile
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Tue Jan 09 2018 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Wed Mar 29 2017 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Tue Nov 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Use upstream's desktop file.
- Updated to 1.0.0.

* Mon Sep 05 2016 Mikhail Efremov <sem@altlinux.org> 0.7.14-alt1
- Updated to 0.7.14.

* Tue Oct 06 2015 Mikhail Efremov <sem@altlinux.org> 0.7.13-alt1
- Updated to 0.7.13.

* Fri Oct 24 2014 Mikhail Efremov <sem@altlinux.org> 0.7.12-alt1
- Updated to 0.7.12.

* Mon Jun 16 2014 Mikhail Efremov <sem@altlinux.org> 0.7.11-alt1
- Fix Url.
- Updated to 0.7.11.

* Wed May 15 2013 Mikhail Efremov <sem@altlinux.org> 0.7.10-alt1
- Updated to 0.7.10.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 0.7.8-alt1
- Updated to 0.7.8.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- Updated to 0.7.5.

* Tue Nov 30 2010 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Initial build
