# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:       Library for converting unicode strings to numbers
Name:          libuninum
Version:       2.7
Release:       alt3_10.1
# numconv is GPLv2, lib is LGPLv2
License:       GPLv2 and LGPLv2
Group:         Development/C
URL:           http://billposer.org/Software/libuninum.html
Source0:       http://billposer.org/Software/Downloads/%{name}-%{version}.tar.bz2
Patch0:        libuninum-2.7-64bit-clean.patch
BuildRequires: libgmp-devel libgmp_cxx-devel
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
Lue, Nko, Old Italic, Old Persian, Oriya, Osmanya, Perso-Arabic,
Phoenician, Roman Numerals, Tamil, Telugu, Tengwar, Thai, and Tibetan.

%package devel
Summary:  Header files, libraries and development documentation for %{name}
Group:    Development/C
Requires: libuninum = %{version}-%{release}

%description devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1 -b .64bit-clean

%build
%configure --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
%{__install} -p -D -m 0644 numconv.1 %{buildroot}/%{_mandir}/man1/numconv.1
%{__rm} -f %{buildroot}%{_bindir}/NumberConverter.tcl

%files
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README README_NUMBERCONVERTER TODO 
%doc Examples
%{_bindir}/numconv
%{_libdir}/libuninum.so.*
%{_mandir}/man1/numconv.1*

%files devel
%{_includedir}/uninum
%{_libdir}/libuninum.so

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt3_10.1
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_10.1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_9.1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_9.1
- initial import by fcimport

