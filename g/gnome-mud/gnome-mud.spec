# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gconftool-2 pkgconfig(gmodule-2.0) zlib-devel
# END SourceDeps(oneline)
Name:		gnome-mud
Version:	0.11.2
Release:	alt2_10
Summary:	A MUD client for GNOME

Group:		Games/Other
License:	GPLv2+
URL:		http://live.gnome.org/GnomeMud
Source:		http://ftp.gnome.org/pub/gnome/sources/%{name}/0.11/%{name}-%{version}.tar.gz

# https://bugzilla.gnome.org/show_bug.cgi?id=625739
Patch0:		gnome-mud-desktop.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=629472
Patch1:		gnome-mud-vte.patch

BuildRequires: gettext
BuildRequires: libgtk+2-devel
BuildRequires: libpcre-devel
BuildRequires: gstreamer-devel
BuildRequires: libgnet-devel
BuildRequires: libvte-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libglade-devel
BuildRequires: libGConf-devel

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2
Source44: import.info

%description
GNOME-MUD is a simple MUD client for GNOME. It supports scripting in
Python and C, and tabbed mudding.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
iconv -f iso-8859-1 -t utf8 ./AUTHORS > ./AUTHORS.utf8
mv ./AUTHORS.utf8 ./AUTHORS

%build
%configure --enable-mccp --enable-gstreamer
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
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

%pre
if [ "$1" -gt 1 ] ; then
	export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
	gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi

%post 
export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null

%preun
if [ "$1" -eq 0 ] ; then
	export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
	gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6.*

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_10
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_9
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_7
- initial release by fcimport

