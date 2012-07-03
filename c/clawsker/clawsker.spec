Name: clawsker
Version: 0.7.8
Release: alt1

Summary: Clawsker is an applet to edit Claws Mail's hidden preferences.
License: %gpl3plus
Group: Networking/Mail
URL: http://www.claws-mail.org/clawsker
BuildArch: noarch

Source: %name-%version.tar
Source1: %name.desktop

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-podlators perl-Locale-gettext perl-Gtk2
BuildRequires: desktop-file-utils

Requires: claws-mail

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
desktop-file-install --dir=%buildroot/%_desktopdir %SOURCE1

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop

%changelog
* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 0.7.8-alt1
- Updated to 0.7.8.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- Updated to 0.7.5.

* Tue Nov 30 2010 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Initial build
