Name: obtheme
Version: 0.7
Release: alt1.1

Summary: A GUI theme editor for Openbox
License: GPLv2+
Group: Graphical desktop/Other
Url: http://xyne.archlinux.ca/info/obtheme

Source0: %name-%version.tar.gz
Source1: obtheme.desktop

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch
Requires: python-module-fuse python-module-pygtk

%description
A GUI theme editor for Openbox.

%prep
%setup -q -n %name

%build

%install
%__install -D -m755 %name %buildroot%_bindir/%name
%__install -D -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Radik Usupov <radik@altlinux.org> 0.7-alt1
- New version (0.7)

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 0.6-alt1
- 0.5.9 -> 0.6

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 0.5.9-alt1
- 0.5.4 -> 0.5.9

* Wed Aug 05 2009 Igor Zubkov <icesik@altlinux.org> 0.5.4-alt1
- build


