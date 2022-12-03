Name:     papirus-icon-theme
Version:  20221201
Release:  alt1

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

%description
Papirus is a free and open source SVG icon theme for Linux, based on
Paper Icon Set with a lot of new icons and a few extras, like
Hardcode-Tray support, KDE colorscheme support, Folder Color support,
and others.

Papirus icon theme is available in five variants:

* Papirus
* Papirus Dark
* Papirus Education
* Papirus Light
* ePapirus (for elementary OS and Pantheon Desktop)

%package -n icon-theme-Papirus
Summary: Papirus icon theme
Group: Other

%description -n icon-theme-Papirus
%summary.

%package -n icon-theme-Papirus-Dark
Summary: Papirus-Dark icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-Papirus-Dark
%summary.

%package -n icon-theme-Papirus-Education
Summary: Papirus-Education icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-Papirus-Education
%summary.

%package -n icon-theme-Papirus-Light
Summary: Papirus-Light icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-Papirus-Light
%summary.

%package -n icon-theme-ePapirus
Summary: ePapirus icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-ePapirus
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

%install
mkdir -p %buildroot%_iconsdir
cp -a Papirus Papirus-Dark Papirus-Edu Papirus-Light ePapirus %buildroot%_iconsdir

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

%changelog
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
