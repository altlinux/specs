Name:     papirus-icon-theme
Version:  20231101
Release:  alt2

Summary:  All Papirus icon themes
License:  GPLv3
Group:    Other
Url:      https://github.com/PapirusDevelopmentTeam/papirus-icon-theme

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: icon-theme-Papirus = %EVR
Requires: icon-theme-Papirus-Dark = %EVR
Requires: icon-theme-Papirus-Education = %EVR
Requires: icon-theme-Papirus-Light = %EVR
Requires: icon-theme-ePapirus = %EVR
Requires: icon-theme-ePapirus-Dark = %EVR

%description
Papirus is a free and open source SVG icon theme for Linux, based on
Paper Icon Set with a lot of new icons and a few extras, like
Hardcode-Tray support, KDE colorscheme support, Folder Color support,
and others.

Papirus icon theme is available in six variants:

* Papirus
* Papirus Dark
* Papirus Education
* Papirus Light
* ePapirus (for elementary OS and Pantheon Desktop only)
* ePapirus Dark (for elementary OS and Pantheon Desktop only)

%package -n icon-theme-Papirus
Summary: Papirus icon theme
Group: Other

%description -n icon-theme-Papirus
%summary.

%package -n icon-theme-Papirus-Dark
Summary: Papirus-Dark icon theme
Group: Other
Requires: icon-theme-Papirus

%description -n icon-theme-Papirus-Dark
%summary.

%package -n icon-theme-Papirus-Education
Summary: Papirus-Education icon theme
Group: Other
Requires: icon-theme-Papirus-Light

%description -n icon-theme-Papirus-Education
%summary.

%package -n icon-theme-Papirus-Light
Summary: Papirus-Light icon theme
Group: Other
Requires: icon-theme-Papirus

%description -n icon-theme-Papirus-Light
%summary.

%package -n icon-theme-ePapirus
Summary: ePapirus icon theme
Group: Other
Requires: icon-theme-Papirus

%description -n icon-theme-ePapirus
%summary.

%package -n icon-theme-ePapirus-Dark
Summary: ePapirus-Dark icon theme
Group: Other
Requires: icon-theme-Papirus
Requires: icon-theme-ePapirus

%description -n icon-theme-ePapirus-Dark
%summary.

%package -n papirus-remix-icon-theme
Summary: Remix of Papirus theme with all colors of folder icons
Group: Other
Requires: icon-theme-Papirus-Remix = %EVR
Requires: icon-theme-Papirus-Dark-Remix = %EVR
Requires: icon-theme-Papirus-Light-Remix = %EVR

%description -n papirus-remix-icon-theme
Papirus Remix is a remix of Papirus icon theme for easy selection
of different color themes.

Papirus Remix icon theme is available in three variants for every of 25 folder colors:

* Papirus <Color>
* Papirus Dark <Color>
* Papirus Light <Color>

%package -n icon-theme-Papirus-Remix
Summary: Papirus Remix icon theme
Group: Other

%description -n icon-theme-Papirus-Remix
%summary.

%package -n icon-theme-Papirus-Dark-Remix
Summary: Papirus Dark Remix icon theme
Group: Other
Requires: icon-theme-Papirus-Remix

%description -n icon-theme-Papirus-Dark-Remix
%summary.

%package -n icon-theme-Papirus-Light-Remix
Summary: Papirus Light Remix icon theme
Group: Other
Requires: icon-theme-Papirus-Remix

%description -n icon-theme-Papirus-Light-Remix
%summary.

%prep
%setup

%build
# Make network menu item in ALT looks like upstream Internet menu item
for i in 16 22 24 32 48 64;do
    ln -s internet-web-browser.svg Papirus/${i}x${i}/apps/applications-network.svg
done

# Make new theme Papirus-Education with orange folder icons
color=orange
THEME_DIR=Papirus-Edu
mkdir $THEME_DIR
cp Papirus-Light/index.theme $THEME_DIR
subst 's/Light/Education/g; s/bright themes/ALT Education/g; s/breeze/orange/g' $THEME_DIR/index.theme

