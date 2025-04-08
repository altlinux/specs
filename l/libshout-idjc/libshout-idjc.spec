BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	3
%define libname	libshout-idjc%{major}
%define devname	libshout-idjc-devel

Name:		libshout-idjc
Version:	2.4.6
Release:	alt1_1
Summary:	Libshout with extensions for IDJC
Group:		System/Libraries
License:	LGPL-2.1+
URL:		https://sourceforge.net/projects/libshoutidjc.idjc.p/
Source0:	https://downloads.sf.net/libshoutidjc.idjc.p/libshout-idjc-%{version}-r1.tar.gz
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(openssl)
Source44: import.info

%description
This is a modified version of libshout, with extensions for IDJC.

%package -n shoutidjc
Summary:	Broadcast streaming library with IDJC extensions (source client)
Group:		Development/Tools

%description -n shoutidjc
Broadcast streaming library with IDJC extensions (source client).

%package -n %{libname}
Summary:	Libshout with extensions for IDJC
Group:		System/Libraries

%description -n %{libname}
This is a modified version of libshout, with extensions for IDJC.

%package -n %{devname}
Summary:	Development files for libshout with extensions for IDJC
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	shout-idjc-devel = %{version}-%{release}
Conflicts: libshout2-devel

%description -n %{devname}
Libshout-idjc is a modified version of libshout, with extensions for IDJC.
This package contains the development files for the library.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

rm -rf %{buildroot}%{_datadir}/doc/libshout-idjc/COPYING

# we don't have ckport tool ATM
rm -rf %{buildroot}%{_libdir}/ckport/
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin,/usr/games} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files -n shoutidjc
%{_bindir}/shoutidjc
%{_mandir}/man1/shoutidjc.1*

%files -n %{libname}
%doc --no-dereference COPYING
%docdir %{_datadir}/doc/libshout-idjc
%doc %{_datadir}/doc/libshout-idjc/
%{_libdir}/libshout-idjc.so.%{major}
%{_libdir}/libshout-idjc.so.%{major}.*

%files -n %{devname}
%docdir %{_datadir}/doc/libshout-idjc
%doc %{_datadir}/doc/libshout-idjc/
%{_includedir}/shoutidjc
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc


%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 2.4.6-alt1_1
- update by mgaimport

* Thu Mar 02 2023 Igor Vlasenko <viy@altlinux.org> 2.4.3-alt1_3
- added conflict (closes: #45452)

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 2.4.3-alt1_2
- update by mgaimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.4.1-alt1_5
- update by mgaimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_4
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1
- new version

