Name:           icc-profiles-basiccolor-printing2009
Version:        1.2.0
Release:        alt2_7
Summary:        The OpenICC profiles from basICColor

Group:          Graphical desktop/Other
License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/basICColor-Profiles/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: color-filesystem rpm-macros-color
Requires: color-filesystem rpm-macros-color
#Owns %%{_icccolordir}/basICColor
Requires:       icc-profiles-openicc
Source44: import.info



%description
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles for ISO Printing conditions.


%prep
%setup -q


%build
%configure --enable-verbose
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT



%files
%doc AUTHORS ChangeLog COPYING
%{_icccolordir}/basICColor/ISOcoated_v2_300_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_grey1c_bas.ICC
%{_icccolordir}/basICColor/ISOnewspaper_v4_26_bas.ICC
%{_icccolordir}/basICColor/ISOuncoatedyellowish_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_300_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Improved_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Standard_bas.ICC
%{_icccolordir}/basICColor/PSO_MFC_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_SNP_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/SC_paper_bas.ICC


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_6
- update to new release by fcimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_5
- moved to Sisyphus as dependency to fop

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_5
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3
- update to new release by fcimport

* Wed Oct 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- new version

