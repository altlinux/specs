# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name stbi
%global soname  lib%{name}
%global srcname stb_image

%define major	1
%define libname	lib%{name}%{major}
%define devname	lib%{name}-devel

Name:           stbi
Version:        1.33
Release:        alt1_7
Summary:        JPEG/PNG reader
License:        Public Domain
URL:            http://nothings.org/%{srcname}.c
Source0:        %{url}
Group:          Development/C
BuildRequires:  dos2unix
Source44: import.info

%description
Public Domain JPEG/PNG reader. Primarily of interest to game developers and
other people who can avoid problematic images and only need the trivial
interface.

%package -n %{libname}
Summary: JPEG/PNG reader
Group: System/Libraries
Obsoletes: %{name} < 1.33-2

%description -n %{libname}
Public Domain JPEG/PNG reader. Primarily of interest to game developers and
other people who can avoid problematic images and only need the trivial
interface.

%package -n %{devname}
Group: Development/C
Summary: JPEG/PNG reader development files
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{name}-devel < 1.33-2

%description -n %{devname}
Development files for %{name}.

%prep
%setup -Tc
head -62 %{SOURCE0} > README
head -184 %{SOURCE0} | tail -112 >> README
 
head -65 %{SOURCE0} | tail -2 > %{srcname}.h
head -332 %{SOURCE0} | tail -146 >> %{srcname}.h

echo '#include "stb_image.h"' > %{srcname}.c
head -4586 %{SOURCE0} | tail -4254 >> %{srcname}.c

tail -86 %{SOURCE0} > CHANGES

dos2unix *

%build
gcc %{optflags} -I. -fPIC -c %{srcname}.c
gcc %{optflags} -I. -shared -Wl,-soname,%{soname}.so.1 %{srcname}.o -o %{soname}.so.1.0.0 -lm


%install
install -Dpm0755 %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1.0.0
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so
install -Dpm0644 %{srcname}.h %{buildroot}%{_includedir}/%{srcname}.h


%files -n %{libname}
%doc README CHANGES
%{_libdir}/%{soname}.so.%{major}
%{_libdir}/%{soname}.so.%{major}.*

%files -n %{devname}
%{_libdir}/%{soname}.so
%{_includedir}/*


%changelog
* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 1.33-alt1_7
- new version

