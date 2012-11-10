BuildRequires: gcc-c++
%add_optflags %optflags_shared
%define oldname GLee
%define major 5
Name:           libGLee
Version:        %{major}.4.0
Release:        alt1_3
Summary:        GL Easy Extension library

Group:          Development/C
License:        BSD
URL:            http://elf-stone.com/glee.php
Source0:        http://www.elf-stone.com/downloads/GLee/GLee-5.4.0-src.tar.gz

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
%setup -q -c %{oldname}-%{version}

sed -i "s|\r||g" *.h *.c *.txt
chmod -x *.h *.c *.txt
iconv -f=iso-8859-1 -t=utf-8 readme.txt > tmp && mv tmp readme.txt

sed -i -e '/${LDCONFIG}/d' Makefile.in
sed -i -e '/doc/d' Makefile.in

sed -i 's|-shared|-shared -Wl,-soname,lib%{oldname}.so.%{major} -fPIC|g' Makefile.in
sed -i 's|LIBNAME=.*|LIBNAME=lib%{oldname}.so.%{version}|g' Makefile.in

%build
%configure
make %{?_smp_mflags}


%install
install -dm 755 $RPM_BUILD_ROOT{%{_includedir}/GL,%{_libdir}}
make install INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
             LIBDIR=$RPM_BUILD_ROOT%{_libdir}

pushd $RPM_BUILD_ROOT%{_libdir}
    /sbin/ldconfig -n .
    ln -s lib%{oldname}.so.%{version} lib%{oldname}.so
popd


%files
%doc readme.txt
%{_libdir}/lib%{oldname}.so.*

%files devel
%doc extensionList.txt
%{_libdir}/lib%{oldname}.so
%{_includedir}/GL/%{oldname}.h

%changelog
* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_3
- new version

