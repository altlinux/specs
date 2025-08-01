# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++ pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define commit 78a874b30a4c3161251b8e12ffb6443f29005eb3
%define gitrel  %(c=%{commit}; echo ${c:0:7})

%define major   4
%define libname libmirisdr%{major}
%define devname libmirisdr-devel

%define rel 2

Name:           libmirisdr
Version:        0.0.20240620
Release:        alt1_2.78a874b
Summary:        Support programs for MRi2500
License:        GPLv2
Group:          Communications
URL:            https://github.com/f4exb/libmirisdr-4/
##TODO Try a more recent fork e.g. https://github.com/ericek111/libmirisdr-5
Source0:        https://api.github.com/repos/ericek111/libmirisdr-5/tarball/%{gitrel}#/%{name}-%{version}.tar.gz
Patch0:         libmirisdr-cmake-4.0.patch

BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(libusb)
Source44: import.info

%description
Programs to control the Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n mirisdr-utils
Summary:        Support programs for MRi2500
License:        GPLv2
Group:          Communications

Obsoletes:      libmirisdr <= %{version}-%{release}

%description -n mirisdr-utils
Programs to control the Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n %{libname}
Summary:        SDR driver for MRi2500
Group:          System/Libraries

%description -n %{libname}
Library to run Mirics MRi2500 based DVB dongle as a SDR receiver.

%package -n %{devname}
Summary:        Development files for mirisdr
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
Library headers and other development files for mirisdr driver.

%prep
%setup -q -n ericek111-libmirisdr-5-%{gitrel}
%patch0 -p1


# remove buildtime from documentation
#sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' Doxyfile.in

# fix version in .pc
sed -i -e 's,\(^Version:\).*,\1 %{version},' libmirisdr.pc.in

# fix libdir in .pc
sed -i -e 's,\(^set(libdir \\${exec_prefix}/lib\),\1${LIB_SUFFIX},' CMakeLists.txt

%build
%{mageia_cmake} -DCMAKE_SKIP_INSTALL_RPATH=ON
%mageia_cmake_build

%install
%mageia_cmake_install

rm %{buildroot}%{_libdir}/libmirisdr.a

#install udev rules
install -Dpm644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

%files -n mirisdr-utils
%{_bindir}/miri_*

%files -n %{libname}
%{_udevrulesdir}/10-mirisdr.rules
%{_libdir}/libmirisdr.so.%{major}
%{_libdir}/libmirisdr.so.%{major}.*

%files -n %{devname}
%{_libdir}/libmirisdr.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libmirisdr.pc



%changelog
* Fri Aug 01 2025 Igor Vlasenko <viy@altlinux.org> 0.0.20240620-alt1_2.78a874b
- update by mgaimport

* Fri Mar 22 2024 Igor Vlasenko <viy@altlinux.org> 0.0.20230516-alt1_1.faf794b
- update by mgaimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.0.20130608-alt1_9
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_7
- fixed build

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_5
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_3
- new version

