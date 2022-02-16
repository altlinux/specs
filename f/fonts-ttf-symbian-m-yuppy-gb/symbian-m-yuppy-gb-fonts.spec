Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname symbian-m-yuppy-gb-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname symbian-m-yuppy-gb-fonts
Version: 1.00
Release: alt1_5
URL:     https://www.businesswire.com/news/home/20100608005491/en/Monotype-Imaging-Contributes-Simplified-Chinese-Font-%%E2%%80%%9CMYuppy%%E2%%80%%9D

%global foundry           Symbian
%global fontlicense       EPL-1.0

%global fontlicenses      *.TXT

%global fontfamily        M Yuppy GB
%global fontsummary       M Yuppy GB, a Chinese font family with a unique, modern feel

%global fontdescription   \
Designed to appeal to young urban professionals, M Yuppy is a font family with\
a unique, modern feel. The design combines elements of handwriting with classic\
letter-form characteristics, such as open shapes and proper proportions that\
help the typeface retain legibility.

Source0: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium.ttf
Source1: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium_README.TXT
Source2: 65-symbian-m-yuppy-gb-fonts.xml

Name:           fonts-ttf-symbian-m-yuppy-gb
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fonts             %{SOURCE0}
%global fontconfngs       %{SOURCE2}
%setup -n %{oldname}-%{version} -q -c -T
cp %{SOURCE1} .
%linuxtext *TXT

%build
# fontbuild 
fontnames=$(
  for font in '%SOURCE0'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '%SOURCE0'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the symbian-m-yuppy-gb-fonts appstream file"
cat > "org.altlinux.symbian-m-yuppy-gb-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.symbian-m-yuppy-gb-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>EPL-1.0</project_license>
  <name>Symbian M Yuppy GB</name>
  <summary><![CDATA[M Yuppy GB, a Chinese font family with a unique, modern feel]]></summary>
  <description>
    <p><![CDATA[Designed to appeal to young urban professionals, M Yuppy is a font family with]]></p><p><![CDATA[a unique, modern feel. The design combines elements of handwriting with classic]]></p><p><![CDATA[letter-form characteristics, such as open shapes and proper proportions that]]></p><p><![CDATA[help the typeface retain legibility.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.businesswire.com/news/home/20100608005491/en/Monotype-Imaging-Contributes-Simplified-Chinese-Font-%%E2%%80%%9CMYuppy%%E2%%80%%9D</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing symbian-m-yuppy-gb-fonts
echo "" > "symbian-m-yuppy-gb-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/symbian-m-yuppy-gb/
echo "%%dir %_fontsdir/ttf/symbian-m-yuppy-gb" >> "symbian-m-yuppy-gb-fonts.list"
install -m 0644 -vp "%SOURCE0" %buildroot%_fontsdir/ttf/symbian-m-yuppy-gb/
echo \"%_fontsdir/ttf/symbian-m-yuppy-gb//$(basename "%SOURCE0")\" >> 'symbian-m-yuppy-gb-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE2'; do
      gen-fontconf -x "${fontconfng}" -w -f '%SOURCE0'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "symbian-m-yuppy-gb-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "symbian-m-yuppy-gb-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.symbian-m-yuppy-gb-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "symbian-m-yuppy-gb-fonts.list"
done

for fontlicense in 'MYuppyGB-Medium_README.TXT'; do
  echo %%doc "'${fontlicense}'" >> "symbian-m-yuppy-gb-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'symbian-m-yuppy-gb-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'symbian-m-yuppy-gb-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-symbian-m-yuppy-gb -f symbian-m-yuppy-gb-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 1.00-alt1_5
- new version

