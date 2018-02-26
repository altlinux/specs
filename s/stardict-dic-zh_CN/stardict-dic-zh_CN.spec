Name: stardict-dic-zh_CN
Summary: Simplified Chinese(zh_CN) dictionaries for StarDict
Version: 2.4.2
Release: alt2_8
Group: Text tools
License: GPL+
URL: http://stardict.sourceforge.net

# Hi. Are you adding a dictionary here? Please be sure we have a clear license for it.
# The stardict page is _NOT_ a trusted source for licensing.
# Not sure? Don't include it, or email fedora-legal@redhat.com first.

# Cannot find licensing.
# Source0: http://downloads.sourceforge.net/stardict/stardict-cdict-gb-2.4.2.tar.bz2
# CEDICT license is non-free
# Source1: http://downloads.sourceforge.net/stardict/stardict-cedict-gb-2.4.2.tar.bz2
# Cannot find licensing
# Source2: http://downloads.sourceforge.net/stardict/stardict-langdao-ce-gb-2.4.2.tar.bz2
# Source3: http://downloads.sourceforge.net/stardict/stardict-langdao-ec-gb-2.4.2.tar.bz2
# Almost certainly not used with permission.
# Source4: http://downloads.sourceforge.net/stardict/stardict-oxford-gb-2.4.2.tar.bz2
# From upstream stardict, okay.
Source5: http://downloads.sourceforge.net/stardict/stardict-stardict1.3-2.4.2.tar.bz2
# From http://ftp.cdut.edu.cn/pub/linux/system/chinese/xdict/xdict.README
# GPL+
Source6: http://downloads.sourceforge.net/stardict/stardict-xdict-ce-gb-2.4.2.tar.bz2
Source7: http://downloads.sourceforge.net/stardict/stardict-xdict-ec-gb-2.4.2.tar.bz2

BuildArchitectures: noarch

Requires: stardict >= 2.4.2
Source44: import.info

%description
Simplified Chinese(zh_CN) dictionaries for StarDict.
These dictionaries are included currently:
stardict1.3, xdict-ce-gb, xdict-ec-gb.
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
%setup -q -n %{name}-%{version} -D -T -a 7

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
cp -rf stardict-* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/

%files
%{_datadir}/stardict/dic/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_7
- initial release by fcimport

