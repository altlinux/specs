Name: gxmessage
Version: 2.20.0
Release: alt1

Summary: GTK2 based xmessage clone
License: GPL
Group: System/X11

Url: http://homepages.ihug.co.nz/~trmusson/programs.html#gxmessage
Source: %name-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel perl-XML-Parser pkg-config
BuildRequires: intltool libgtk+2-devel

%description
A GTK2 based xmessage clone, gxmessage tries to be
as compatible as possible. You might like it if you're
running a mostly GTK desktop.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_liconsdir/*
%_infodir/*
%_man1dir/*
%doc README NEWS TODO AUTHORS ChangeLog examples/

%changelog
* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 2.20.0-alt1
- 2.20.0

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 2.12.4-alt1
- 2.12.4 (thanks fedorawatch)
- spec cleanup

* Thu Oct 11 2007 Eugene V. Horohorin <genix@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Jul 16 2006 Eugene V. Horohorin <genix@altlinux.ru> 2.6.1-alt2
- conflict with mike's -alt1 $)

* Sat Jul 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Jan 27 2006 Eugene V. Horohorin <genix@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Nov 29 2004 Eugene V. Horohorin <genix@altlinux.ru> 2.4.0-alt1
- new version

* Sat Sep 25 2004 Eugene V. Horohorin <genix@altlinux.ru> 2.0.11-alt1
- new version

* Fri Mar 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 2.0.10-alt1
- implementation build


