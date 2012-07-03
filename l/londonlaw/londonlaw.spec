%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           londonlaw
Version:        0.2.1
Release:        alt2_11
Summary:        Online multiplayer version of a well known detective boardgame
License:        GPLv2
Group:          Games/Other
URL:            http://pessimization.com/software/londonlaw/
Source0:        http://pessimization.com/software/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-server.desktop
Patch0:         londonlaw-0.2.1-new-twisted.patch
BuildRequires:  python-devel wxPython /usr/bin/latex texlive-latex-recommended ghostscript-utils ghostscript ImageMagick
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       wxPython python-module-twisted-core
Source44: import.info

%description
London Law is an online multiplayer version of a well known detective
boardgame. The game is unusually asymmetric; one player controls the movements
of the criminal Mr. X as he tries to evade the detectives, while another one to
five players control five detectives trying to track him down. Mr. X has an
advantage in access to transportation routes, and his precise location remains
hidden for most of the game. The detectives have only the advantage of superior
numbers, so they must work in concert to limit the criminal's options. London
Law features an attractive map overlaid on high-resolution satellite imagery.


%prep
%setup -q
%patch0 -p1
chmod +x setup.py


%build
./setup.py build
make -C doc manual.pdf


%install
./setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
# already in /usr/bin
rm $RPM_BUILD_ROOT%{python_sitelib}/%{name}/london-{client,server}.py
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
convert londonlaw/guiclient/images/playericon1.jpg -resize 48x48 \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  \
  %{SOURCE1}
desktop-file-install                \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  \
  %{SOURCE2}
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
%doc COPYING ChangeLog doc/TODO doc/*.pdf doc/readme.protocol
%{_bindir}/london-*
%{_datadir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py?.?.egg-info
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_11
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_11
- update to new release by fcimport

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1_10.1
- Rebuild with Python-2.7

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_10
- initial release by fcimport

