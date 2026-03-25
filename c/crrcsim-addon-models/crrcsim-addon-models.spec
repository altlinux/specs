Name:          crrcsim-addon-models
Version:       0.2.0
Release:       alt1
Group: Games/Other
Summary:       Model-Airplane Flight Simulation Program addon models
# Automatically converted from old format: CC-BY - review is highly recommended.
License:       LicenseRef-Callaway-CC-BY
URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
Source0:       http://prdownloads.sourceforge.net/crrcsim/%{name}/%{name}-%{version}.zip
Source1:       http://creativecommons.org/licenses/by/3.0/legalcode.txt
Source2:       crrcsim-addon-models-license-question-arthur.eml
Source3:       crrcsim-addon-models-license-question-jan.eml
Requires:      crrcsim >= 0.9.5
BuildArch:     noarch
BuildRequires: unzip

%description
Addon models for Crrcsim


%prep
%setup -qcn %{name}-%{version}

# Correct EOL (preserve timestamps).
for i in \
    Readmefirst_Ellipse.txt \
    Readmefirst_Nyx.txt \
    Readmefirst_Europhia2k.txt \
    Readmefirst_Fireworks3.txt \
    Readmefirst_Skorpion.txt \
    Readmefirst_Freestyler.txt \
    Readmefirst_Crossfire.txt \
    install-cam.txt \
    Readmefirst_Erwin.txt; do
        sed 's#\r##g' documentation/$i > documentation/$i.tmp && \
        touch -r documentation/$i documentation/$i.tmp && \
        mv documentation/$i.tmp documentation/$i
done


%build


%install
mkdir -p %{buildroot}/%{_datadir}/crrcsim/

# Remove duplicates and older versions
rm documentation/Readmefirst_Crossfire.txt

rm models/Crossfire.xml \
   models/Erwin.xml \
   models/PilatusB4.xml \
   models/supra.xml

rm objects/Crossfire.ac \
   objects/Erwin.ac \
   objects/Fireworks_C.ac \
   objects/supra.ac

rm textures/CrossfireTexture.rgb \
   textures/Erwin.rgb \
   textures/Fireworks2.rgb \
   textures/PilB4Texture.rgb \
   textures/supra_texture_256.rgb

cp -ar models objects textures %{buildroot}/%{_datadir}/crrcsim
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%files
%doc documentation/*.txt legalcode.txt *.eml
%{_datadir}/crrcsim/models/*.xml
%{_datadir}/crrcsim/objects/*.ac
# Already exists in crrcsim-v0.9.13
%exclude %{_datadir}/crrcsim/objects/PilatusB4.ac
%{_datadir}/crrcsim/textures/*.rgb


%changelog
* Thu Mar 26 2026 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt1
- Initial build for Sisyphus

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-9
- Exclude PilatusB4 object which exists in crrcsim-v0.9.13 (rhbz#1510107)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-2
- preserve timestamps during EOL conversion,
- license clarification e-mails added.

* Wed Jul 11 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-1
- initial RPM release.
