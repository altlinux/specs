BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-plib
Version:        1.8.5
Release:        alt1_3
Summary:        Fedora mingw set of portable game related libraries
Group:          System/Libraries
License:        LGPLv2+
URL:            http://plib.sourceforge.net/
Source:         http://plib.sourceforge.net/dist/plib-%{version}.tar.gz

# native's package patches
Patch1:         plib-1.8.4-fullscreen.patch
Patch3:         plib-1.8.4-autorepeat.patch

#mingw specific patches:
Patch100:       plib-shared-lib.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 35
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw32-freeglut
BuildRequires:  mingw32-libpng

#autotools are run
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%% portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.

%{_mingw32_description}

%package static
Summary:        Static version of Fedora mingw set of portable game related libraries 
Requires:       %{name} = %{version}-%{release}
Group:          System/Libraries

%description static
Static version of Fedora mingw set of portable game related libraries


%prep
%setup -q -n plib-%{version}
%patch1 -p1 -b .fs
%patch3 -p1 -b .autorepeat
%patch100 -p0
# for some reason this file has its x permission sets, which makes rpmlint cry
chmod -x src/sg/sgdIsect.cxx

%build
libtoolize
./autogen.sh
%_mingw32_configure --enable-static --enable-shared
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/libplib*.la

%files
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_mingw32_libdir}/libplibul.dll.a
%{_mingw32_libdir}/libplibssgaux.dll.a
%{_mingw32_libdir}/libplibssg.dll.a
%{_mingw32_libdir}/libplibsm.dll.a
%{_mingw32_libdir}/libplibsl.dll.a
%{_mingw32_libdir}/libplibsg.dll.a
%{_mingw32_libdir}/libplibpw.dll.a
%{_mingw32_libdir}/libplibpuaux.dll.a
%{_mingw32_libdir}/libplibpu.dll.a
%{_mingw32_libdir}/libplibpsl.dll.a
%{_mingw32_libdir}/libplibnet.dll.a
%{_mingw32_libdir}/libplibjs.dll.a
%{_mingw32_libdir}/libplibfnt.dll.a
%{_mingw32_includedir}/plib
%{_mingw32_bindir}/libplibul-0.dll
%{_mingw32_bindir}/libplibssgaux-0.dll
%{_mingw32_bindir}/libplibssg-0.dll
%{_mingw32_bindir}/libplibsm-0.dll
%{_mingw32_bindir}/libplibsl-0.dll
%{_mingw32_bindir}/libplibsg-0.dll
%{_mingw32_bindir}/libplibpw-0.dll
%{_mingw32_bindir}/libplibpuaux-0.dll
%{_mingw32_bindir}/libplibpu-0.dll
%{_mingw32_bindir}/libplibpsl-0.dll
%{_mingw32_bindir}/libplibnet-0.dll
%{_mingw32_bindir}/libplibjs-0.dll
%{_mingw32_bindir}/libplibfnt-0.dll

%files static
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_mingw32_libdir}/libplibul.a
%{_mingw32_libdir}/libplibssgaux.a
%{_mingw32_libdir}/libplibssg.a
%{_mingw32_libdir}/libplibsm.a
%{_mingw32_libdir}/libplibsl.a
%{_mingw32_libdir}/libplibsg.a
%{_mingw32_libdir}/libplibpw.a
%{_mingw32_libdir}/libplibpuaux.a
%{_mingw32_libdir}/libplibpu.a
%{_mingw32_libdir}/libplibpsl.a
%{_mingw32_libdir}/libplibnet.a
%{_mingw32_libdir}/libplibjs.a
%{_mingw32_libdir}/libplibfnt.a

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.5-alt1_3
- initial release by fcimport

