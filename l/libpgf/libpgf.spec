# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libpgf
Version:        6.14.12
Release:        alt1_5
Summary:        PGF (Progressive Graphics File) library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.libpgf.org
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
# Modernize automake usage
Patch0:         libpgf-auto.patch

## backport upstream fixes
Patch147: libpgf-r147.patch
Patch148: libpgf-r148.patch

BuildRequires:  doxygen
BuildRequires:  libtool
Source44: import.info

%description
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .auto
%patch147 -p1 -b .r147
%patch148 -p1 -b .r148
# Fix line endings
sed -i -e 's/\r//' configure.ac README

sed -i 's|$(DESTDIR)$(datadir)/doc/$(DOC_MODULE)|$(RPM_BUILD_DIR)/libpgf|g' doc/Makefile.am

sh autogen.sh


%build
# FIXME/TODO: document need for -DLIBPGF_DISABLE_OPENMP
# commit 52c998909401f404f1c7029b537ec900f3f780d0 doesn't say why, but
# I *think* it's related to digikam -- rex
export CFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP"
export CXXFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP"

%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# unpackaged files
rm -fv %{buildroot}%{_libdir}/libpgf.la


%files
%doc COPYING README
%{_libdir}/libpgf.so.6*

%files devel
%doc html
%{_includedir}/libpgf/
%{_libdir}/libpgf.so
%{_libdir}/pkgconfig/libpgf.pc
%{_mandir}/man3/*.3*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 6.14.12-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 6.14.12-alt1_4
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 6.14.12-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 6.13.45-alt1_0.3.svn123
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 6.13.45-alt1_0.2.svn123
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 6.13.45-alt1_0.1.svn123
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 6.12.24-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 6.12.24-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 6.12.24-alt1_3
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 6.12.24-alt1_2
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt1_1
- initial import by fcimport

