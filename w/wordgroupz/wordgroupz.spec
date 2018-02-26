# python macros required
BuildRequires(pre): rpm-build-python
%define fedora 15
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Summary: A vocabulary building application
Name: wordgroupz
Version: 0.3.1
Release: alt1_5
Source0: http://rtnpro.fedorapeople.org/wordgroupz/wordgroupz-%{version}.tar.gz
License: GPLv3
Group: Text tools
URL: http://gitorious.org/wordgroupz/
BuildArch: noarch
BuildRequires: python-devel desktop-file-utils
Requires: pygtk2 pywebkitgtk python-module-nltk wordnet
Requires: python-module-BeautifulSoup python-module-gst
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
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5
- update to new release by fcimport

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1_4.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- initial release by fcimport

