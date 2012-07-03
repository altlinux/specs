BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

%global nativename proj

Name:      mingw32-%{nativename}
Version:   4.6.1
Release:   alt1_5
Summary:   Cartographic projection software (PROJ.4)

Group:     Engineering
License:   MIT
URL:       http://proj.osgeo.org
Source0:   http://download.osgeo.org/proj/proj-%{version}.tar.gz
BuildArch: noarch

BuildRequires: libtool
BuildRequires:  mingw32-filesystem >= 35
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

Patch:    proj-noundefined.patch
Source44: import.info

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/

%prep
%setup -q -n %{nativename}-%{version}

%patch -p 1

%build
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Remove libtool archives
rm $RPM_BUILD_ROOT%{_mingw32_libdir}/libproj.la

# Remove inverse program symbolic links
rm $RPM_BUILD_ROOT%{_mingw32_bindir}/inv*.exe

# Remove unneeded files
rm -R $RPM_BUILD_ROOT%{_mingw32_datadir}/*

%check

%files
%doc NEWS AUTHORS COPYING README ChangeLog
%{_mingw32_bindir}/libproj-0.dll
%{_mingw32_bindir}/*.exe
%{_mingw32_libdir}/libproj.dll.a 
%{_mingw32_includedir}/*.h

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt1_5
- initial release by fcimport

