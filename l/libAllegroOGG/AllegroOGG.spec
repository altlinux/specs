# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname AllegroOGG
Name:           libAllegroOGG
Version:        1.0.3
Release:        alt2_9
Summary:        Ogg library for use with the Allegro game library
Group:          System/Libraries
License:        BSD
URL:            http://www.allegro.cc/resource/Libraries/Audio/alogg
Source0:        http://www.hero6.com/filereviver/alogg.zip
Source1:        AllegroOGG.pc.in
BuildRequires:  liballegro-devel libvorbis-devel
Source44: import.info
Provides: AllegroOGG = %{version}-%{release}

%description
%{oldname} is an Allegro wrapper for the Ogg Vorbis decoder from the Xiph.org
foundation. This lib lets you play OGGs and convert OGGs to Allegro SAMPLEs
amongst a lot of other capabilites.


%package devel
Summary:        Developmental libraries and include files for AllegroOgg
Group:          Development/C
Requires:       libAllegroOGG = %{version}-%{release}
Provides: AllegroOGG-devel = %{version}-%{release}

%description devel
Development libraries and include files for developing applications using
the %{oldname} library.


%prep
%setup -q -c
%{__sed} -i 's/\r//' docs/A*.txt
%{__sed} -e "s#@prefix@#%{_prefix}#g" -e "s#@libdir@#%{_libdir}#g" \
  -e "s#@includedir@#%{_includedir}#g" -e "s#@version@#%{version}#g" \
  -e "s#@name@#%{oldname}#" %{SOURCE1} > %{oldname}.pc

%build
# makefile doesn't support creating an .so, and wants to use its own version
# of libogg and libvorbis and there is only one source file so lets DIY
gcc $RPM_OPT_FLAGS -fPIC -DPIC -Iinclude -c src/alogg.c -o src/alogg.o
gcc -g -shared -Wl,-soname=lib%{oldname}.so.0 -o lib%{oldname}.so.0 \
  src/alogg.o -logg -lvorbis -lvorbisfile $(allegro-config --libs)


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -m 755 lib%{oldname}.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{oldname}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}.so
install -m 644 %{oldname}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig

mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{oldname}
install -m 644 include/* $RPM_BUILD_ROOT%{_includedir}/%{oldname}


%files
%doc docs/*.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{oldname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oldname}.pc


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_9
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8
- initial release by fcimport

