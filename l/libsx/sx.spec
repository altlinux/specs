# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname sx
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Tool to extract reports and run plug-ins against those extracted reports
Name: libsx
Version: 2.17
Release: alt1_4
URL: http://fedorahosted.org/sx
Source0: https://git.fedorahosted.org/cgit/sx.git/snapshot/%{oldname}-%{version}.tar.gz
License: GPLv2
Group: System/Libraries
BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
Requires: python
Source44: import.info
Provides: sx = %{version}-%{release}

%description
sxconsole is a tool used to extract various report types and then
analyze those extracted reports with plug-ins. The tool also provides
an archiving structure so that all the compressed and extracted
reports are saved to a directory. This tool was developed for
sysreport/sosreports but has been expanded to include any report that
has a class defined.

%prep
%setup -n %{oldname}-%{version} -q

%build
%{__python} setup.py build

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__python} setup.py install --optimize 1 --root=${RPM_BUILD_ROOT}

%files
%doc LICENSE AUTHORS PKG-INFO CHANGELOG
%doc doc/*
%{_bindir}/sxconsole
%{python_sitelibdir_noarch}/*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_1
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1_2
- update to new release by fcimport

* Mon Jun 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1_1
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1_1
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_1
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_1
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.05-alt3_20
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.05-alt2_20
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.05-alt2_19
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1_19
- initial import by fcimport

