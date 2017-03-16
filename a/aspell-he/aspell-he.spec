# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lang he
%define langrelease 0
Summary: Hebrew dictionary for Aspell
Name: aspell-%{lang}
Version: 1.0
Release: alt2_16
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}

%description
Provides the word list/dictionaries for Hebrew.

# Note that this package, like other aspell's language packs, does not come up
# cleanly through rpmlint, but with the following errors:
# E: aspell-he no-binary
# E: aspell-he only-non-binary-in-usr-lib
# This is because the package contains only data files which sit under /usr/lib.
# They have to stay there, as they are architecture-dependent (due to
# byte-ordering issues).

%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure
%make_build

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_16
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- update and rebuild with proper aspell datadir

* Tue Jul 29 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3
- build for Sisyphus

