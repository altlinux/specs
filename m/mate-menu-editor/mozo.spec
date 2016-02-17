Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache pkgconfig(libmate-menu) pkgconfig(pygobject-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname mozo
%define fedora 22
Name:           mate-menu-editor
Version:        1.12.0
Release:        alt1_1
Summary:        MATE Desktop menu editor
License:        LGPLv2+
URL:            http://mate-desktop.org
# source is from gtk3 branch at http://git.mate-desktop.org/mozo/?h=gtk3
Source0:        https://raveit65.fedorapeople.org/Mate/SOURCE/%{oldname}-gtk3-%{version}.tar.xz

# rhbz (#1202674)
# https://github.com/infirit/mozo/commit/acf2f98
Patch0:         mozo_Use-Gtk-selection-mode.patch

BuildRequires:  desktop-file-utils
BuildRequires:  mate-common 
BuildRequires:  mate-menus-devel
BuildRequires:  python-module-pygobject3-devel
BuildRequires:  python-devel

Requires:       mate-menus

%if 0%{?fedora} && 0%{?fedora} > 20
%endif

BuildArch:  noarch
Patch33: mozo-gtk3-1.12.0-alt-xfce.patch
Source44: import.info

%description
MATE Desktop menu editor

%prep
%setup -n %{oldname}-%{version} -qn %{oldname}-gtk3-%{version}
%patch33 -p1
#NOCONFIGURE=1 ./autogen.sh

# disable for gtk3
# %patch0 -p1 -b .selection-mode

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
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt2_2
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_2
- new version

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

