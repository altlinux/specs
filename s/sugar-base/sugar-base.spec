# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Base Sugar library
Name: sugar-base
Version: 0.96.0
Release: alt1_1
URL: http://sugarlabs.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2
Group: System/Libraries

BuildRequires: python-devel
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-pygtk-devel
BuildRequires: gettext
BuildRequires: perl-XML-Parser
BuildRequires: intltool

Requires: python-module-decorator
Source44: import.info

%description

The base libary for Sugar, the user interface of the One Laptop Per
Child project. It provides helpers for the development of services and
activities.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

%find_lang %name

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# hack: move arch-dependent py+so
%ifarch x86_64
mkdir -p %{buildroot}%{python_sitelibdir}/
mv %{buildroot}%{python_sitelibdir_noarch}/* %{buildroot}%{python_sitelibdir}/
%endif


%files -f %{name}.lang
%{python_sitelibdir}/sugar

%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.0-alt1_1
- new version; import from fc17 release

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88.0-alt1.1
- Rebuild with Python-2.7

* Tue Apr 06 2010 Aleksey Lim <alsroot@altlinux.org> 0.88.0-alt1
- Sucrose 0.88.0 release

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84.1-alt2.1
- Rebuilt with python 2.6

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.1-alt2
- fix %files warnings

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.1-alt1
- update Sucrose to 0.84.2 version

* Tue Mar 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.0-alt1
- update Sucrose to 0.84.0 version

* Tue Jan 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt1
- new Sucrose 0.83.4 release

* Tue Dec 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.2-alt1
- remove pygtk2 dependency
- new upstream release

* Fri Dec 12 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.1-alt1
- Sugar 0.84 release cycle

* Sun Nov 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt2
- change group tag to "Graphical desktop/Sugar"

* Sat Nov 08 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt1
- first build for ALT Linux Sisyphus
