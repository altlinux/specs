Name:		gnocky
Version:	0.0.7
Release:	alt1.1
Summary:	GLib2/GTK+2 frontend for gnokii using libglade
Group:		Communications
License:	GPLv2
URL:		http://wiki.gnokii.org/index.php/Gnocky
Source:		http://www.gnokii.org/download/%name/%name-%version.tar.gz
Patch:		gnocky-0.0.7-folders.patch

# Automatically added by buildreq on Sun Sep 19 2010
BuildRequires: libglade-devel libgnokii-devel

%description
%summary

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
# TODO desktop
%doc NEWS README TODO BUGS AUTHORS
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 0.0.7-alt1.1
- Fix patch

* Sun Sep 19 2010 Fr. Br. George <george@altlinux.ru> 0.0.7-alt1
- Initial build from scratch

