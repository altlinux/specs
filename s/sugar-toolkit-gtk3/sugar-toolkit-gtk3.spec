# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/pygtk-codegen-2.0 libICE-devel libgtk+3-gir-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(ice)
# END SourceDeps(oneline)
# bootstrapping around sugar...
%set_verify_elf_method relaxed
BuildRequires: libXi-devel
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Sugar toolkit GTK+ 3
Name:    sugar-toolkit-gtk3
Version: 0.98.5
Release: alt1_1
URL:     http://wiki.laptop.org/go/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
Source1: macros.sugar
License: LGPLv2+
Group:   System/Libraries

BuildRequires: libalsa-devel
BuildRequires: gettext-devel
BuildRequires: libgtk+3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: python-devel
BuildRequires: python-module-pygtk-devel
BuildRequires: python-module-pygobject-devel

Requires: gettext
Requires: sugar-datastore
Requires: unzip
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%setup -q

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
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*
%{_bindir}/sugar-activity

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.98.5-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.5-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.1-alt1_1
- new version; import from fc17 release

