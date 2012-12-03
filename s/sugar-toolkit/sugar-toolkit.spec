# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 libICE-devel pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(ice) python-devel
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Sugar toolkit
Name: sugar-toolkit
Version: 0.96.3
Release: alt1_2
URL: http://wiki.laptop.org/go/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
Source1: macros.sugar
License: LGPLv2+
Group: System/Libraries

Patch0: presence-RoomConfig1.patch

BuildRequires: libalsa-devel
BuildRequires: gettext-devel
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: python-module-pygtk-devel

Requires: dbus-python
Requires: gettext
Requires: python-module-pygnome-desktop
Requires: python-module-hippo-canvas
Requires: pygtk2
Requires: python-module-simplejson
Requires: python-module-dateutil
Requires: sugar-base
Requires: sugar-datastore
Requires: sugar-presence-service
Requires: unzip
Source44: import.info

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_sysconfdir}/rpm/

%find_lang %name

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# hack: move arch-dependent py+so
%ifarch x86_64
mkdir -p %{buildroot}%{python_sitelibdir}/
mv %{buildroot}%{python_sitelibdir_noarch}/* %{buildroot}%{python_sitelibdir}/
%endif


%files -f %{name}.lang
%doc COPYING README
%{python_sitelibdir}/*

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.3-alt1_2
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.1-alt1_1
- new version; import from fc17 release

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88.0-alt1.1
- Rebuild with Python-2.7

* Wed Apr 07 2010 Aleksey Lim <alsroot@altlinux.org> 0.88.0-alt1
- Sucrose 0.88.0 release

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84.4-alt1.1
- Rebuilt with python 2.6

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.4-alt1
- update Sucrose to 0.84.2 version

* Tue Mar 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.0-alt1
- update Sucrose to 0.84.0 version

* Sun Feb 15 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.6-alt1
- new Sucrose 0.83.5 release

* Tue Jan 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.4-alt1
- new Sucrose 0.83.4 release

* Tue Dec 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt1
- new upstream release

* Tue Dec 16 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.2-alt2
- use python-module-pygtk package instead of pygtk2
- sugar #11 fix

* Fri Dec 12 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.2-alt1
- Sugar 0.84 release cycle

* Mon Dec 01 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.5-alt3
- add xorg-xextproto-devel dependence

* Sun Nov 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.5-alt2
- change group tag to "Graphical desktop/Sugar"
- make all links to child packages hard

* Tue Nov 18 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.5-alt1
- first build for ALT Linux Sisyphus
