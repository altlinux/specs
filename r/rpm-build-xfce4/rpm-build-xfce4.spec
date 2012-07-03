Name: rpm-build-xfce4
Version: 0.1.0
Release: alt2

Summary: Macros for comfort build xfce4 and plugins
Summary(ru_RU.UTF-8): Макросы для удобной сборки Xfce
Group: Graphical desktop/XFce
License: Public Domain
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: xfce4.macros

Requires: xfce4-dev-tools >= 4.8.0-alt2

BuildArch: noarch

%description
Some macros for standard path for xfce4.

%description -l ru_RU.UTF-8
Некоторые макросы, необходимые для сборки Xfce.

%install
mkdir -p %buildroot/etc/rpm/macros.d
install -m644 %SOURCE0 %buildroot/etc/rpm/macros.d/xfce4

%files
/etc/rpm/macros.d/xfce4

%changelog
* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2
- Fix summary and description (by Igor Zubkov).

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Update macroses.
- Use xdt-autogen in %%xfce4reconf macros.

* Mon Jun 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.0.1-alt2
- Added russian 'summary' and 'description' sections.

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.0.1-alt1
- add %%xfce4reconf macros

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.1-alt0.1
- first build
