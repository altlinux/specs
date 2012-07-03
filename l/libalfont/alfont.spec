%add_optflags %optflags_shared
%define oldname alfont
Name:           libalfont
Version:        2.0.6
Release:        alt2_9
Summary:        Font rendering library for the Allegro game library
Group:          System/Libraries
License:        FTL
URL:            http://chernsha.sitesled.com/
# this is http://chernsha.sitesled.com/AlFont206.rar repackaged in .tgz format
Source0:        %{oldname}-%{version}.tar.gz
Patch0:         alfont-2.0.6-linux.patch
BuildRequires:  liballegro-devel libfreetype-devel
Source44: import.info
Provides: alfont = %{version}-%{release}

%description
alfont also known as AllegroFont or AlFont is a wrapper around the freetype2
library for use with the Allegro game library. Thus allowing the display of
text using freetype fonts on Allegro bitmaps.


%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       libalfont = %{version}-%{release}
Provides: alfont-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1 -z .linux
sed -i s'/\r//g' freetype/docs/FTL.TXT


%build
# Upstreams makefile uses its own private copy of freetype, since all
# we want is the wrapper and since the wrapper is only one file we
# do a manual compile here
gcc -fPIC -DPIC $RPM_OPT_FLAGS -Iinclude `freetype-config --cflags` \
  -o src/alfont.o -c src/alfont.c
gcc -shared -Wl,-soname,lib%{oldname}.so.2 -o lib%{oldname}.so.%{version} \
  src/alfont.o $(freetype-config --libs) $(allegro-config --libs)


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 lib%{oldname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{oldname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}.so.2
ln -s lib%{oldname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}.so
install -m 644 include/%{oldname}*.h $RPM_BUILD_ROOT%{_includedir}


%files
%doc CHANGES.txt README.txt freetype/docs/FTL.TXT
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}*.h
%{_libdir}/lib%{oldname}.so


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt2_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_9
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_8
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_7
- initial release by fcimport

