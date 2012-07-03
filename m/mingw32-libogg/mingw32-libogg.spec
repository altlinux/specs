BuildRequires: rpm-build-mingw32
%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}

Summary:        The Ogg bitstream file format library
Name:           mingw32-libogg
Version:        1.1.4
Release:        alt2_3
Group:          System/Libraries
License:        BSD
URL:            http://www.xiph.org/
Source:         http://downloads.xiph.org/releases/ogg/libogg-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
Requires:       pkgconfig
Source44: import.info

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.


%prep
%setup -q -n libogg-%{version}

%build
sed -i "s/-O20/-O2/" configure
sed -i "s/-ffast-math//" configure
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
# zap docs, redundant with native package
rm -rf $RPM_BUILD_ROOT%{_mingw32_docdir}

%files
%doc AUTHORS CHANGES COPYING README
%{_mingw32_bindir}/libogg*
%{_mingw32_libdir}/libogg*
%{_mingw32_libdir}/pkgconfig/ogg.pc
%dir %{_mingw32_includedir}/ogg
%{_mingw32_includedir}/ogg/ogg.h
%{_mingw32_includedir}/ogg/os_types.h
%{_mingw32_includedir}/ogg/config_types.h
%{_mingw32_datadir}/aclocal/ogg.m4

%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_3
- bugfix release by fcimport

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_3
- initial release by fcimport

