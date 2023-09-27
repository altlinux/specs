Name: rpm-build-xfce4
Version: 0.2.0
Release: alt1

Summary: comfort build environment for xfce4 and plugins
Summary(ru_RU.UTF-8): Зависимости для удобной сборки Xfce
Group: Graphical desktop/XFce
License: Public Domain
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: xfce4.macros

Requires: xfce4-dev-tools >= 4.8.0-alt2
Requires: rpm-macros-xfce4 = %EVR

BuildArch: noarch

%description
Some macros for standard path for xfce4.

%description -l ru_RU.UTF-8
Некоторые макросы, необходимые для сборки Xfce.


%package -n rpm-macros-xfce4
Summary: Macros for comfort build xfce4 and plugins
Summary(ru_RU.UTF-8): Макросы для удобной сборки Xfce
Group: Graphical desktop/XFce
BuildArch: noarch
Conflicts: rpm-build-xfce4 <= 0.1.2-alt1

%description -n rpm-macros-xfce4
Some macros for standard path for xfce4.

%description -n rpm-macros-xfce4 -l ru_RU.UTF-8
Некоторые макросы, необходимые для сборки Xfce.

%install
mkdir -p %buildroot%_rpmmacrosdir
install -m644 %SOURCE0 %buildroot%_rpmmacrosdir/xfce4

%files

%files -n rpm-macros-xfce4
%_rpmmacrosdir/xfce4


%changelog
* Tue Sep 19 2023 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Add %%xfce4_cleanup_version() macro.

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt1
- NMU:
- use %%_rpmmacrosdir instead of /etc/rpm/macros.d
- added rpm-macros-xfce4 w/o dependencies on xfce4-dev-tools

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- xfce4reconf: Create m4/ directory.
- Drop commented _xfce4htmldoc macro.
- Fix Xfce name (XFCE -> Xfce).

* Tue Aug 28 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Add comment for xfce4reconf macros.
- Add xfce4_drop_gitvtag macros.

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
