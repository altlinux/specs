# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/db2html /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/xsltproc docbook-dtds docbook-style-xsl gobject-introspection-devel libgtk+2-gir-devel pkgconfig(gladeui-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name gtkextra
%define major	8
%define api	3.0
%define libname	lib%{name}-x11_%{api}_%{major}
%define devname	lib%{name}-x11-devel

Name:		gtkextra
Summary:	A library of gtk+ widgets
Version:	3.3.4
Release:	alt1_1
License:	LGPLv2
Group:		System/Libraries
URL:		http://sourceforge.net/projects/gtkextra
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gtkextra-3.0.5-mga-format_security.patch

BuildRequires:	pkgconfig(gtk+-x11-2.0)
Source44: import.info

%description
GtkExtra is a useful set of widgets for creating GUI's for the Xwindows system
using GTK+. You can use it complementary to GTK+ and it is written in C.
The library includes: GtkSheet, GtkPlot, GtkIconList, GtkDirTree GtkFileList,
GtkIconFileSelection. GtkItemEntry, GtkFontCombo, GtkComboBox, GtkColorCombo,
GtkBorderCombo and GtkCheckItem.

%package -n %{libname}
Summary:	A library of gtk+ widgets
Group:		System/Libraries

%description -n %{libname}
The gtk+extra package includes the libraries.

%package -n %{devname}
Summary:	Development files for gtkextra
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The gtk+extra-devel package includes the static libraries, header files,
and documentation for compiling programs that use gtk+extra widgets.

%prep
%setup -q
#autopatch -p1

%build
%configure \
  --disable-static
# This is ignored and html is installed to %%{name}-3 so we move it
#  --htmldir=%%{buildroot}%%{_datadir}/gtk-doc/html/%%{name}/

%make

%install
%makeinstall_std
mv %{buildroot}/usr/share/gtk-doc/html/gtkextra-3 \
%{buildroot}/usr/share/gtk-doc/html/gtkextra

find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%{_libdir}/lib%{name}-x11-%{api}.so.%{major}
%{_libdir}/lib%{name}-x11-%{api}.so.%{major}.*

%files -n %{devname}
%doc README docs/*.ChangeLog
%{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-x11-%{api}.so
%{_includedir}/%{name}-%{api}/


%changelog
* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.4-alt1_1
new version

