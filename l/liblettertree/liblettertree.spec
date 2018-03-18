# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major	0
%define	libname	liblettertree%{major}
%define devname liblettertree-devel

Name:		liblettertree
Version:	0.1
Release:	alt1_12
Summary:	A letter tree data structure
License:	LGPL
Group:		System/Libraries
Source:		ftp://ftp.inria.fr/INRIA/Atoll/Guillaume.Rousse/%{name}-%{version}.tar.bz2
Source44: import.info

%description
This is a simple implementation of a lettertree, an efficient data structure
for storing and indexing string sharing a common prefix.

%package -n %{libname}
Summary:	A letter tree data structur
Group:		System/Libraries

%description -n	%{libname}
This is a simple implementation of a lettertree, an efficient data structure
for storing and indexing string sharing a common prefix.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lettertree-devel = %{version}-%{release}
Obsoletes:	%{_lib}lettertree0-devel < 0.1-8

%description -n	%{devname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_includedir}/lettertree.h





%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_12
- new version

