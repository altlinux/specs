Group: Text tools
Name: stardict-dic-zh_TW
Summary: Traditional Chinese(zh_TW) dictionaries for StarDict
Version: 2.4.2
Release: alt2_17
License: GPL+
URL: http://stardict.sourceforge.net

# Hi. Are you adding a dictionary here?	Please be sure we have a clear license for it.
# The stardict page is _NOT_ a trusted source for licensing.
# Not sure? Don't include it, or email fedora-legal@redhat.com first.

# Cannot find licensing.
# Source0: http://downloads.sourceforge.net/stardict/stardict-cdict-big5-2.4.2.tar.bz2
# CEDICT license is non-free.
# Source1: http://downloads.sourceforge.net/stardict/stardict-cedict-big5-2.4.2.tar.bz2
# Cannot find licensing
# Source2: http://downloads.sourceforge.net/stardict/stardict-langdao-ce-big5-2.4.2.tar.bz2
# Source3: http://downloads.sourceforge.net/stardict/stardict-langdao-ec-big5-2.4.2.tar.bz2
# Almost certainly not used with permission.
# Source4: http://downloads.sourceforge.net/stardict/stardict-oxford-big5-2.4.2.tar.bz2
# From http://ftp.cdut.edu.cn/pub/linux/system/chinese/xdict/xdict.README
# GPL+
Source5: http://prdownloads.sourceforge.net/stardict/stardict-xdict-ec-big5-2.4.2.tar.bz2
Source6: http://prdownloads.sourceforge.net/stardict/stardict-xdict-ce-big5-2.4.2.tar.bz2

BuildArch: noarch
Requires: stardict stardict-plugin-espeak stardict-plugin-spell
Source44: import.info

%description
Traditional Chinese(zh_TW) dictionaries for StarDict.

These dictionaries are included currently:
xdict-ce-big5, xdict-ec-big5.

You can download more at: http://stardict.sourceforge.net

%prep
%setup -c -T -n %{name}-%{version}
# %%setup -q -n %{name}-%{version} -D -T -a 0
# %%setup -q -n %{name}-%{version} -D -T -a 1
# %%setup -q -n %{name}-%{version} -D -T -a 2
# %%setup -q -n %{name}-%{version} -D -T -a 3
# %%setup -q -n %{name}-%{version} -D -T -a 4
%setup -q -n %{name}-%{version} -D -T -a 5
%setup -q -n %{name}-%{version} -D -T -a 6

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
cp -rf stardict-* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/

%files
%{_datadir}/stardict/dic/*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_15
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_13
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_10
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_9
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_9
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_8
- initial release by fcimport

