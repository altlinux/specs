# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 10
%define libname libtifiles2_%{major}
%define develname libtifiles2-devel

Name:           libtifiles2
Version:        1.1.7
Release:        alt1_1
Summary:        Texas Instruments calculator files library

Group:          System/Libraries
License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        https://download.sourceforge.net/tilp/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel
BuildRequires:  zlib-devel
BuildRequires:  libticonv-devel
BuildRequires:  libarchive-devel
BuildRequires:  gettext-tools libasprintf-devel
Source44: import.info

%package i18n
Summary:        Internationalization and locale data for %{name}
Group:          System/Internationalization
BuildArch:      noarch
Conflicts:      libtifiles9 < 1.1.6-2

%description i18n
Internationalization and locale data for %{name}

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
Provides:       tifiles2-devel = %{version}-%{release}
Obsoletes:      %{_lib}tifiles-devel < 1.1.7


%description
The tifiles library is a library capable of reading, modifying,
and writing TI formatted files. It can also group/ungroup files.
This library is able to manipulate files in a fairly transparent
fashion. With this library, the developer does not have to worry
about the different file formats.

%description -n %{libname}
The tifiles library is a library capable of reading, modifying,
and writing TI formatted files. It can also group/ungroup files.
This library is able to manipulate files in a fairly transparent
fashion. With this library, the developer does not have to worry
about the different file formats.

%description -n %{develname}
Include files and libraries for developing applications that
make use of libtifiles.


%prep
%setup -q

rm po/fr.gmo

%build
autoreconf -vfi
%configure \
        --disable-static
%make_build

make -C po fr.gmo

%check
make check

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

#handle docs in files section
rm -rf %{buildroot}%{_docdir}

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%doc --no-dereference COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/libtifiles2.so.%{major}
%{_libdir}/libtifiles2.so.%{major}.*

%files -n %{develname}
%{_libdir}/libtifiles2.so
%{_libdir}/pkgconfig/tifiles2.pc
%{_includedir}/tilp2/*


%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.7-alt1_1
- new version

