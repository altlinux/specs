# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python-devel python3-devel unzip
# END SourceDeps(oneline)
%define oldname pyke
%global with_python3 1

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:			python-module-pyke
Summary:		Knowledge-based inference engine
Version:		1.1.1
Release:		alt3
License:		MIT
Group:			System/Libraries
URL:			http://pyke.sourceforge.net/
Source0:		http://download.sourceforge.net/%{oldname}/%{oldname}-%{version}.zip
%if 0%{?with_python3}
Source1:		http://download.sourceforge.net/%{oldname}/%{oldname}3-%{version}.zip
%endif # if with_python3
BuildArch:		noarch
BuildRequires: python-base python-dev, python-module-setuptools
Requires:		python-module-ply

%if 0%{?with_python3}
BuildRequires:          python3-dev
%endif # if with_python3
Source44: import.info

%description
Pyke is a knowledge-based inference engine (expert system) written in 100% 
python that can:
* Do both forward-chaining (data driven) and backward-chaining (goal 
  directed) inferencing.
* Automatically generate python programs by assembling individual python 
  functions into complete call graphs.

%if 0%{?with_python3}
%package -n python3-module-pyke
Summary:		Knowledge-based inference engine
Group:			System/Libraries
Requires:		python3-module-ply

%description -n python3-module-pyke
Pyke is a knowledge-based inference engine (expert system) written in 100%
python that can:
* Do both forward-chaining (data driven) and backward-chaining (goal
  directed) inferencing.
* Automatically generate python programs by assembling individual python
  functions into complete call graphs.
%endif # with_python3

%package examples
Summary:		Examples from pyke source code
Group:			Documentation
# Overkill, but it is hypothetically possible that the main package could go arch-specific.
BuildArch:		noarch

%description examples
Pyke example code files from the upstream source.

%prep
%if 0%{?with_python3}
%setup -n %{oldname}-%{version} -q -a 1
mv %{oldname}-%{version} %{oldname}3-%{version}
%else
%setup -n %{oldname}-%{version} -q
%endif # with_python3


%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{oldname}3-%{version}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{oldname}3-%{version}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

rm -rf doc/testdocs*
# This is stupid. Delete this.
rm -rf $RPM_BUILD_ROOT/usr/pyke
rm -rf doc/source/

%files
%doc LICENSE
%doc README.txt RELEASE_NOTES-* doc/html/
%{python_sitelibdir_noarch}/%{oldname}/
%{python_sitelibdir_noarch}/%{oldname}-%{version}*.egg-info

%if 0%{?with_python3}
%files -n python3-module-pyke
%doc LICENSE
%doc README.txt RELEASE_NOTES-* doc/html/
%{python3_sitelibdir_noarch}/%{oldname}/
%{python3_sitelibdir_noarch}/%{oldname}-%{version}*.egg-info
%endif # with_python3

%files examples
%doc examples/

%changelog
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

