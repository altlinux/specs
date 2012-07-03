BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-libsigc++20
Version:        2.2.9
Release:        alt1_1
Summary:        MinGW Windows port of the typesafe signal framework for C++

License:        LGPLv2+
Group:          System/Libraries
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.2/libsigc++-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  m4

Requires:       pkgconfig
Source44: import.info


%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, %name is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses %name.


%{?_mingw32_debug_package}


%prep
%setup -q -n libsigc++-%{version}


%build
%{_mingw32_configure} --disable-static --disable-documentation
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
chmod a-x $RPM_BUILD_ROOT/%{_mingw32_libdir}/libsigc-2.0.dll.a
chmod a-x $RPM_BUILD_ROOT/%{_mingw32_libdir}/libsigc-2.0.la

%files
%doc COPYING
%{_mingw32_bindir}/libsigc-2.0-0.dll
%{_mingw32_libdir}/libsigc-2.0.dll.a
%{_mingw32_libdir}/libsigc-2.0.la
%{_mingw32_libdir}/pkgconfig/sigc++-2.0.pc
%{_mingw32_includedir}/sigc++-2.0
%{_mingw32_libdir}/sigc++-2.0


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt1_1
- initial release by fcimport

