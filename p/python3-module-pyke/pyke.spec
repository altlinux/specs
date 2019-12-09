%define oname pyke

Name:       python3-module-pyke
Version:    1.1.1
Release:    alt4

Summary:    Knowledge-based inference engine
License:    MIT
Group:      System/Libraries
URL:        http://pyke.sourceforge.net/
BuildArch:  noarch

Source0:    http://download.sourceforge.net/%{oname}/%{oname}3-%{version}.zip
Source44:   import.info

BuildRequires(pre): rpm-build-python3
BuildRequires: unzip

%py3_requires ply


%description
Pyke is a knowledge-based inference engine (expert system) written in 100%% 
python that can:
* Do both forward-chaining (data driven) and backward-chaining (goal 
  directed) inferencing.
* Automatically generate python programs by assembling individual python 
  functions into complete call graphs.

%package examples
Summary: Examples from pyke source code
Group: Documentation
# Overkill, but it is hypothetically possible that the main package could go arch-specific.
BuildArch: noarch

%description examples
Pyke example code files from the upstream source.

%prep
%setup -n %oname-%version -q

%build
%__python3 setup.py build

%install
%__python3 setup.py install --skip-build --root $RPM_BUILD_ROOT

rm -rf doc/testdocs*
# This is stupid. Delete this.
rm -rf $RPM_BUILD_ROOT/usr/pyke
rm -rf doc/source/

%files
%doc LICENSE
%doc README.txt RELEASE_NOTES-* doc/html/
%python3_sitelibdir_noarch/%oname/
%python3_sitelibdir_noarch/*.egg-info

%files examples
%doc examples/


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt4
- python2 disabled

* Wed Dec 14 2016 Denis Medvedev <nbr@altlinux.org> 1.1.1-alt3
- move to sisyphus

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_18
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_17
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_14
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_11
- update to new release by fcimport

* Mon Apr 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1.1.1-alt2_10
- rebuild to get rid of unmets

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_10
- update to new release by fcimport

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_9
- initial fc import

