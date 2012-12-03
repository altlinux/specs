# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(English.pm) unzip
# END SourceDeps(oneline)
%define oldname madan-fonts
%global fontname madan
%global fontconf 65-0-%{fontname}.conf

Name: fonts-ttf-madan
Version: 2.000
Release: alt3_9
Summary: Font for Nepali language
Group: System/Fonts/True type
License: GPL+
URL: http://madanpuraskar.org/
# Found new following working Source URL. Use wget to download this archive
Source0: http://download.com.np/uploads/nepali_unicode/madan.zip
Source1: %{oldname}-fontconfig.conf
Source2: ttf2sfd.pe
Source3: sfd2ttf.pe
BuildArch: noarch
BuildRequires: fontforge
BuildRequires: fontpackages-devel
# This patch will make sure "fc-scan madan.ttf |grep lang:" will show ne
Patch0: madan-fonts-2.000-bug842965-u0970.patch
Source44: import.info

%description
This package provides the Madan font for Nepali made by the
Madan Puraskar Pustakalaya project.

%prep
%setup -c -q
for file in madan/license.txt; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

cp -p %{SOURCE2} %{SOURCE3} .

chmod 755 ttf2sfd.pe sfd2ttf.pe
./ttf2sfd.pe madan/*.ttf
rm -rf madan/*ttf
%patch0 -p1 -b .added-u0970-character
./sfd2ttf.pe madan/*.sfd


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc %{fontname}/license.txt


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_9
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_6
- update to new release by fcimport

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_4
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_4
- initial release by fcimport

