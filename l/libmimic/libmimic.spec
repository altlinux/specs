# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 0
%define libname libmimic%{major}
%define develname libmimic-devel

Summary:	Audio/Video Conference software for Instant Messengers
Name:		libmimic
Version:	1.0.4
Release:	alt1_14
License:	LGPLv2+
Url:		http://sourceforge.net/projects/farsight/
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/farsight/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.0.4-fix-underlinking.patch
BuildRequires:	glib2-devel
Source44: import.info

%description
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n %libname
Group: System/Libraries
Summary:Audio/Video Conference software for Instant Messengers
Obsoletes: libmimic

%description -n %libname
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n %develname
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
Headers of %{name} for development.


%prep
%setup -q
%patch0 -p1

%build

%configure --disable-static
%make

%install
%{makeinstall_std}

# don't ship .la
find %{buildroot} -name *.la | xargs rm -f

%files -n %{libname}
%{_libdir}/libmimic.so.%{major}*

%files -n %develname
%{_includedir}/mimic.h
%{_libdir}/libmimic.so
%{_libdir}/pkgconfig/libmimic.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_14
- new version

