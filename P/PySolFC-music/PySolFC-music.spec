%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define debug_package %{nil}

%define mainversion 1.1

Name:           PySolFC-music
Version:        4.40
Release:        alt2_14
Summary:        Music for PySolFC

Group:          Games/Other
License:        GPLv2+
URL:            http://www.pysol.org/
Source0:        ftp://ibiblio.org/pub/linux/games/solitaires/pysol-music-%{version}.tar.gz

Requires:       python-module-PySolFC >= %{mainversion}
Requires:       python-module-pygame

BuildArch: noarch
Source44: import.info

%description
This package contains the background music for %{name}


%prep
%setup -q -n pysol-music-%{version}

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC/music
cp -a data/music/* $RPM_BUILD_ROOT%{_datadir}/PySolFC/music

%files
%doc README NEWS COPYING
%dir %{_datadir}/PySolFC/music
%{_datadir}/PySolFC/music/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.40-alt1_8
- update to new release by fcimport

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 4.40-alt1_7
- initial release by fcimport

