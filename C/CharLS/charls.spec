# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define oldname charls
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name charls
%define major		2
%define libname		lib%{name}%{major}
%define develname	lib%{name}-devel

Name:		CharLS
Version:	2.0.0
Release:	alt1_3
Summary:	An optimized implementation of the JPEG-LS standard
Group:		System/Libraries
License:	BSD
URL:		https://github.com/team-charls/charls
Source0:	https://github.com/team-charls/charls/archive/%{version}/%{oldname}-%{version}.tar.gz
BuildRequires:	ccmake cmake ctest
BuildRequires:	dos2unix
Source44: import.info

%description
An optimized implementation of the JPEG-LS standard for loss less and 
near loss less image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

JPEG-LS (ISO-14495-1/ITU-T.87) is a standard derived from the Hewlett Packard
LOCO algorithm. JPEG LS has low complexity (meaning fast compression) and high
compression ratios, similar to JPEG 2000. JPEG-LS is more similar to the old
loss less JPEG than to JPEG 2000, but interestingly the two different
techniques result in vastly different performance characteristics.

#----------------------------------------------------

%package -n %{libname}
Summary:	An optimized implementation of the JPEG-LS standard
Group:		System/Libraries
Provides:	%{oldname} = %{?epoch:%epoch:}%{version}-%{release}
Provides:	CharLS = %{?epoch:%epoch:}%{version}-%{release}
Obsoletes:	CharLS < 1.0-6

%description -n %{libname}
An optimized implementation of the JPEG-LS standard for loss less and 
near loss less image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

JPEG-LS (ISO-14495-1/ITU-T.87) is a standard derived from the Hewlett Packard
LOCO algorithm. JPEG LS has low complexity (meaning fast compression) and high
compression ratios, similar to JPEG 2000. JPEG-LS is more similar to the old
loss less JPEG than to JPEG 2000, but interestingly the two different
techniques result in vastly different performance characteristics.

#----------------------------------------------------

%package -n %{develname}
Summary:	Libraries and headers for CharLS
Group:		Development/C
Requires:	%{libname} = %{?epoch:%epoch:}%{version}-%{release}
Provides:	%{oldname}-devel = %{?epoch:%epoch:}%{version}-%{release}
Provides:	CharLS-devel = %{?epoch:%epoch:}%{version}-%{release}
Obsoletes:	CharLS-devel < 1.0-6

%description -n %{develname}
CharLS - An optimized implementation of the JPEG-LS standard.

This package contains development libraries and headers for CharLS.

#----------------------------------------------------

%prep
%setup -n %{oldname}-%{version} -q

%build
%{mageia_cmake} -DBUILD_TESTING=ON
%mageia_cmake_build

%install
%mageia_cmake_install

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
ctest ./src

%files -n %{libname}
%{_libdir}/libCharLS.so.%{major}*

%files -n %{develname}
%doc README.md
%doc --no-dereference License.txt
%{_includedir}/CharLS/
%{_libdir}/libCharLS.so


%changelog
* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_3
- new version

* Sun Jan 12 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- fix build

* Wed Nov 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- first build for ALT Linux
