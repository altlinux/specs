Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libst2205
Version:        1.4.3
Release:        alt3_25
Summary:        Library for accessing the display of hacked st2205 photo frames
License:        GPLv3+
URL:            http://picframe.spritesserver.nl/wiki/index.php
# Note the st2205tool includes tools to actually hack the pictureframe, this is
# something which should only be done by experienced techies and which we
# should not package. We do want to package the lib (which also is the only
# thing make install installs), hence the packagename is libst2205.
Source0:        http://www.neophob.com/files/st2205tool-1.4.3.tar.gz
Patch0:         st2205tool-1.4.3-no-exit.patch
Patch1:         st2205tool-1.4.3-width-height-swap.patch
Patch2:         libst2205-c99.patch
BuildRequires:  gcc
BuildRequires:  libgd3-devel
Source44: import.info

%description
It is possible to flash digital photo frames with the st2205 chip-sets with
a modified firmware, which allows one to display real time images on the
display of the frame from a PC. This package contains a library for accessing
the display from the PC, for st2205 frames with the hacked firmware.


%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Group: Development/Other
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
This package contains the st2205 set picture utility which can be used to
display a (properly sized) PNG file on a supported picture frames display.


%prep
%setup -q -n st2205tool
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
# -D_GNU_SOURCE to define the O_DIRECT macro.
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC -D_GNU_SOURCE" -C libst2205
%make_build CFLAGS="$RPM_OPT_FLAGS -I../libst2205" -C setpic


%install
# make install does not support DESTDIR nor PREFIX, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 setpic/setpic $RPM_BUILD_ROOT%{_bindir}/st2205-setpic
install -m 755 libst2205/libst2205.so $RPM_BUILD_ROOT%{_libdir}/libst2205.so.1
ln -s libst2205.so.1 $RPM_BUILD_ROOT%{_libdir}/libst2205.so
install -p -m 644 libst2205/st2205.h $RPM_BUILD_ROOT%{_includedir}






%files
%doc LICENSE
%{_libdir}/%{name}.so.1

%files devel
%doc %{name}/readme.txt
%{_includedir}/st2205.h
%{_libdir}/%{name}.so

%files tools
%{_bindir}/st2205-setpic


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt3_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_7
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_4
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_3
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_2
- initial import by fcimport

