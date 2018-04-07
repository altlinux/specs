# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#

%define rel 4

Summary:        asynchronous REST C++11 library
Name:           restbed
Version: 4.0
Release:        alt1_%rel
License:        GPLv2+
Group:          System/Base
URL:            http://www.corvusoft.co.uk
Source0:        https://github.com/Corvusoft/restbed/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         version-so.patch
Patch1:         usr-lib.patch
ExcludeArch:    armv5tl

BuildRequires:  ccmake cmake ctest
BuildRequires:  asio-devel
BuildRequires:  pkgconfig(openssl)
Source44: import.info

%description
Corvusoft's Restbed framework brings asynchronous RESTful functionality
to C++11 applications.

#--------------------------------------------------------------------

%define major 0
%define librestbed librestbed%{major}

%package -n %librestbed
Summary:        asynchronous REST C++11 library
Group:          System/Libraries

%description -n %librestbed
asynchronous REST C++11 library.

%files -n %librestbed
%{_libdir}/librestbed.so.%{major}*

#--------------------------------------------------------------------

%define librestbed_devel librestbed-devel

%package -n %librestbed_devel
Summary:        Devel stuff for %name
Group:          Development/Other
Requires:       %librestbed >= %{version}-%{release}
Provides:       %name-devel = %{version}-%{release}

%description -n %librestbed_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %librestbed_devel
%_includedir/corvusoft/restbed
%_includedir/restbed
%_libdir/librestbed.so

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -e 's,MGALIB,%{_libdir},g' -i CMakeLists.txt

%build
%{mageia_cmake} -DBUILD_SHARED=ON
%make_build

%install
%makeinstall_std -C build


%changelog
* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_4
- new version