# Total copy all directory from Papirus as symlinks except 'places'
for dir in Papirus/*; do
	[ -d "$dir" ] || continue
	size="${dir#*/}"
	mkdir $THEME_DIR/$size
	for d in $dir/*; do
		category="$(basename $d)"
		if [ "$category" = "places" ]; then
			# Create directory places and fill it by icon symlinks
			mkdir $THEME_DIR/$size/places
			for i in Papirus/$size/places/*.svg; do
				if [ -L "$i" ]; then
					# Copy symlinks because its source shoud be local, not base theme (ex. inode-directory.svg)
					cp -P $i $THEME_DIR/$size/places
				else
					# Symlink to icon in base theme
					ln -s ../../../$i $THEME_DIR/$size/places
				fi
			done
			pushd $THEME_DIR/$size/places
			# Replaced standard icons by colored variant
			for prefix in folder user; do
				for icon in ${prefix}-${color}*.svg; do
					symlink="${icon/$prefix-$color/$prefix}"
					[ -e "$symlink" ] || continue
					rm -f "$symlink"
					ln -s "$icon" "$symlink"
				done
			done
			popd
		else
			# Make symlink to category directory
			ln -s ../../Papirus/$size/$category $THEME_DIR/$size
		fi
	done
done

rm -rf $THEME_DIR/24x24/panel
ln -s ../../Papirus-Light/24x24/panel $THEME_DIR/24x24/panel
rm -rf $THEME_DIR/22x22/panel
ln -s ../../Papirus-Light/22x22/panel $THEME_DIR/22x22/panel
rm -rf $THEME_DIR/16x16/panel
ln -s ../../Papirus-Light/16x16/panel $THEME_DIR/16x16/panel

# Make Papirus Remix themes with all colors of folder icons
%define THEMES Adwaita Black BlueGrey Breeze Brown Carmine Cyan DarkCyan DeepOrange Green Grey Indigo Magenta Nordic Orange PaleBrown PaleOrange Pink Red Teal Violet White Yaru Yellow
%define PTHEME Blue

Pcolor=%PTHEME
Pcolor=${Pcolor,,}
Papirus=Papirus-%PTHEME

# Make Papirus Remix primary theme
cp -a Papirus $Papirus
subst "s/Papirus/$Papirus/g" $Papirus/index.theme

# Make Papirus-<Color> themes indexes from Papirus Remix primary theme
for theme in %THEMES; do
	THEME_DIR=Papirus-$theme
	mkdir $THEME_DIR
	cp $Papirus/index.theme $THEME_DIR
	subst "s/$Papirus/$THEME_DIR/g" $THEME_DIR/index.theme
done

# Edit Papirus Remix primary theme and make Papirus-<Color> themes
for dir in $Papirus/*; do
	[ -d "$dir" ] || continue
	size="${dir#*/}"
	if [ -L "$dir" ]; then
		for t in %THEMES; do
			cp -P $dir Papirus-$t
		done
	else
	if [ "$size" = "symbolic" ] || [ "$size" = "16x16" ]; then
		for t in %THEMES; do
			ln -s ../$Papirus/$size Papirus-$t
		done
	else
	for t in %THEMES; do
		mkdir Papirus-$t/$size
	done
	for d in $dir/*; do
		if [ -L "$d" ]; then
			for t in %THEMES; do
				cp -P $d Papirus-$t/$size
			done
		else
		category="$(basename $d)"
		if [ "$category" = "places" ]; then
			pushd $d
			[ -f "folder-red.svg" ] && [ -L "folder-root.svg" ] && \
			rm -f "folder-root.svg" && cp "folder-red.svg" "folder-root.svg"
			for i in *-$Pcolor*.svg; do
				[ -L "$i" ] && rm -f $i
				[ -f "$i" ] && [ -L "${i/-$Pcolor/}" ] && \
				rm -f "${i/-$Pcolor/}" && mv -f "$i" "${i/-$Pcolor/}"
			done
			files=`ls *.svg`
			for t in %THEMES; do
				f=`ls *-${t,,}*.svg`
				for i in $f; do
					files="${files/$i/}"
				done
			done
			for t in %THEMES; do
				mkdir ../../../Papirus-$t/$size/places
				for i in $files; do
					if [ -L "$i" ]; then
						cp -P $i ../../../Papirus-$t/$size/places
					else
						ln -s ../../../$d/$i ../../../Papirus-$t/$size/places
					fi
				done
				color="${t,,}"
				for i in *-$color*.svg; do
					[ -L "$i" ] && rm -f $i
					[ -f "$i" ] && mv -f $i ../../../Papirus-$t/$size/places/${i/-$color/}
				done
			done
			popd
		else
			for t in %THEMES; do
				ln -s ../../$Papirus/$size/$category Papirus-$t/$size
			done
		fi
		fi
	done
	fi
	fi
done

# Make Papirus-Dark-<Color> and Papirus-Light-<Color> themes with other colors of folder icons
for style in Dark Light; do
	for theme in %PTHEME %THEMES; do
		THEME_DIR=Papirus-$style-$theme
		mkdir $THEME_DIR
		cp Papirus-$style/index.theme $THEME_DIR
		subst "s/Name=Papirus-$style/Name=$THEME_DIR/g; \
		s/Comment=Papirus/Comment=Papirus-$theme/g" $THEME_DIR/index.theme

		for dir in Papirus-$style/*; do
			[ -d "$dir" ] || continue
			size="${dir#*/}"
			if [ -L "$dir" ]; then
				if [ "${size: -3:3}" = "@2x" ]; then
					cp -P $dir $THEME_DIR
				else
					ln -s ../Papirus-$theme/$size $THEME_DIR
				fi
			else
				mkdir $THEME_DIR/$size
				for d in $dir/*; do
					category="$(basename $d)"
					if [ -L "$d" ]; then
						if [ "$category" = "categories" ]; then
							cp -P $d $THEME_DIR/$size
						else
							ln -s ../../Papirus-$theme/$size/$category $THEME_DIR/$size
						fi
					else
					if [ "$theme" = "%PTHEME" ]; then
						cp -a $d $THEME_DIR/$size
					else
						ln -s ../../Papirus-$style-%PTHEME/$size/$category $THEME_DIR/$size
					fi
					fi
				done
			fi
		done
	done
done

%install
mkdir -p %buildroot%_iconsdir
cp -a Papirus* ePapirus* %buildroot%_iconsdir

%files
%doc AUTHORS LICENSE README.md

%files -n icon-theme-Papirus
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus

%files -n icon-theme-Papirus-Dark
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Dark

%files -n icon-theme-Papirus-Education
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Edu

%files -n icon-theme-Papirus-Light
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Light

%files -n icon-theme-ePapirus
%doc AUTHORS LICENSE README.md
%_iconsdir/ePapirus

%files -n icon-theme-ePapirus-Dark
%doc AUTHORS LICENSE README.md
%_iconsdir/ePapirus-Dark

%files -n papirus-remix-icon-theme
%doc AUTHORS LICENSE README.md

%files -n icon-theme-Papirus-Remix
%doc AUTHORS LICENSE README.md
%{expand:%(\
    for theme in %{PTHEME} %{THEMES}; do \
	echo -e "%%_iconsdir/Papirus-$theme";\
    done\
)}

%files -n icon-theme-Papirus-Dark-Remix
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Dark-*

%files -n icon-theme-Papirus-Light-Remix
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Light-*

%changelog
* Thu Nov 16 2023 Kirill Izmestev <felixz@altlinux.org> 20231101-alt2
- Add ePapirus-Dark theme
- Add Papirus Remix theme with all colors of folders. (ALT #47651)

* Fri Nov 03 2023 Kirill Izmestev <felixz@altlinux.org> 20231101-alt1
- New version.

* Wed Oct 25 2023 Kirill Izmestev <felixz@altlinux.org> 20230901-alt2
- Added a symlink to papirus-light/panel in the Papirus-Education theme (ALT #48153, #48156).

* Mon Sep 04 2023 Kirill Izmestev <felixz@altlinux.org> 20230901-alt1
- New version.

* Wed Aug 02 2023 Kirill Izmestev <felixz@altlinux.org> 20230801-alt1
- New version.

* Thu Jun 01 2023 Kirill Izmestev <felixz@altlinux.org> 20230601-alt1
- New version.

* Wed Jan 04 2023 Kirill Izmestev <felixz@altlinux.org> 20230104-alt1
- New version.

* Fri Dec 02 2022 Kirill Izmestev <felixz@altlinux.org> 20221201-alt1
- New version.

* Wed Nov 02 2022 Andrey Cherepanov <cas@altlinux.org> 20221101-alt1
- New version.

* Tue Sep 13 2022 Andrey Cherepanov <cas@altlinux.org> 20220910-alt1
- New version.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 20220808-alt1
- New version.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 20220508-alt3
- Fixed icon color Papirus-Education changing independently of other themes, no dependency on papirus-folders corrected (closes: 42867) (thanks felixz@)
- Package Papiris-Education theme to Papirus-Edu directory.

* Wed May 11 2022 Kirill Izmestev <felixz@altlinux.org> 20220508-alt2
- Add new Papirus icon theme: Papirus-Education
(based on Papirus-Light, but with orange folders).

* Mon May 09 2022 Andrey Cherepanov <cas@altlinux.org> 20220508-alt1
- New version.

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 20220302-alt1
- New version.

* Sat Feb 05 2022 Andrey Cherepanov <cas@altlinux.org> 20220204-alt1
- New version.

* Sun Jan 02 2022 Andrey Cherepanov <cas@altlinux.org> 20220101-alt1
- New version.

* Thu Dec 02 2021 Andrey Cherepanov <cas@altlinux.org> 20211201-alt1
- New version.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 20211101-alt1
- New version.

* Sat Oct 02 2021 Andrey Cherepanov <cas@altlinux.org> 20211001-alt1
- New version.

* Fri Sep 03 2021 Andrey Cherepanov <cas@altlinux.org> 20210901-alt1
- New version.

* Mon Aug 02 2021 Andrey Cherepanov <cas@altlinux.org> 20210802-alt1
- New version.

* Fri Jul 02 2021 Andrey Cherepanov <cas@altlinux.org> 20210701-alt1
- New version.

* Wed Jun 02 2021 Andrey Cherepanov <cas@altlinux.org> 20210601-alt1
- New version.

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 20210501-alt1
- New version.

* Fri Apr 02 2021 Andrey Cherepanov <cas@altlinux.org> 20210401-alt1
- New version.

* Wed Mar 03 2021 Andrey Cherepanov <cas@altlinux.org> 20210302-alt1
- New version.

* Tue Feb 02 2021 Andrey Cherepanov <cas@altlinux.org> 20210201-alt1
- New version.

* Fri Jan 01 2021 Andrey Cherepanov <cas@altlinux.org> 20210101-alt1
- New version.

* Wed Dec 02 2020 Andrey Cherepanov <cas@altlinux.org> 20201201-alt1
- New version.

* Mon Nov 02 2020 Andrey Cherepanov <cas@altlinux.org> 20201031-alt1
- New version.

* Fri Oct 02 2020 Andrey Cherepanov <cas@altlinux.org> 20201001-alt1
- New version.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 20200901-alt1
- New version.

* Mon Aug 03 2020 Andrey Cherepanov <cas@altlinux.org> 20200801-alt1
- New version.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 20200702-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 20200602-alt1
- New version.

* Fri May 01 2020 Andrey Cherepanov <cas@altlinux.org> 20200430-alt1
- New version.

* Mon Apr 06 2020 Andrey Cherepanov <cas@altlinux.org> 20200405-alt1
- New version.

* Mon Mar 02 2020 Andrey Cherepanov <cas@altlinux.org> 20200301-alt1
- New version.

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 20200201-alt1
- New version.

* Thu Jan 02 2020 Andrey Cherepanov <cas@altlinux.org> 20200102-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 20191201-alt1
- New version.

* Fri Nov 01 2019 Andrey Cherepanov <cas@altlinux.org> 20191101-alt1
- New version.

* Wed Oct 09 2019 Andrey Cherepanov <cas@altlinux.org> 20191009-alt1
- New version.

* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 20190919-alt1
- New version.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 20190817-alt1
- New version.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 20190802-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 20190720-alt1
- New version.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 20190708-alt1
- New version.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190701-alt1
- New version.

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 20190615-alt1
- New version.

* Tue May 28 2019 Andrey Cherepanov <cas@altlinux.org> 20190521-alt2
- Make network menu item in ALT looks like upstream Internet menu item.

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 20190521-alt1
- New version.
- Make trash icon grayed.

* Thu May 02 2019 Andrey Cherepanov <cas@altlinux.org> 20190501-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190331-alt1
- New version.
- Requires icon-theme-Papirus to derivative themes for correct upgrade (ALT #36318). 

* Wed Mar 06 2019 Andrey Cherepanov <cas@altlinux.org> 20190302-alt1
- New version.

* Mon Feb 04 2019 Andrey Cherepanov <cas@altlinux.org> 20190203-alt1
- New version.

* Sun Jan 06 2019 Andrey Cherepanov <cas@altlinux.org> 20190106-alt1
- New version.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 20181120-alt1
- New version.
- Remove Papirus-Adapta{,-Nokto} icon themes.

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 20181007-alt1
- New version.

* Fri Aug 17 2018 Andrey Cherepanov <cas@altlinux.org> 20180816-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 20180720-alt1
- New version.

* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 20180601-alt1
- Initial build for Sisyphus
