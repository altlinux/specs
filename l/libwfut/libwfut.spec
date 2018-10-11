# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libwfut
Version:        0.2.3
Release:        alt1_17
Summary:        Software updater tool for WorldForge applications

Group:          Development/Other
License:        LGPLv2+
URL:            http://www.worldforge.org/
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz

# libsigc++20-2.6.0 remove object_slot.h and it causes the build failure.
# Backport patch from upstream
Patch0:         libwfut-0.2.3-Remove-reference-to-object_slot-h.patch

BuildRequires:  gcc-c++
BuildRequires:  libsigc++2-devel libcurl-devel zlib-devel tinyxml-devel swig
Source44: import.info

%description
libwfut is the WorldForge Update Tool (WFUT) client side implementation in C++
for use directly by WorldForge clients.


%package devel
Summary: Development files for libwfut library
Group:   Development/Other
Requires: pkgconfig %{name} = %{version}-%{release}


%description devel
Development libraries and headers for linking against the libwfut library.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# remove wfut binary from package - will return it back when java wfut package will be obsoleted
rm -f $RPM_BUILD_ROOT%{_bindir}/wfut
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/wfut.1


%check
make check

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
#%{_bindir}/wfut
#%{_mandir}/man1/wfut.1*
%{_libdir}/libwfut-0.2.so.*


%files devel
%{_includedir}/%{name}-0.2
%{_libdir}/libwfut-0.2.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_9
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_5
- fixed build

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.2-alt1_1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1_1.1
- Rebuild with Python-2.7

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- initial release by fcimport

