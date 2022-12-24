Group: System/Fonts/True type
%define oldname baekmuk-bdf-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: rpm-build-fedora-compat-fonts
%global fontname   baekmuk-bdf

%global fontdir      %_bitmapfontsdir/%{fontname}
%global catalogue    %{_sysconfdir}/X11/fontpath.d

Name:           fonts-bitmap-baekmuk
Version:        2.2
Release:        alt3_33
Summary:        Korean bitmap fonts

License:        Baekmuk
URL:            http://kldp.net/projects/baekmuk/
Source:  http://kldp.net/frs/download.php/1428/%{fontname}-%{version}.tar.gz
Patch0:	 baekmuk-bdf-fonts-fix-fonts-alias.patch
BuildArch:      noarch
BuildRequires:  mkfontdir bdftopcf
Source44: import.info

%description
This package provides the Korean Baekmuk bitmap fonts.


%prep
%setup -q -n %{fontname}-%{version}
%patch0 -p1 -b .fix-fonts-alias

%build
for file in bdf/*.bdf; do
    bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done

%install

install -d $RPM_BUILD_ROOT%{fontdir}

# for bmp font
install -m 0644 bdf/*.pcf.gz $RPM_BUILD_ROOT%{fontdir}/
install -m 0444 bdf/fonts.alias $RPM_BUILD_ROOT%{fontdir}/

# for catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -sf ../../..%{fontdir} $RPM_BUILD_ROOT%{catalogue}/%{oldname}

mkfontdir $RPM_BUILD_ROOT%{fontdir} 

# convert Korean copyright file to utf8
iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko

%files
%doc COPYRIGHT COPYRIGHT.ko README
%dir %{fontdir}
%{fontdir}/*.gz
%{fontdir}/fonts.alias
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%{catalogue}/*


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.2-alt3_33
- update to new release by fcimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 2.2-alt3_29
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_24
- sync with fc

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_12
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_11
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_11
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_10
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_9
- rebuild with rpm-build-fonts alt3

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_9
- initial release by fcimport

