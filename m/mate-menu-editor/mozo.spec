Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname mozo
%define fedora 21
Name:           mate-menu-editor
Version:        1.8.0
Release:        alt1_1
Summary:        MATE Desktop menu editor
License:        LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.8/%{oldname}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  mate-menus-devel
BuildRequires: python-module-pygobject python-module-pygobject-devel
BuildRequires:  python-devel

Requires:       mate-menus

%if 0%{?fedora} && 0%{?fedora} > 20
%endif

BuildArch:  noarch
Patch33: alacarte-0.13.2-alt-xfce.patch
Source44: import.info

%description
MATE Desktop menu editor

%prep
%setup -n %{oldname}-%{version} -q
%patch33 -p1
#NOCONFIGURE=1 ./autogen.sh


%build
%configure

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                                  \
        --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mozo.desktop

%find_lang %{oldname} --with-gnome --all-name


%files -f %{oldname}.lang
%doc AUTHORS COPYING README
%{_bindir}/mozo
%{_datadir}/icons/hicolor/*x*/apps/mozo.png
%{_datadir}/mozo/
%{_datadir}/applications/mozo.desktop
%{_mandir}/man1/mozo.1.*
%{python_sitelibdir_noarch}/Mozo/


%changelog
* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

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

