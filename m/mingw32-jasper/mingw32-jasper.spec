BuildRequires: rpm-build-mingw32
# one of the sources is a zip file
BuildRequires: unzip
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-jasper
Version:        1.900.1
Release:        alt1_13
Summary:        MinGW Windows Jasper library

License:        JasPer
Group:          System/Libraries

URL:            http://www.ece.uvic.ca/~mdadams/jasper/
Source0:        http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-%{version}.zip

# Patches from Fedora native package.
# OpenGL is disabled in this build, so we don't need this patch:
#Patch1:         jasper-1.701.0-GL.patch
# Note patch2 appears in native package, but is not applied:
#Patch2:         jasper-1.701.0-GL-ac.patch
Patch3:         patch-libjasper-stepsizes-overflow.diff

# MinGW-specific patches.
# This patch adds '-no-undefined' flag to libtool line:
Patch1000:      jasper-1.900.1-mingw32.patch
# This patch is a bit of a hack, but it's just there to fix a demo program:
Patch1001:      jasper-1.900.1-sleep.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-dlfcn
Source44: import.info


%description
MinGW Windows Jasper library.


%package static
Summary:        Static version of the MinGW Windows Jasper library
Requires:       %{name} = %{version}-%{release}
Group:          System/Libraries

%description static
Static version of the MinGW Windows Jasper library.




%prep
%setup -q -n jasper-%{version}
%patch3 -p1 -b .CVE-2007-2721

%patch1000 -p1 -b .mingw32
%patch1001 -p1 -b .sleep


%build
%{_mingw32_configure} \
  --disable-opengl --enable-libjpeg --enable-static --enable-shared
make %{?_smp_mflags}


%install

make DESTDIR=$RPM_BUILD_ROOT install mandir=%{_mingw32_mandir}

# Remove the manual pages - don't duplicate documentation which
# is in the native Fedora package.
rm $RPM_BUILD_ROOT%{_mingw32_mandir}/man1/*


%files
%doc COPYRIGHT LICENSE NEWS README
%{_mingw32_bindir}/i586-pc-mingw32-imgcmp.exe
%{_mingw32_bindir}/i586-pc-mingw32-imginfo.exe
%{_mingw32_bindir}/i586-pc-mingw32-jasper.exe
%{_mingw32_bindir}/i586-pc-mingw32-tmrdemo.exe
%{_mingw32_bindir}/libjasper-1.dll
%{_mingw32_libdir}/libjasper.dll.a
%{_mingw32_libdir}/libjasper.la
%{_mingw32_includedir}/jasper/

%files static
%{_mingw32_libdir}/libjasper.a


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.900.1-alt1_13
- initial release by fcimport

