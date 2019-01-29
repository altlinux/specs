Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python-module-setuptools python3-module-setuptools
# END SourceDeps(oneline)
%define oldname pyaudio
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname pyaudio
%global sum Python bindings for PortAudio

Name:		python-module-pyaudio
Version:	0.2.11
Release:	alt1_1
License:	MIT
Url:		http://people.csail.mit.edu/hubert/pyaudio/
Source0:	https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz
Summary:	%{sum}

BuildRequires:  gcc
BuildRequires:	libportaudio2-devel
BuildRequires:	python-devel
BuildRequires:	python3-devel
Source44: import.info

%description
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O
library. With PyAudio, you can easily use Python to play and record audio on
a variety of platforms.

%package -n python3-module-pyaudio
Group: System/Libraries

Summary:	%{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-module-pyaudio
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O
library. With PyAudio, you can easily use Python to play and record audio on
a variety of platforms.

%prep
%setup -q -n PyAudio-%{version}

# remove some pre-built binaries
rm -rf packaging

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files -n python-module-pyaudio
%doc README CHANGELOG
%{python_sitelibdir}/*.py*
%{python_sitelibdir}/*.so
%{python_sitelibdir}/*egg-info

%files -n python3-module-pyaudio
%doc README CHANGELOG
%{python3_sitelibdir}/*.py*
%{python3_sitelibdir}/__pycache__/*.py*
%{python3_sitelibdir}/*.so
%{python3_sitelibdir}/*egg-info

%changelog
* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1_1
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt3_10
- update to new release by fcimport

* Mon Apr 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.9-alt3_8
- (NMU) Rebuilt with python-3.6.4.

* Wed Apr 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt2_8
- to Sisyphus as anki dep

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt1_8
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt1_7
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_12
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_11
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_10
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_9
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_8
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_7
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_6
- initial fc import

