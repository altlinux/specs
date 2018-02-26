%define common_desc \
ghostscript font configuration files for Chinese fonts.


%define gsdir            %{_datadir}/ghostscript/conf.d
%define umingver         0.2.20080216.1
%define ukaiver          0.2.20080216.1
%define zenheiver        0.9.45

Name:           ghostscript-chinese
Version:        0.3.1
Release:        alt2_4
Summary:        Ghostscript Chinese fonts configuration files
Group:          System/Fonts/True type
License:        GPLv2+
URL:            http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:        http://pwu.fedorapeople.org/ghostscript-chinese/ghostscript-chinese-%{version}.tar.gz
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
Requires:     ghostscript-chinese = %{version}-%{release}

%description zh_CN
%common_desc

For Simplified Chinese.

%package zh_TW
Summary:      Ghostscript Traditional Chinese fonts configuration files
Group:        System/Fonts/True type
Requires:     ghostscript-utils ghostscript
Requires:     fonts-ttf-cjkuni-uming = %{umingver}
Requires:     fonts-ttf-cjkuni-ukai = %{ukaiver}
Requires:     ghostscript-chinese = %{version}-%{release}

%description zh_TW
%common_desc

For Traditional Chinese.

%prep
%setup -q -c -n %{name}-%{version}


%build
%{nil}


%install
install -m 0755 -d %{buildroot}%{gsdir}

#Note modify the absolute path of zenhei fonts in ghostscript files.
for gscid in `ls *.zh_CN`
do
    cat $gscid | sed --expression='s/###zenheiloc###/\/usr\/share\/fonts\/wqy-zenhei/g' > tmp_gs
    mv tmp_gs $gscid
    install -m 0644 -p $gscid %{buildroot}%{gsdir}
done

#Note modify the absolute path of uming/ukai fonts in ghostscript files.
for gscid in `ls *.zh_TW`
do
    cat $gscid | sed --expression='s/###ukailoc###/\/usr\/share\/fonts\/cjkuni-ukai/g' --expression='s/###umingloc###/\/usr\/share\/fonts\/cjkuni-uming/g' > tmp_gs
    mv tmp_gs $gscid
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- update to new release by fcimport

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3
- initial release by fcimport

