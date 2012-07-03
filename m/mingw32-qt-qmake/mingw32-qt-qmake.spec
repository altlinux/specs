BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

%global debug_package %{nil}

#global pre beta1

%global platform win32-g++-cross
%global compatplatform fedora-win32-cross

Name:           mingw32-qt-qmake
Version:        4.7.1
Release:        alt1_3
Summary:        Qt for Windows Build Environment

License:        GPLv3 with exceptions or LGPLv2 with exceptions
Group:          System/Libraries

URL:            http://www.qtsoftware.com/

# Special cross-compilation qmake target.
Source0:        qmake.conf
Source1:        qplatformdefs.h
Source2:        LGPL_EXCEPTION.txt
Source3:        LICENSE.GPL3
Source4:        LICENSE.LGPL


BuildRequires:  dos2unix
BuildRequires:  mingw32-filesystem >= 35

Requires:       qt4-devel
Source44: import.info

%description
This package contains the build environment for cross compiling
applications with the Fedora Windows Qt Library and cross-compiler.

%prep

%setup -n mingw32-qt-qmake -c -T
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build

%install

# Cross-compiler qmake specs.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/qt4/mkspecs/%{platform}
cp %{SOURCE0} %{SOURCE1} \
  $RPM_BUILD_ROOT%{_libdir}/qt4/mkspecs/%{platform}
%if 0%{?compatplatform:1}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/qt4/mkspecs/%{compatplatform}
cp %{SOURCE0} %{SOURCE1} \
  $RPM_BUILD_ROOT%{_libdir}/qt4/mkspecs/%{compatplatform}
%endif


%files
%doc LGPL_EXCEPTION.txt LICENSE.GPL3 LICENSE.LGPL
%{_libdir}/qt4/mkspecs/%{platform}
%if 0%{?compatplatform:1}
%{_libdir}/qt4/mkspecs/%{compatplatform}
%endif


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.1-alt1_3
- initial release by fcimport

