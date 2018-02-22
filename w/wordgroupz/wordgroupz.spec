# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Summary: A vocabulary building application
Name: wordgroupz
Version: 0.3.1
Release: alt1_14
Source0: http://rtnpro.fedorapeople.org/wordgroupz/wordgroupz-%{version}.tar.gz
License: GPLv3
Group: Games/Other
URL: http://gitorious.org/wordgroupz/
BuildArch: noarch
BuildRequires: python-devel, desktop-file-utils
Requires: python-module-pygtk python-module-pygtk-demo, python-module-pywebkitgtk, python-module-nltk libwordnet wordnet
Requires: python-module-BeautifulSoup, python-module-gst1.0
Source44: import.info

%description
wordGroupz is a vocabulary building application. You can store here
words in relevant groups so that you have an idea overall meaning of
the words. This is very useful for standard test preparations.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

%files
%{_bindir}/wordgroupz
%{_datadir}/wordgroupz/
%{_datadir}/pixmaps/wordgroupz.png
%{_datadir}/applications/wordgroupz*.desktop
%{python_sitelibdir_noarch}/*.egg-info

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_14
- rebuild with gstreamer

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_6
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5
- update to new release by fcimport

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1_4.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- initial release by fcimport

