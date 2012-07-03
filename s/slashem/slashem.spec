# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           slashem
Version:        0.0.8
Release:        alt2_0.8.E0F1
Summary:        Super Lotsa Added Stuff Hack - Extended Magic

Group:          Games/Other
License:        NGPL
URL:            http://slashem.sourceforge.net/
Source0:        http://downloads.sourceforge.net/slashem/se008e0f1.tar.gz
Source1:        %{name}.desktop
Patch0:         slashem-config.patch
# fix building with libpng 1.5
Patch1:         slashem-libpng-1.5.patch

BuildRequires:  libncurses-devel
BuildRequires:  bison flex desktop-file-utils
BuildRequires:  bdftopcf libX11-devel libXaw-devel libXext-devel
BuildRequires:  libXmu-devel libXpm-devel libXt-devel
BuildRequires:  libSDL-devel libGL-devel libpng-devel zlib-devel
# to compress save files
Requires:       bzip2
# for X11 core fonts

%global fa_var      /var/games/%{name}
%global fa_save     /var/games/%{name}/save
%global fa_share    %{_datadir}/games/%{name}
%global fa_unshare  %{_libdir}/games/%{name}
%global fa_doc      %{_defaultdocdir}/%{name}-%{version}
Source44: import.info

%description
From the land before 3DFX, before VGA graphics and DOOM, before the IBM PC, way
back in the dark ages of Unixland, there was a game. They called it Rogue.
People played it, and found it good. From this basis, Hack was born. Soon Hack
became Nethack, because it was developed by many people (and has nothing to do
with hacking the internet). And people played this on many machines, from
Unices to Macs to PCs, due to the amazing power of Open Source Code.

But the DevTeam, the reclusive masterminds of Nethack, are a rather quiet
bunch, gracing the world with new versions as they see fit, and when they see
fit. Which is usually a new version every good number of years.

And there was much gnashing of teeth.

But because of the Freely Available Source Code Phenomenon, people began making
their own versions of Nethack to tide themselves between magical releases.

SLASH'EM is the (continuing) saga of one such variant...


%prep
%setup -q -n %{name}-%{version}E0F1
%patch0 -p 1 -b .config
%patch1 -p 1 -b .libpng

sed -i \
    -e 's:^\(#define FILE_AREA_VAR\).*:\1 "%{fa_var}/":' \
    -e 's:^\(#define FILE_AREA_SAVE\).*:\1 "%{fa_save}/":'  \
    -e 's:^\(#define FILE_AREA_SHARE\).*:\1 "%{fa_share}/":' \
    -e 's:^\(#define FILE_AREA_UNSHARE\).*:\1 "%{fa_unshare}/":' \
    -e 's:^\(#define FILE_AREA_DOC\).*:\1 "%{fa_doc}/":' \
    include/unixconf.h


for f in *.txt ; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done


%build
export LIBXAW_CFLAGS="-I/usr/include"
export LIBXAW_LIBS="$(pkg-config --libs xaw7)"
%configure \
    --enable-tty-graphics   \
    --enable-x11-graphics   \
    --enable-sdl-graphics   \
    --enable-gl-graphics    \
    --enable-data-librarian \
    --enable-sinks          \
    --enable-reincarnation  \
    --enable-zouthern       \
    --enable-score-on-botl  \
    --enable-wizmode=games
# smp_mflags fails
make \
    FILE_AREA_VAR=%{fa_var} \
    FILE_AREA_SAVE=%{fa_save} \
    FILE_AREA_SHARE=%{fa_share} \
    FILE_AREA_UNSHARE=%{fa_unshare} \
    FILE_AREA_DOC=%{fa_doc} \
    SHELLDIR=%{_bindir}

%install
make install DESTDIR=%{buildroot} \
    FILE_AREA_VAR=%{buildroot}%{fa_var} \
    FILE_AREA_SAVE=%{buildroot}%{fa_save} \
    FILE_AREA_SHARE=%{buildroot}%{fa_share} \
    FILE_AREA_UNSHARE=%{buildroot}%{fa_unshare} \
    FILE_AREA_DOC=%{buildroot}%{fa_doc} \
    SHELLDIR=%{buildroot}%{_bindir} \
    CHOWN=/bin/true \
    CHGRP=/bin/true

install -d -m 0755 %{buildroot}%{_mandir}/man6
make -C doc MANDIR=%{buildroot}%{_mandir}/man6 manpages

sed -i \
    -e 's!%{buildroot}!!g' \
    -e '/XUSERFILE/s!\$HACKDIR!%{fa_share}!' \
    %{buildroot}%{_bindir}/slashem

mv %{buildroot}%{fa_unshare}/recover %{buildroot}%{_bindir}/slashem-recover
mv %{buildroot}%{_mandir}/man6/recover.6 %{buildroot}%{_mandir}/man6/slashem-recover.6
rm %{buildroot}%{_mandir}/man6/[^s]*

sed -i -e 's:^!\(SlashEM.tile_file.*\):\1:' %{buildroot}%{fa_share}/SlashEM.ad

install -D -p -m 0644 win/X11/nh_icon.xpm %{buildroot}%{_datadir}/pixmaps/slashem.xpm
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category X-Fedora \
    --add-category Application \
    --add-category Game \
    %{SOURCE1}
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
%doc history.txt doc/*.txt README.34 readme.* slamfaq.txt dat/license dat/history
%{_bindir}/slashem
%{_bindir}/slashem-recover
%{fa_share}
%dir %{fa_unshare}
%{fa_unshare}/nhushare
%{_mandir}/man6/*
%{_datadir}/applications/slashem.desktop
%{_datadir}/pixmaps/slashem.xpm
%defattr(0664,root,games)
%config(noreplace) %{fa_var}/logfile
%config(noreplace) %{fa_var}/perm
%config(noreplace) %{fa_var}/record
%attr(0775,root,games) %dir %{fa_var}
%attr(0775,root,games) %dir %{fa_var}/save
%attr(2711,root,games) %{fa_unshare}/slashem


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2_0.8.E0F1
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_0.8.E0F1
- update to new release by fcimport

* Sat Jul 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_0.6.E0F1
- initial release by fcimport

