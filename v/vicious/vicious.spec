Name: vicious
Version: 2.0.0
Release: alt1

Summary: Vicious is a modular widget library for "awesome" window manager
License: GPL2
Group: Graphical desktop/Other
Url: http://git.sysphere.org/vicious/
Source: %name-%version.tar
BuildArch: noarch
Requires: awesome >= 3.4

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
Vicious is a modular widget library for "awesome" window manager,
derived from the "Wicked" widget library. It has some of the old
Wicked widget types, a few of them rewritten, and a good number of
new widgets:


%prep
%setup -n %name-%version

%build

%install
mkdir -p %buildroot%_datadir/awesome/lib/%name
cp -v *.lua %buildroot%_datadir/awesome/lib/%name
cp -rv widgets %buildroot%_datadir/awesome/lib/%name

%files
%_datadir/awesome/lib/%name
%doc CHANGES README

%changelog
* Thu Apr 29 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Jan 10 2010 Terechkov Evgenii <evg@altlinux.ru> 1.0.22-alt1
- 1.0.22

* Sun Dec 27 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.21-alt1
- 1.0.21

* Sun Oct  4 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Tue Sep 22 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.15-alt1
- Initial build for ALT Linux Sisyphus
