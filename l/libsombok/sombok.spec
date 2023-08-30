# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname sombok
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libsombok
Version:        2.4.0
Release:        alt4_21
Summary:        Unicode Text Segmentation Package
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR Artistic-1.0-Perl)
URL:            http://sf.net/projects/linefold/
Source0:        https://github.com/hatukanezumi/sombok/archive/%{oldname}-%{version}.tar.gz
# A multilib-safe wrapper, bug #1853260
Source1:        sombok.h

BuildRequires:  libthai-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info
Provides: sombok = %{version}-%{release}


%description
Sombok library package performs Line Breaking Algorithm described in Unicode
Standards Annex #14 (UAX #14). East_Asian_Width informative properties defined
by Annex #11 (UAX #11) may be concerned to determine breaking positions. This
package also implements "default" Grapheme Cluster segmentation described in
Annex #29 (UAX #29).


%package        devel
Group: Development/Other
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Provides: sombok-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{oldname}-%{version}


%build
autoreconf -vif
%configure --disable-static
%make_build


%install
# hack
rm -rf doc/html/search
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Rename sombok.h to sombok-ARCH.h and install a sombok.h wrapper to avoid
# a file conflict on multilib systems, bug #1853260
mv %{buildroot}/%{_includedir}/sombok.h %{buildroot}/%{_includedir}/sombok-%{_arch}.h
install -m 0644 %{SOURCE1} %{buildroot}/%{_includedir}/sombok.h

# not all sombok-arch.h are included in wrapper
%ifarch %ix86
ln -s sombok-%{_arch}.h %buildroot%_includedir/sombok-i386.h ||:
%endif
%ifarch armh
ln -s sombok-armh.h %buildroot%_includedir/sombok-arm.h
%endif
%ifarch %{e2k}
mv -f %buildroot%_includedir/{sombok-%{_arch},sombok}.h
%endif





%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog ChangeLog.REL1 NEWS README README.ja_JP
%{_libdir}/libsombok.so.*


%files devel
%{_includedir}/sombok*.h
%{_libdir}/libsombok.so
%{_libdir}/pkgconfig/sombok.pc


%changelog
* Wed Aug 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.4.0-alt4_21
- sombok.h: support LoongArch architecture (lp64d ABI)

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt4_20
- update to new release by fcimport

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt4_14
- e2k support

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt3_14
- fix for i586

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt2_14
- fix for armh

* Wed Apr 28 2021 Slava Aseev <ptrnine@altlinux.org> 2.4.0-alt2_13
- fix include name on i[3-9]86 architectures

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_13
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_3
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_2
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_1
- moved to Sisyphus for perl-Text-vCard

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

