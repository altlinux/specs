# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           icc-profiles-openicc
Version:        1.3.1
Release:        alt2_13
Summary:        The OpenICC profiles

Group:          Graphics
License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/OpenICC-Profiles/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  color-filesystem rpm-macros-color
Requires:       color-filesystem rpm-macros-color
Source44: import.info


%description
The OpenICC profiles are provided to serve color managed
applications and services.


%prep
%setup -q


%build
%configure --enable-verbose
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/{pixmaps,mime/packages}

install -pm 0644 *.png $RPM_BUILD_ROOT%{_datadir}/pixmaps



%files
%doc AUTHORS ChangeLog COPYING
%doc default_profiles/base/LICENSE-ZLIB
%doc default_profiles/base/LICENSE-ZLIB-LSTAR
%dir %{_icccolordir}/OpenICC
%{_icccolordir}/OpenICC/compatibleWithAdobeRGB1998.icc
%{_icccolordir}/OpenICC/sRGB.icc
%{_icccolordir}/OpenICC/ProPhoto-RGB.icc
%dir %{_icccolordir}/Oyranos
%{_icccolordir}/Oyranos/Gray-CIE_L.icc
%{_icccolordir}/Oyranos/Gray_linear.icc
%{_icccolordir}/Oyranos/ITULab.icc
%dir %{_icccolordir}/basICColor
%{_icccolordir}/basICColor/LStar-RGB.icc
%dir %{_icccolordir}/lcms
%{_icccolordir}/lcms/LCMSLABI.ICM
%{_icccolordir}/lcms/LCMSXYZI.ICM
%{_icccolordir}/lcms/Lab.icc
%{_icccolordir}/lcms/XYZ.icc
%dir %{_colordir}/target
%dir %{_colordir}/target/NPES
%{_colordir}/target/NPES/TR002.ti3
%{_colordir}/target/NPES/TR003.ti3
%{_colordir}/target/NPES/TR005.ti3
%{_colordir}/target/NPES/TR006.ti3
%dir %{_colordir}/target/fogra
%{_colordir}/target/fogra/FOGRA28L.ti3
%{_colordir}/target/fogra/FOGRA29L.ti3
%{_colordir}/target/fogra/FOGRA30L.ti3
%{_colordir}/target/fogra/FOGRA39L.ti3
%{_colordir}/target/fogra/FOGRA40L.ti3
%{_datadir}/icons/application-vnd.iccprofile.png
%{_datadir}/icons/text-vnd.cgats.png
%{_datadir}/mime/packages/x-color-cgats.xml
%exclude %{_datadir}/mime/packages/x-color-icc.xml
%{_datadir}/pixmaps/application-vnd.iccprofile.png
%{_datadir}/pixmaps/%{name}_logo.png
%{_datadir}/pixmaps/text-vnd.cgats.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_11
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_8
- update to new release by fcimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_7
- moved to Sisyphus as dependency to fop

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_7
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_3
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_2
- update to new release by fcimport

* Sat Jun 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- update to new fc release

