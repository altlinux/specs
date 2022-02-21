Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-alkalami-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-alkalami-fonts
# SPDX-License-Identifier: MIT
Version: 1.200
Release: alt1_6

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alkalami
%global fontsummary       A font family for the Arabic scripts of the Kano region of Nigeria and Niger
%global projectname       alkalami
%global archivename       Alkalami-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Alkalami is a font family for Arabic-based writing systems in the Kano region\
of Nigeria and in Niger. This style of writing African Ajami has sometimes been\
called Sudani Kufi or Rubutun Kano.\
\
AlkC.lami (pronounced al-KA-la-mi) is the local word for the Arabic a.'qalama.', a\
type of sharpened stick used for writing on wooden boards in the Kano region of\
Nigeria and in Niger, and what gives the style its distinct appearance. The\
baseline stroke is very thick and solid. The ascenders and other vertical\
strokes including the teeth are very narrow when compared to the baseline. A\
generous line height is necessary to allow for deep swashes and descenders, and\
the overall look of the page is a very black, solid rectangle. Diacritics are\
much smaller in scale, with very little distance from the main letters.\
\
The Alkalami font supports the characters known to be used by languages written\
with the Kano style of Arabic script, but may not have the characters needed\
for other languages.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 66-sil-alkalami-fonts.xml

Name:           fonts-ttf-sil-alkalami
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt

%build
# fontbuild 
fontnames=$(
  for font in 'Alkalami-Light.ttf' 'Alkalami-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Alkalami-Light.ttf' 'Alkalami-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-alkalami-fonts appstream file"
cat > "org.altlinux.sil-alkalami-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-alkalami-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Alkalami</name>
  <summary><![CDATA[A font family for the Arabic scripts of the Kano region of Nigeria and Niger]]></summary>
  <description>
    <p><![CDATA[Alkalami is a font family for Arabic-based writing systems in the Kano region]]></p><p><![CDATA[of Nigeria and in Niger. This style of writing African Ajami has sometimes been]]></p><p><![CDATA[called Sudani Kufi or Rubutun Kano.]]></p> Alkǎlami (pronounced al-KA-la-mi) is the local word for the Arabic “qalam”, a type of sharpened stick used for writing on wooden boards in the Kano region of Nigeria and in Niger, and what gives the style its distinct appearance. The baseline stroke is very thick and solid. The ascenders and other vertical strokes including the teeth are very narrow when compared to the baseline. A generous line height is necessary to allow for deep swashes and descenders, and the overall look of the page is a very black, solid rectangle. Diacritics are much smaller in scale, with very little distance from the main letters. The Alkalami font supports the characters known to be used by languages written with the Kano style of Arabic script, but may not have the characters needed for other languages.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-alkalami-fonts
echo "" > "sil-alkalami-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-alkalami/
echo "%%dir %_fontsdir/ttf/sil-alkalami" >> "sil-alkalami-fonts.list"
install -m 0644 -vp "Alkalami-Light.ttf" %buildroot%_fontsdir/ttf/sil-alkalami/
echo \"%_fontsdir/ttf/sil-alkalami//$(basename "Alkalami-Light.ttf")\" >> 'sil-alkalami-fonts.list'
install -m 0644 -vp "Alkalami-Regular.ttf" %buildroot%_fontsdir/ttf/sil-alkalami/
echo \"%_fontsdir/ttf/sil-alkalami//$(basename "Alkalami-Regular.ttf")\" >> 'sil-alkalami-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Alkalami-Light.ttf' 'Alkalami-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-alkalami-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-alkalami-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-alkalami-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-alkalami-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-alkalami-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-alkalami-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-alkalami-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-alkalami-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-alkalami -f sil-alkalami-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*.pdf

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.200-alt1_6
- new version

