# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
%global _name   mate_menu
%global _internal_version 7af4f232dc12
%global _internal_name ubuntu-mate-mate-menu
%global _internal_sitelib_version 17.10.1

Name:           mate-menu
Version:        17.10.1
Release:        alt1_4
Summary:        Advanced Menu for the MATE Desktop
Group:          Shells
# mate_menu/keybinding.py use MIT license and the rest is under GPLv2+
License:        GPLv2+ and MIT
BuildArch:      noarch
Url:            https://bitbucket.org/ubuntu-mate/mate-menu
# download link
#Source:         https://bitbucket.org/ubuntu-mate/%{name}/get/%{version}.tar.bz2
Source:          %{_internal_name}-%{_internal_version}.tar.bz2

Patch1:         mate-menu_adjust-package-manager.patch
Patch2:         mate-menu_default-applications.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python-devel >= 2.7
BuildRequires:  python-module-distutils-extra
BuildRequires:  python-module-setuptools
BuildRequires:  desktop-file-utils

Requires:       mate-menus
Requires:       mate-menu-editor
Requires:       python-module-configobj
%if 0%{?fedora} && 0%{?fedora} <= 27
Requires:       python-module-pygobject3
%else
Requires:       python-module-pygobject3
%endif
Requires:       python-module-pyxdg
Requires:       python-module-xlib
Requires:       beesu
Requires:       mate-panel
Source44: import.info


%description
An advanced menu for MATE. Supports filtering, favorites,
auto-session, and many other features.
This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.


%prep
%setup -q -n %{_internal_name}-%{_internal_version}

# xdg-su isn't available in fedora
sed -i 's/xdg-su/beesu/g' %{_name}/execute.py
#some python fixes
sed -i 's/#!\/usr\/bin\/env python2/#!\/usr\/bin\/python2/g' lib/%{name}.py
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python2/g' lib/%{name}-config.py

%patch1 -p1 -b .adjust-package-manager
%patch2 -p1 -b .default-applications

%build
%python_build

%install
%python_install

# avoid rpmlint invalid-lc-messages-dir and incorrect-locale-subdir errors
rm -rf %{buildroot}%{_datadir}/locale/ber
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/nah/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/

%find_lang %{name}


%post
/bin/touch --no-create %{_datadir}/mate-menu &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/mate-menu &>/dev/null

fi

%files -f %{name}.lang
%doc README.md
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{python_sitelibdir_noarch}/%{_name}/
%{python_sitelibdir_noarch}/%{_name}-%{version}-py2.7.egg-info/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.mate.mate-menu*.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateMenuAppletFactory.service
%{_mandir}/man1/mate-menu.1.*


%changelog
* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 17.10.1-alt1_4
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 17.10.1-alt1_2
- new fc release

* Wed Oct 26 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 16.10.1-alt1_2
- import to Sisyphus

