Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-menu-editor
Version:        1.5.0
Release:        alt2_2
Summary:        MATE Desktop menu editor
License:        LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  mate-menus-devel
BuildRequires: python-module-pygobject python-module-pygobject-devel
BuildRequires:  python-devel

Requires:  mate-desktop

BuildArch:  noarch
Source44: import.info

%description
MATE Desktop menu editor

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh


%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%find_lang %{name} --all-name


desktop-file-install                                  \
        --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mozo.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mozo.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mozo
%{_datadir}/icons/hicolor/*x*/apps/mozo.png
%{_datadir}/mozo
%{_datadir}/applications/mozo.desktop
%{python_sitelibdir_noarch}/Mozo

%changelog
* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_2
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
- dropped obsolete dependencies on mate 1.4.x stuff

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- new release

