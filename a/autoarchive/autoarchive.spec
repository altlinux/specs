Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           autoarchive
Version:        1.3.0
Release:        alt1_3
Summary:        A simple backup tool that uses tar

License:        GPLv3
URL:            http://autoarchive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Fix tests. Cannot submit upstream as issue tracker is locked
Patch0:         autoarchive-1.3.0-fix_tests.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-module-mock

Requires:       gzip-utils less xz
Requires:       tar
Requires:       gzip gzip-utils less
Requires:       bzip2 gzip-utils less
Requires:       gzip-utils less xz
Source44: import.info

%description
AutoArchive is a simple utility for making backups more easily. It
uses tar for creating archives. The idea of the program is that every 
information needed for making a backup is in one file - the archive 
spec file. Path to this file is passed as a parameter to 'aa' command 
which reads information from it and creates desired backup.

%prep
%setup -q
%patch0 -p1

%build
# Need to set LANG to ensure we get utf-8 as default codec, or setup.py
# crashes
export LANG=en_US.UTF-8
%python3_build

%install
# Need to set LANG to ensure we get utf-8 as default codec, or setup.py
# crashes
export LANG=en_US.UTF-8 
%python3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{name}-%{version}/

%check
pushd AutoArchive
%{__python3} tests/run_tests.py
popd

%files
%doc NEWS README README.sk
%doc COPYING
%config(noreplace) %{_sysconfdir}/aa/
%{_mandir}/man?/*.*
%{_bindir}/autoarchive
%{_bindir}/aa
%{python3_sitelibdir_noarch}/AutoArchive/
%{python3_sitelibdir_noarch}/%{name}*.egg-info

%changelog
* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- fixed build

* Tue Jan 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1_6.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- update to new release by fcimport

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.1-alt1_1.1
- Rebuild with Python-3.3

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update to new release by fcimport

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_4
- new release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- rebuild to get rid of #27020

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1_3.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_3
- initial release by fcimport

