Name:           cdogs-sdl
Version:        0.4
Release:        alt4_8
Summary:        C-Dogs is an arcade shoot-em-up
Group:          Games/Other
License:        GPLv2+
URL:            http://lumaki.com/code/cdogs/
Source0:        http://icculus.org/%{name}/files/src/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         cdogs-sdl-0.4-64bit.patch
Patch1:         cdogs-sdl-0.4-default-cfg.patch
Patch2:         cdogs-sdl-0.4-open.patch
BuildRequires:  libSDL_mixer-devel desktop-file-utils
Requires:       cdogs-data = 0.4
Source44: import.info

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilising the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the a.'dogfighta.' deathmatch mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.


%prep
%setup -q
%patch0 -p1 -z .64bit
%patch1 -p1 -z .cfg
%patch2 -p1 -z .open
sed -i 's/\r//' doc/original_readme.txt
# stop this from getting installed as %doc
rm doc/INSTALL


%build
pushd src
make %{?_smp_mflags} DATADIR=%{_datadir}/cdogs-data \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char" I_AM_CONFIGURED=yes cdogs
popd


%install
# DIY, as make install wants to install the data too, and thats in another rpm
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/cdogs $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
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
%doc doc/*
%{_bindir}/cdogs
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_7
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- converted from Fedora by srpmconvert script

