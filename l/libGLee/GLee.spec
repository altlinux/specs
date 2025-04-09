BuildRequires: gcc-c++
Group: Development/C
%add_optflags %optflags_shared
%define oldname GLee
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 5

Name:           libGLee
Version:        %{major}.4.0
Release:        alt1_31
Summary:        GL Easy Extension library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://elf-stone.com/glee.php
Source0:        http://www.elf-stone.com/downloads/%{oldname}/%{oldname}-%{version}-src.tar.gz
Patch0:         GLee-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
Source44: import.info
Provides: GLee = %{version}-%{release}

%description
GLee (GL Easy Extension library) is a free cross-platform extension loading
library for OpenGL. It provides seamless support for OpenGL functions up
to version 3.0 and 399 extensions. 


%package devel
Group: Development/C
Summary:        Development headers for %{oldname}
Requires:       %{name} = %{version}-%{release}
Provides: GLee-devel = %{version}-%{release}

%description devel
Development headers for %{oldname}


%prep
%setup -q -c -n %{oldname}-%{version}
%patch0 -p1


sed -i "s|\r||g" *.h *.c *.txt
chmod -x *.h *.c *.txt
iconv -f=iso-8859-1 -t=utf-8 readme.txt > tmp && mv tmp readme.txt

sed -i -e '/${LDCONFIG}/d' Makefile.in
sed -i -e '/doc/d' Makefile.in

sed -i 's|-shared|-shared -Wl,-soname,lib%{oldname}.so.%{major} -fPIC|g' Makefile.in
sed -i 's|LIBNAME=.*|LIBNAME=lib%{oldname}.so.%{version}|g' Makefile.in


%build
%configure
%make_build


%install
install -dm755 %{buildroot}%{_includedir}/GL
install -dm755 %{buildroot}%{_libdir}
make install INCLUDEDIR=%{buildroot}%{_includedir} \
             LIBDIR=%{buildroot}%{_libdir}
ln -s lib%{oldname}.so.%{version} %{buildroot}%{_libdir}/lib%{oldname}.so





%files
%{_libdir}/lib%{oldname}.so.*
%doc readme.txt


%files devel
%{_libdir}/lib%{oldname}.so
%{_includedir}/GL/%{oldname}.h
%doc extensionList.txt


%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 5.4.0-alt1_31
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_3
- new version

