%define oldname taipeifonts
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name taipeifonts
%define version 1.2
%define fontname taipeifonts
%define common_desc Traditional Chinese Bitmap fonts

%define bmpfontdir    %{_datadir}/fonts/bitmap/%{oldname}
%define catalogue     /etc/X11/fontpath.d

Name:       fonts-bitmap-taipei
Version:    1.2
Release:    alt1_14
Summary:    %common_desc

Group:      Graphical desktop/Other
License:    Public Domain
URL:        http://cle.linux.org.tw/

BuildArch:        noarch
BuildRequires:    xorg-x11-font-utils

Source0:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/%{oldname}-%{version}.tar.gz
Source1:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/%{oldname}.alias
Source2:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/re-build.readme
Source44: import.info

%description
%common_desc

%prep
%setup -q -n %{oldname}-%{version}
cp -p %SOURCE2 README

%build
bdftopcf taipei24.bdf | gzip -c > taipei24.pcf.gz
bdftopcf taipei20.bdf | gzip -c > taipei20.pcf.gz
bdftopcf taipei16.bdf | gzip -c > taipei16.pcf.gz

%install

install -d $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei20.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei16.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 vga12x24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{bmpfontdir}/fonts.alias

mkfontdir $RPM_BUILD_ROOT%{bmpfontdir}

# catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -s %{bmpfontdir} $RPM_BUILD_ROOT%{catalogue}/%{oldname}
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
%doc README
%dir %{bmpfontdir}
%{bmpfontdir}/*.gz
%{bmpfontdir}/fonts.alias
%verify(not md5 size mtime) %{bmpfontdir}/fonts.dir
%{catalogue}/%{oldname}*

%changelog
* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_14
- fc import

