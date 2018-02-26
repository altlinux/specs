BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:      mingw-win-iconv
Version:   0.0.3
Release:   alt1_4
Summary:   Iconv implementation using Win32 API

License:   Public Domain
Group:     System/Libraries
URL:       http://code.google.com/p/win-iconv
Source0:   http://win-iconv.googlecode.com/files/win-iconv-%{version}.tar.bz2
# rename libiconv.dll -> iconv.dll to match the .def file
Patch0:    win-iconv-0.0.3-dllname.patch
BuildArch: noarch

BuildRequires: mingw32-filesystem >= 68
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-runtime

BuildRequires: cmake >= 2.8.0
BuildRequires: dos2unix
Source44: import.info


%description
MinGW Windows Iconv library


%package -n %{_mingw32_pkg_name}
Group: System/Libraries
Summary:        MinGW Windows Iconv library

%description -n %{_mingw32_pkg_name}
MinGW Windows cross compiled Iconv library.


%package -n %{_mingw32_pkg_name}-static
Group: System/Libraries
Summary:        Static version of the MinGW Windows Iconv library
Requires:       mingw32-win-iconv = %{version}-%{release}

%description -n %{_mingw32_pkg_name}-static
Static version of the MinGW Windows Iconv library.


%{?_mingw32_debug_package}


%prep
%setup -q -n win-iconv-%{version}
%patch0 -p1 -b .dllname

dos2unix readme.txt
dos2unix ChangeLog
chmod -x readme.txt
chmod -x ChangeLog


%build
%{_mingw32_cmake} -DBUILD_STATIC=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_mingw32_bindir}/*.exe


%files -n %{_mingw32_pkg_name}
%doc ChangeLog readme.txt
%{_mingw32_bindir}/iconv.dll
%{_mingw32_includedir}/iconv.h
%{_mingw32_libdir}/libiconv.dll.a

%files -n %{_mingw32_pkg_name}-static
%{_mingw32_libdir}/libiconv.a


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_4
- dropped obsoletes on mingw32-iconv

