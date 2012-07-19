Group: Sound
Name:           cd-discid
Version:        1.3.1
Release:        alt1_1
Summary:        Utility to get CDDB discid information

# Also "Larry Wall's Artistic" upstream, but that's not accepted in Fedora
License:        GPLv2+
URL:            http://linukz.org/cd-discid.shtml
Source0:        http://linukz.org/download/%{name}-%{version}.tar.gz
# Sent upstream 2012-06-26
Patch0:         0001-Make-it-possible-to-prevent-stripping-e.g.-with-STRI.patch
Source44: import.info

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc.  It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.


%prep
%setup -q
%patch0 -p1


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} STRIP=:


%files
%doc changelog COPYING README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*


%changelog
* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- initial release by fcimport

