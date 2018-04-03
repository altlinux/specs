# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/clang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 12
%define libname libticalcs2_%{major}
%define develname libticalcs2-devel

Name:           libticalcs2
Version:        1.1.9
Release:        alt1_1
Summary:        Texas Instruments calculator communication library

Group:          System/Libraries
License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        https://download.sourceforge.net/tilp/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel
BuildRequires:  libticonv-devel
BuildRequires:  libticables2-devel
BuildRequires:  libtifiles2-devel
BuildRequires:  gettext-tools libasprintf-devel
Source44: import.info

%package i18n
Summary:        Internationalization and locale data for %{name}
Group:          System/Internationalization
BuildArch:      noarch
Conflicts:      libticalcs11 < 1.1.8-2

%description i18n
Internationalization and locale data for %{name}.

%package -n %{libname}
Group:          System/Libraries
Summary:        Texas Instruments calculators files library
Provides:       %{name} = %{version}-%{release}
Requires:       %{name}-i18n >= %{version}-%{release}

%package -n %{develname}
Group:          Development/C
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       ticalcs2-devel = %{version}-%{release}
Obsoletes:      %{_lib}ticalcs-devel < 1.1.9

%description
The ticalcs library is a library which brings about all the
functions needed to communicate with a Texas Instruments
graphing calculator (or hand-held).

%description -n %{libname}
The ticalcs library is a library which brings about all the
functions needed to communicate with a Texas Instruments
graphing calculator (or hand-held). Currently, it does not
support some education devices (such as CBL/CBR and others).
This library is able to communicate with handhelds in a fairly
transparent fashion. With this library, the developer does not
have to worry about the packet oriented protocol, the file
management and some other stuff.

%description -n %{develname}
Include files and libraries for developing applications
to work with libticalcs.

%prep
%setup -q

rm po/fr.gmo

%build
autoreconf -vfi
%configure --disable-static
%make_build

make -C po fr.gmo

%check
make -C tests check

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%doc README AUTHORS ChangeLog
%doc --no-dereference COPYING
%{_libdir}/libticalcs2.so.%{major}
%{_libdir}/libticalcs2.so.%{major}.*

%files -n %{develname}
%{_includedir}/tilp2/*
%{_libdir}/pkgconfig/ticalcs2.pc
%{_libdir}/libticalcs2.so


%changelog
* Tue Apr 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.9-alt1_1
- new version

