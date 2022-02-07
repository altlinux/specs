Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname astigmatic-grand-hotel-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname astigmatic-grand-hotel-fonts
Version:        1.000
Release:        alt1_15
URL:            http://www.astigmatic.com/

%global foundry           Astigmatic
%global fontlicense       OFL
%global fontlicenses      "SIL Open Font License.txt"

%global fontfamily        Grand Hotel
%global fontsummary       Script retro style fonts
%global fonts             *.otf
%global fontdescription   \
Grand Hotel finds its inspiration from the title screen of the 1937 film a.'Cafe \
Metropolea.' starring Tyrone Power. This condensed upright connecting script has \
a classic vibe to it.\
\
It has a wonderful weight to it that feels subtly tied to Holiday and Bakery \
themed designs, even though it can work outside that genre.

Source0:        https://www.fontsquirrel.com/fonts/download/grand-hotel/grand-hotel.zip
Source1:        61-astigmatic-grand-hotel-fonts.conf

Name:           fonts-otf-astigmatic-grand-hotel
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs         %{SOURCE1}
%setup -n %{oldname}-%{version} -q -c


%build
# fontbuild 
fontnames=$(
  for font in 'GrandHotel-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GrandHotel-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the astigmatic-grand-hotel-fonts appstream file"
cat > "org.altlinux.astigmatic-grand-hotel-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.astigmatic-grand-hotel-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Astigmatic Grand Hotel</name>
  <summary><![CDATA[Script retro style fonts]]></summary>
  <description>
    <p><![CDATA[Grand Hotel finds its inspiration from the title screen of the 1937 film “Cafe]]></p><p><![CDATA[Metropole” starring Tyrone Power. This condensed upright connecting script has]]></p><p><![CDATA[a classic vibe to it.]]></p> It has a wonderful weight to it that feels subtly tied to Holiday and Bakery
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.astigmatic.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "astigmatic-grand-hotel-fonts
echo "" > "astigmatic-grand-hotel-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/astigmatic-grand-hotel/
echo "%%dir %_fontsdir/otf/astigmatic-grand-hotel" >> "astigmatic-grand-hotel-fonts.list"
install -m 0644 -vp "GrandHotel-Regular.otf" %buildroot%_fontsdir/otf/astigmatic-grand-hotel/
echo \"%_fontsdir/otf/astigmatic-grand-hotel//$(basename "GrandHotel-Regular.otf")\" >> 'astigmatic-grand-hotel-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "astigmatic-grand-hotel-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "astigmatic-grand-hotel-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.astigmatic-grand-hotel-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "astigmatic-grand-hotel-fonts.list"
done

for fontlicense in 'SIL Open Font License.txt'; do
  echo %%doc "'${fontlicense}'" >> "astigmatic-grand-hotel-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'astigmatic-grand-hotel-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'astigmatic-grand-hotel-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-astigmatic-grand-hotel -f astigmatic-grand-hotel-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.000-alt1_15
- update to new release by fcimport

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1_5
- new version

