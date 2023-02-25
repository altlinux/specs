# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ swig
# END SourceDeps(oneline)
Group: Development/Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:       Library for converting unicode strings to numbers
Name:          libuninum
Version:       2.7
Release:       alt3_33
# numconv is GPLv2, lib is LGPLv2
License:       GPLv2 and LGPLv2
URL:           http://billposer.org/Software/libuninum.html
Source0:       http://billposer.org/Software/Downloads/libuninum-%{version}.tar.bz2
Patch0:        libuninum-2.7-64bit-clean.patch
Patch1:        libuninum-configure-c99.patch
BuildRequires:  gcc
BuildRequires: libgmp-devel libgmpxx-devel
Source44: import.info
%description
libuninum is a library for converting Unicode strings to
numbers. Internal computation is done using arbitrary precision
arithmetic, so there is no limit on the size of the integer that can
be converted. The value is returned as an ASCII decimal string, a GNU
MP object, or an unsigned long integer.  Auto-detection of the number
system is provided. The number systems supported include Arabic,
Armenian, Balinese, Bengali, Burmese, Chinese, Cyrillic, Devanagari,
Egyptian, Ethiopic, Glagolitic, Greek, Gujarati, Gurmukhi, Hebrew,
Kannada, Khmer, Klingon, Lao, Limbu, Malayalam, Mongolian, New Tai
Lue, Nko, Old Italic, Old Persian, Odia, Osmanya, Perso-Arabic,
Phoenician, Roman Numerals, Tamil, Telugu, Tengwar, Thai, and Tibetan.

%package       devel
Group: Development/Other
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
%description   devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1 -b .64bit-clean
%patch1 -p1

%build
%configure --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
make install DESTDIR=%{buildroot}
install -p -D -m 0644 numconv.1 %{buildroot}/%{_mandir}/man1/numconv.1
rm -f %{buildroot}%{_bindir}/NumberConverter.tcl
rm -f %{buildroot}%{_libdir}/libuninum.la

%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog CREDITS NEWS README README_NUMBERCONVERTER TODO
%doc Examples
%{_bindir}/numconv
%{_libdir}/libuninum.so.*
%{_mandir}/man1/numconv.1*

%files devel
%doc --no-dereference COPYING
%{_includedir}/uninum
%{_libdir}/libuninum.so

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.7-alt3_33
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_20.1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_18.1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_17.1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_16.1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_15.1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_14.1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_13.1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_12.1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_11.1
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_10.1
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_10.1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_9.1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_9.1
- initial import by fcimport

