Name:           cd-discid
Version:        1.1
Release:        alt2_3
Summary:        Utility to get CDDB discid information

Group:          Sound
# Also "Larry Wall's Artistic" upstream, but that's not accepted in Fedora
License:        GPLv2+
URL:            http://linukz.org/cd-discid.shtml
Source0:        http://linukz.org/download/%{name}-%{version}.tar.gz
Source44: import.info

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc.  It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.


%prep
%setup -q


%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc changelog COPYING README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- initial release by fcimport

