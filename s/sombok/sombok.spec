# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 21
Name:           sombok
Version:        2.3.1
Release:        alt1_2
Summary:        Unicode Text Segmentation Package

Group:          System/Libraries
License:        GPLv2+ or Artistic clarified
URL:            http://sf.net/projects/linefold/
Source0:        http://downloads.sourceforge.net/linefold/%{name}-%{version}.tar.gz

# libthai is available only in Fedora and EL6
%if 0%{?rhel} > 5 || 0%{?fedora}
BuildRequires:  libthai-devel
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info


%description
Sombok library package performs Line Breaking Algorithm described in Unicode
Standards Annex #14 (UAX #14). East_Asian_Width informative properties defined
by Annex #11 (UAX #11) may be concerned to determine breaking positions. This
package also implements "default" Grapheme Cluster segmentation described in
Annex #29 (UAX #29).


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}


%install
# hack
rm -rf doc/html/search
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog ChangeLog.REL1 COPYING NEWS README README.ja_JP
%{_libdir}/libsombok.so.*


%files devel
%{_includedir}/sombok*.h
%{_libdir}/libsombok.so
%{_libdir}/pkgconfig/sombok.pc


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3
- update to new release by fcimport

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- new release

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- fc import

