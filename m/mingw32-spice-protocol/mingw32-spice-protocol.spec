BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-spice-protocol
Version:        0.8.0
Release:        alt1_1
Summary:        Spice protocol header files
Group:          System/Libraries
License:        BSD
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 49
Requires:       pkgconfig
Source44: import.info

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%setup -q -n spice-protocol-%{version}

%build
%{_mingw32_configure}
make

%install
make DESTDIR=%{buildroot} install

%files
%doc COPYING NEWS
%{_mingw32_includedir}/spice-1
%{_mingw32_datadir}/pkgconfig/spice-protocol.pc

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_1
- initial release by fcimport

