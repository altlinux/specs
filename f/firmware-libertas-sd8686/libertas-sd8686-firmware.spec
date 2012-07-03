%define oldname libertas-sd8686-firmware
Summary: Firmware for Marvell Libertas SD 8686 Network Adapter
Name:    firmware-libertas-sd8686
Version: 9.70.20.p0
Release: alt2_2
License: Redistributable, no modification permitted
Group:   System/Kernel and hardware
URL:     http://www.marvell.com/
Source0: http://dev.laptop.org/pub/firmware/libertas/sd8686-%{version}.bin
Source1: http://dev.laptop.org/pub/firmware/libertas/sd8686_helper.bin
Source2: http://dev.laptop.org/pub/firmware/libertas/LICENSE
BuildArch: noarch

Requires: udev
Source44: import.info

%description
Firmware for Marvell Libertas SD 8686 Network Adapter

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
cp -p %{SOURCE2} LICENSE
sed -i 's/\r//' LICENSE

%build

%install
%{__install} -D -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/sd8686.bin
%{__install} -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/sd8686_helper.bin
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
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
%doc LICENSE
/lib/firmware/*.bin


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 9.70.20.p0-alt2_2
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 9.70.20.p0-alt1_2
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 9.70.20.p0-alt1_1
- initial import by fcimport

