Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-goschen-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-goschen-fonts
# SPDX-License-Identifier: MIT
Version: 20100203
Release: alt3_21
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Goschen
%global fontsummary       GFS GA.schen, a 19th century neoclassical cursive Greek font family
%global fonts             *.otf
%global fontdescription   \
Georg Joachim GA.schen founded in 1782 the publishing house of G.J.\
GA.schensche Verlagsbuchhandlung in Leipzig and was one of the most active\
publishers of the period in Germany. GA.schen was very interested in\
typography, influenced by the fame and quality of the editions of G. Bodoni\
and F. Didot.\
\
In 1797, he collaborated with the leading scholar of the period, Johann Jakob\
Griesbach, to edit and publish the New Testament in Greek for which he formed\
a committee of scholars to decide the new Greek type which were eventually\
cut by Johann Prillwitz. The book appeared in 1803 and the types show many\
influences from the Greek types of Bodoni. Their characteristic was the\
neoclassical form of marked contrast between thick and thin strokes, the\
cursive style and the large size of the font.\
\
The design was too cumbersome to allow general use and can be considered\
successful only for its indirect influence on the later cut Greek Leipzig\
type. It is, however, part of the greater heritage of Greek type design and\
therefore the type has been digitized by George D. Matthiopoulos in 2009 and\
is part of GFSa.' type library under the name GFS GA.schen cursive, in\
commemoration of the great German publisher.

%global archivename GFS_Goschen

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 64-gfs-goschen-fonts.xml

Name:           fonts-otf-gfs-goschen
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
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'GFS Goschen-Italic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFS Goschen-Italic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-goschen-fonts appstream file"
cat > "org.altlinux.gfs-goschen-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-goschen-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Goschen</name>
  <summary><![CDATA[GFS Göschen, a 19th century neoclassical cursive Greek font family]]></summary>
  <description>
    <p><![CDATA[Georg Joachim Göschen founded in 1782 the publishing house of G.J.]]></p><p><![CDATA[Göschensche Verlagsbuchhandlung in Leipzig and was one of the most active]]></p><p><![CDATA[publishers of the period in Germany. Göschen was very interested in]]></p><p><![CDATA[typography, influenced by the fame and quality of the editions of G. Bodoni]]></p><p><![CDATA[and F. Didot.]]></p> In 1797, he collaborated with the leading scholar of the period, Johann Jakob Griesbach, to edit and publish the New Testament in Greek for which he formed a committee of scholars to decide the new Greek type which were eventually cut by Johann Prillwitz. The book appeared in 1803 and the types show many influences from the Greek types of Bodoni. Their characteristic was the neoclassical form of marked contrast between thick and thin strokes, the cursive style and the large size of the font. The design was too cumbersome to allow general use and can be considered successful only for its indirect influence on the later cut Greek Leipzig type. It is, however, part of the greater heritage of Greek type design and therefore the type has been digitized by George D. Matthiopoulos in 2009 and is part of GFS’ type library under the name GFS Göschen cursive, in
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-goschen-fonts
echo "" > "gfs-goschen-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-goschen/
echo "%%dir %_fontsdir/otf/gfs-goschen" >> "gfs-goschen-fonts.list"
install -m 0644 -vp "GFS Goschen-Italic.otf" %buildroot%_fontsdir/otf/gfs-goschen/
echo \"%_fontsdir/otf/gfs-goschen//$(basename "GFS Goschen-Italic.otf")\" >> 'gfs-goschen-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFS Goschen-Italic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-goschen-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-goschen-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-goschen-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-goschen-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-goschen-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-goschen-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-goschen-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-goschen-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-goschen -f gfs-goschen-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20100203-alt3_21
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100203-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20100203-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 20100203-alt1_2
- initial release by fcimport

