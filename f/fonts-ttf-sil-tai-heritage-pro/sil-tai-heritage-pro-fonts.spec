Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-tai-heritage-pro-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-tai-heritage-pro-fonts
# SPDX-License-Identifier: MIT
Version: 2.600

Release: alt1_6

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Tai Heritage Pro
%global fontsummary       Tai Heritage Pro, a traditional style Tai Viet script font family
%global projectname       taiheritagepro
%global archivename       TaiHeritagePro-%{version}
URL:                      https://software.sil.org/taiheritage/
%global fonts             *.ttf
%global fontdescription   \
The Tai people of northwestern Vietnam and surrounding areas have a long\
tradition of literacy in the Tai Viet script. Tai Heritage Pro reflects the\
traditional style of this script.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-sil-tai-heritage-pro-fonts.xml

Name:           fonts-ttf-sil-tai-heritage-pro
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
%linuxtext *txt documentation/*txt documentation/developer/*txt

%build
# fontbuild 
fontnames=$(
  for font in 'TaiHeritagePro-Bold.ttf' 'TaiHeritagePro-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'TaiHeritagePro-Bold.ttf' 'TaiHeritagePro-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-tai-heritage-pro-fonts appstream file"
cat > "org.altlinux.sil-tai-heritage-pro-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-tai-heritage-pro-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Tai Heritage Pro</name>
  <summary><![CDATA[Tai Heritage Pro, a traditional style Tai Viet script font family]]></summary>
  <description>
    <p><![CDATA[The Tai people of northwestern Vietnam and surrounding areas have a long]]></p><p><![CDATA[tradition of literacy in the Tai Viet script. Tai Heritage Pro reflects the]]></p><p><![CDATA[traditional style of this script.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/taiheritage/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-tai-heritage-pro-fonts
echo "" > "sil-tai-heritage-pro-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-tai-heritage-pro/
echo "%%dir %_fontsdir/ttf/sil-tai-heritage-pro" >> "sil-tai-heritage-pro-fonts.list"
install -m 0644 -vp "TaiHeritagePro-Bold.ttf" %buildroot%_fontsdir/ttf/sil-tai-heritage-pro/
echo \"%_fontsdir/ttf/sil-tai-heritage-pro//$(basename "TaiHeritagePro-Bold.ttf")\" >> 'sil-tai-heritage-pro-fonts.list'
install -m 0644 -vp "TaiHeritagePro-Regular.ttf" %buildroot%_fontsdir/ttf/sil-tai-heritage-pro/
echo \"%_fontsdir/ttf/sil-tai-heritage-pro//$(basename "TaiHeritagePro-Regular.ttf")\" >> 'sil-tai-heritage-pro-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'TaiHeritagePro-Bold.ttf' 'TaiHeritagePro-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-tai-heritage-pro-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-tai-heritage-pro-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-tai-heritage-pro-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-tai-heritage-pro-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-tai-heritage-pro-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-tai-heritage-pro-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-tai-heritage-pro-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-tai-heritage-pro-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-tai-heritage-pro -f sil-tai-heritage-pro-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.600-alt1_6
- new version

