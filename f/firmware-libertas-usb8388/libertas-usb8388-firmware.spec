%define oldname libertas-usb8388-firmware
Summary: Firmware for Marvell Libertas USB 8388 Network Adapter
Name:    firmware-libertas-usb8388
Version: 5.110.22.p23
Release: alt2_6
# up the Epoch because the Marvel version scheme is less than Cozybit's
Epoch:   2
License: Redistributable, no modification permitted
Group:   System/Kernel and hardware
URL:     http://www.marvell.com/
Source0: http://dev.laptop.org/pub/firmware/libertas/usb8388-%{version}.bin
Source1: http://dev.laptop.org/pub/firmware/libertas/usb8388-%{version}.bin.md5
Source2: http://dev.laptop.org/pub/firmware/libertas/LICENSE
BuildArch: noarch
Source44: import.info

%description
Firmware for Marvell Libertas USB 8388 Network Adapter

%prep
%setup -c -T -q

cp -p %{SOURCE0} .
md5sum -c %{SOURCE1}

%build

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware
%{__install} -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/usb8388.bin
%{__install} -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/LICENSE.usb8388
sed -i 's/\r//' $RPM_BUILD_ROOT/lib/firmware/LICENSE.usb8388
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
/lib/firmware/usb8388.bin
%doc /lib/firmware/LICENSE.usb8388


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2:5.110.22.p23-alt2_6
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2:5.110.22.p23-alt1_6
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 2:5.110.22.p23-alt1_5
- initial import by fcimport

