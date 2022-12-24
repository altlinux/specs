# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen pkgconfig(bluez) pkgconfig(libmtp)
# END SourceDeps(oneline)
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%filter_from_provides /^pkgconfig.libdivecomputer./d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major       0
%define libname     libdivecomputer-subsurface%{major}
%define develname   libdivecomputer-subsurface-devel

%define major_orig       0
%define libname_orig     libdivecomputere%{major_orig}
%define develname_orig   libdivecomputer-devel

# disable debuginfo, it's empty anyway due to static-only library
%global debug_package   %{nil}

Name:           libdivecomputer-subsurface
Summary:        Library for communication with dive computers
Version:        5.0.10
Release:        alt1_1
# includes "Public domain" portions from https://github.com/kokke/tiny-AES128-C :
# aes.c
License:        LGPLv2+
Group:          Development/C
URL:            http://git.subsurface-divelog.org/index.cgi?p=libdc.git
Source0:        https://subsurface-divelog.org/downloads/libdivecomputer-subsurface-branch-%{version}.tgz

BuildRequires:  libusb-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
Source44: import.info

%description
Libdivecomputer is a cross-platform and open source library for
communication with dive computers from various manufacturers.

%package -n %{develname}
Summary:    Header files and development libraries for %{name}
Group:      Development/C
Provides:   divecomputer-subsurface-devel = %{version}-%{release}
Conflicts:  %{develname_orig}

%description -n %{develname}
Header files and development libraries for %{name}.

%prep
%setup -q -n libdivecomputer-subsurface-branch-%{version}

%build
# generate configure
autoreconf -fi

%configure \
  --disable-doc \
  --disable-silent-rules \
  --disable-shared \
  --enable-static

%make_build

%install
%makeinstall_std

# fix version in libdivecomputer.pc
sed -i -e 's,^Version.*,Version: %{version},' \
	%{buildroot}%{_libdir}/pkgconfig/libdivecomputer.pc

## unpackaged files
rm -f %{buildroot}%{_bindir}/dctool
rm -f %{buildroot}%{_libdir}/lib*.la

%files -n %{develname}
%doc NEWS README
%doc --no-dereference COPYING
%{_includedir}/libdivecomputer/
%{_libdir}/libdivecomputer.a
%{_libdir}/pkgconfig/libdivecomputer.pc



%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_1
- update by mgaimport

* Thu Apr 14 2022 Igor Vlasenko <viy@altlinux.org> 5.0.8-alt1_1
- update by mgaimport

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 5.0.3-alt1_1
- fixed build with LTO

* Fri Apr 16 2021 Igor Vlasenko <viy@altlinux.org> 5.0.1-alt1_1
- update by mgaimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 4.9.10-alt1_1
- new version

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 4.9.6-alt1_1
- update by mgaimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.9.4-alt1_1
- update by mgaimport

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.9.3-alt1_1
- update by mgaimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 4.9.1-alt1_1
- update by mgaimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 4.8.6-alt1_1
- update by mgaimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 4.8.5-alt1_1
- update by mgaimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 4.8.3-alt1_1
- update by mgaimport

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 4.7.8-alt1_1
- new version

