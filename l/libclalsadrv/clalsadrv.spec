# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname clalsadrv

Summary:       ALSA driver C++ Library
Name:          libclalsadrv
Version:       2.0.0
Release:       alt1_5
License:       GPLv2+
Group:         System/Libraries
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{oldname}-%{version}.tar.bz2

Obsoletes:     alsadrv <= 0.0.2
Provides:      alsadrv > 0.0.2
BuildRequires: libalsa-devel
Source44: import.info
Provides: clalsadrv = %{version}-%{release}

%description
ALSA driver C++ access library

%package       devel
Summary:       ALSA driver C++ access library
Group:         Development/C
Requires:      %{name}%{?_isa} = %{version}-%{release}

Obsoletes:     alsadrv-devel <= 0.0.2
Provides:      alsadrv-devel > 0.0.2
Provides: clalsadrv-devel = %{version}-%{release}

%description devel
ALSA driver C++ access library. This package includes the development
tools.

%prep
%setup -n %{oldname}-%{version} -q

%build
cd libs
sed -i -e "s|/sbin/ldconfig|# /sbin/ldconfig|g" \
       -e "s|-O2|%{optflags}|g" Makefile
make %{?_smp_mflags} LIBDIR=%{_lib}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cd libs
make PREFIX=%{buildroot}%{_prefix} LIBDIR=%{_lib} install
ln -s lib%{oldname}.so.2.0.0 %{buildroot}%{_libdir}/lib%{oldname}.so.2

%files
%doc AUTHORS COPYING
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}.h
%{_libdir}/lib%{oldname}.so

%changelog
* Thu Jan 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_5
- fc import

