# BEGIN SourceDeps(oneline):
BuildRequires: libXext-devel libpulseaudio-devel pkgconfig(liblo) xorg-xproto-devel
# END SourceDeps(oneline)
Name:		bristol
Version:	0.60.11
Release:	alt2
Summary:	Synthesizer emulator
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:		Sound
License:	GPLv2+
URL:		http://bristol.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		bristol-0.60.9-CVE-2010-3351.patch
# fix build on non-x86 arches (remove compiler options from linker flags)
#Patch1:		bristol-0.60.9-secondary.patch

BuildRequires:	libX11-devel libalsa-devel libjack-devel desktop-file-utils
Source44: import.info

%description
Bristol is an emulation package for a number of different 'classic' 
synthesizers including additive and subtractive and a few organs. 
The application consists of the engine, which is called bristol, 
and its own GUI library called brighton that represents all the emulations.

%package devel
Summary:	%{summary}
Group:		Sound
Requires:	%{name} = %{version}

%description devel
This package contains the development libraries for Bristol.

%prep
%setup -q

%patch0 -p0 -b .libpath
#%patch1 -p1 -b .secondary

find ./bitmaps/ -name '*.gz' | xargs chmod -x 
chmod -x ./memory/profiles/*
find . -name '*.c' | xargs chmod -x
find . -name '*.h' | xargs chmod -x
find . -name '*.xbm' | xargs chmod -x
find . -name '*.svg' | xargs chmod -x
chmod -x NEWS COPYING* README AUTHORS ChangeLog
chmod -x memory/mixer/default/memory memory/mini/readme.txt

# Only x86_64 is optimised for SSE, non x86 platforms don't have SSE
%ifnarch x86_64
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.am 
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.in
%endif

%build
%configure --enable-static=no --disable-version-check
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm INSTALL
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 0644 bitmaps/bicon.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/bristol.svg
desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_bindir}/*
%{_datadir}/bristol
%{_datadir}/pixmaps/*
%{_datadir}/applications/bristol.desktop
%{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%{_libdir}/lib*.so

%changelog
* Sat Mar 07 2015 Ilya Mashkin <oddity@altlinux.ru> 0.60.11-alt2
- Build for Sisyphus

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_2
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.60.11-alt1_1
- initial fc import

