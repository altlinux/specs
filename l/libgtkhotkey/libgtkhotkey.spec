%define oname gtkhotkey
Name: lib%oname
Version: 0.1
Release: alt1.qa1

Summary: Cross Platform Library For Using Desktop Wide Hotkeys

License: LGPLv3
Group: Development/C
Url: http://www.grillbar.org/wordpress/?p=250

Source: http://grillbar-org/%oname-%version/%oname-%version.tar.gz
Patch: %oname-%version-notest-alt.patch

BuildRequires: libgtk+2-devel >= 2.13 glib2-devel >= 2.15.6 gtk-doc perl-XML-Parser

%description
I wrote GtkHotkey because I needed a platform independent way to manage and
bind desktop hotkeys. Gnome applications can register hotkeys via GConf and
Metacity, but I wanted desktop neutrality and more flexibility.

The idea of the library is to keep it as simple as possible, while sticking
to an object oriented design, without falling back to C-isms (read: '#ifdefs')
where it would otherwise be tempting.

%package devel
Summary: Development files for lib%name
Group: Development/C

%description devel
This package contains development files required
in development of the lib%name-based applications.

%prep
%setup -q -n %oname-%version
%patch -p1

%build
%configure --disable-static
%make_build

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so
%_datadir/gtk-doc/html/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Mar 25 2009 Yury Aliaev <mutabor@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
