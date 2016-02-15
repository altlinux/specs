# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(Archive/Tar.pm) perl(Archive/Zip.pm)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname alfont
Name:           libalfont
Version:        2.0.9
Release:        alt1_9
Summary:        Font rendering library for the Allegro game library
Group:          System/Libraries
License:        FTL
URL:            http://chernsha.sitesled.com/
# this is http://chernsha.sitesled.com/AlFont209.rar repackaged in .tgz format
Source0:        %{oldname}-%{version}.tar.gz
Patch0:         alfont-2.0.9-linux.patch
Patch1:         alfont-2.0.9-remove-alfont_get_string.patch
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
Requires:       %{name} = %{version}
Provides: alfont-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -z .linux
%patch1 -p1
for i in include/alfont*.h freetype/docs/FTL.TXT; do
    sed -i.orig s'/\r//g' $i
    touch -r $i.orig $i
done


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
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_4
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_3
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt2_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_9
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_8
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_7
- initial release by fcimport

