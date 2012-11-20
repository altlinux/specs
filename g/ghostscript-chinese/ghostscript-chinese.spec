# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/python-config /usr/bin/runtest binutils-devel cmake elfutils-devel gcc-c++ libICE-devel libSM-devel libX11-devel libelf-devel perl(IPC/Open2.pm) python-devel
# END SourceDeps(oneline)
%global common_desc \
ghostscript font configuration files for Chinese fonts.


%global gsdir            %{_datadir}/ghostscript/conf.d
%global umingver         0.2.20080216.1
%global ukaiver          0.2.20080216.1
%global zenheiver        0.9.45

Name:           ghostscript-chinese
Version:        0.4.0
Release:        alt1_1
Summary:        Ghostscript Chinese fonts configuration files
Group:          System/Fonts/True type
License:        GPLv2+
URL:            http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:        http://pwu.fedorapeople.org/ghostscript-chinese/%{name}-%{version}.tar.gz
BuildArch:      noarch

#BuildRequires:
Provides:     cjkuni-fonts-ghostscript = %{version}
Obsoletes:    cjkuni-fonts-ghostscript < 0.2.20080216.1-45
Source44: import.info
%description
%common_desc


%package zh_CN
Summary:      Ghostscript Simplified Chinese fonts configuration files
Group:        System/Fonts/True type
Requires:     ghostscript-utils ghostscript
Requires:     fonts-ttf-wqy-zenhei >= %{zenheiver}
Requires:     %{name} = %{version}-%{release}

%description zh_CN
%common_desc

For Simplified Chinese.

%package zh_TW
Summary:      Ghostscript Traditional Chinese fonts configuration files
Group:        System/Fonts/True type
Requires:     ghostscript-utils ghostscript
Requires:     fonts-ttf-cjkuni-uming = %{umingver}
Requires:     fonts-ttf-cjkuni-ukai = %{ukaiver}
Requires:     %{name} = %{version}-%{release}

%description zh_TW
%common_desc

For Traditional Chinese.

%prep
%setup -q -c -n %{name}-%{version}


%build
%{nil}


%install
install -m 0755 -d %{buildroot}%{gsdir}

for gscid in `ls *.zh_CN *.zh_TW`
do
    install -m 0644 -p $gscid %{buildroot}%{gsdir}
done


%files
%doc COPYING
%doc README

%files zh_CN
%{gsdir}/FAPIcidfmap.zh_CN
%{gsdir}/cidfmap.zh_CN
%{gsdir}/CIDFnmap.zh_CN

%files zh_TW
%{gsdir}/FAPIcidfmap.zh_TW
%{gsdir}/cidfmap.zh_TW
%{gsdir}/CIDFnmap.zh_TW


%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- update to new release by fcimport

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3
- initial release by fcimport

