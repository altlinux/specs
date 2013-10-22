BuildRequires: python-modules-encodings python-modules-xml
Name:           malaga-suomi-voikko
Version:        1.14
Release:        alt1_1
Summary:        A description of Finnish morphology written in Malaga (Voikko edition)

Group:          Text tools
License:        GPLv2+
URL:            http://voikko.sourceforge.net/
# The usual format of stable release source URLs
Source0:        http://downloads.sourceforge.net/voikko/suomi-malaga-%{version}.tar.gz
# The usual format of testing release source URLs
#Source0:        http://www.puimula.org/htp/testing/suomi-malaga-%{version}rc3.tar.gz

BuildRequires:  malaga >= 7.8

# debuginfo would be empty
%define debug_package %{nil}
Source44: import.info

%description
A description of Finnish morphology written in Malaga. This package is built
to support the Voikko spellchecker/hyphenator, it doesn't support the Sukija
text indexer.

%prep
%setup -q -n suomi-malaga-%{version}


%build
# configure removed, not needed in this package
make %{?_smp_mflags} voikko


%install
# Files differ on big-endian and small-endian archs, and they have different
# names (*_l vs *_b). This is the reason we use %%{_libdir} instead of
# %%{_datadir} and won't noarch the package.
make voikko-install DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko


%files
%doc ChangeLog CONTRIBUTORS COPYING README README.fi
%{_libdir}/voikko


%changelog
* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_3
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_2
- new version

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- initial import by fcimport

