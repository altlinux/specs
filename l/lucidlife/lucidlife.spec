Name:           lucidlife
Version:        0.9.2
Release:        alt3_9.1
Summary:        A Conway's Life simulator

Group:          Games/Other
License:        GPLv2+
URL:            http://linux.softpedia.com/get/GAMES-ENTERTAINMENT/Simulation/LucidLife-26633.shtml
Source0:        http://mirror.thecodergeek.com/src/lucidlife-0.9.2.tar.gz
Patch0:		%{name}-make-docs-use-proper-dir.patch
Patch1: 	%{name}-fix-FSF-address.patch
Patch2: %name-0.9.2-alt-DSO.patch

BuildRequires:  libgtk+2-devel >= 2.6.0
BuildRequires:	gnome-vfs-devel
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML/Parser.pm)
BuildRequires:	gettext
Source44: import.info

%description
LucidLife is a Conway's Life simulator. The rules are rather simple. The game
is started with a large grid of cell locations, and an arbitrary set of
living cells. On each turn, each cell thrives or dies based on the number of 
cells which surround it. A dead (empty) cell with three live cells around it
becomes a living cell (a birth); a living cell with two or three neighbors
survives; otherwise the cell dies (due to overcrowding) or remains dead
(due to loneliness). It is based on the the GtkLife project, but with a
more modern user interface and other enhancements.


%prep
%setup -q
%patch0 -p0 -b .make-docs-use-proper-dir
%patch1 -p0 -b .fix-FSF-address
%patch2 -p2


%build
%configure LDFLAGS='-lX11'
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install 	\
	--dir %{buildroot}%{_datadir}/applications	\
	--delete-original	\
	--remove-category=Application	\
	--add-category=LogicGame	\
	%{buildroot}%{_datadir}/applications/lucidlife.desktop
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
 

%files -f %{name}.lang 
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/*.png doc/*.html doc/*.gif doc/*.css
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3_9.1
- Fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt3_9
- rebuild with fixed sourcedep analyser (#27020)

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_9
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_8
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_7
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_5
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_5
- converted from Fedora by srpmconvert script

* Sun Oct 05 2008 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Initial build from FC

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.2-2
- Update License tag (GPLv2+).
- Rebuild with new BuildID-enabled binutils.

* Sun Apr 29 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.2-1
- Update to new upstream bugfix release (0.9.2)
- Drop .desktop encoding fix (merged upstream):
  - add-.desktop-encoding.patch
- Use %%name in the %%files listing instead of hardcoding it, for consistency
  with my other packages; and use the $(VERSION) macro in the autotools build
  scripts to ease version bumps/updates.

* Fri Apr 20 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.1-3
- Ammend make-docs-use-proper-dir patch to ensure that the "Help" menu
  functionality works properly. (Thanks to Leonard A. Hickey for the patch;
  resolves bug #237329.)

* Sun Mar 11 2007 Peter Gordon <peter@thecodergeek.com> - 0.9.1-2
- Add LogicGame to the categories of the installed .desktop file for improved
  organization with games-menus.
- Rework patch calls for more readability.

* Sat Oct 28 2006 Peter Gordon <peter@thecodergeek.com> - 0.9.1-1
- Update to new upstream release (0.9.1)
- Drop X-Fedora and Application categories in installed .desktop file
- Add patch (sent upstream) to add Encoding=UTF-8 in installed .desktop file:
  + add-.desktop-encoding.patch
- Add %%name prefix to old make-docs-use-proper-dir patch filename
  to keep it all in the same logical namespace.

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-11
- Mass FC6 rebuild

* Sat Jul 22 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-10
- Add gettext as a build requirement to fix reduced mock build NLS issues.
  Thanks again, Matt.

* Tue Jul 18 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-9
- Add perl(XML::Parser) as a build requirement to fix reduced mock build
  (#199355) Thanks for your build report, Matt Domsch.
- Fix up zero-padding for single-digit dates in the %%changelog for
  consistency.

* Sat Apr 08 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-8
- Use desktop-file-install's "--delete-original" option instead of doing
  it manually.

* Tue Mar 28 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-7
- Add patch to put the documentation and %%doc stuff in the same directory.

* Sun Mar 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-6
- Bump release due to CVS tagging not liking me.

* Sun Mar 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-5
- Rebuild for new dist tag in FE Devel.

* Wed Mar 15 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-4
- Rebuild for spec file fixes and email address change.

* Sun Feb 26 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-3
- Add %%{?dist} tag to the release to fix CVS tagging issue.

* Sun Feb 19 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-2
- Dropped Requires: on gtk2 and gnome-vfs2, as the -devel sonames will pull
  these in.
- Fixed handling of .desktop file to conform to Fedora Extras guidelines.
- Changed %%files section to use %%{_datadir}/%%{name} instead of hardcoding
  "lucidlife" to help prevent file ownership problems
- Thanks to Brian Pepple in BZ #177881 for these suggestions.

* Sun Jan 15 2006 Peter Gordon <peter@thecodergeek.com> - 0.9-1
- Initial packaging.
