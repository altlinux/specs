Name: zorin-icon-themes
Version: 2.9.12
Release: alt1
Summary: Zorin icon themes

License: CC-BY-SA-4.0
Group: Graphical desktop/GNOME
URL: https://github.com/ZorinOS/zorin-icon-themes

Source: %name-%version.tar

BuildArch: noarch
AutoReqProv: no

%description
The Zorin icon theme provided in a variety of color combinations.

%define themes Zorin ZorinBlue-Dark ZorinBlue-Light ZorinGreen-Dark ZorinGreen-Light ZorinGrey-Dark ZorinGrey-Light ZorinOrange-Dark ZorinOrange-Light ZorinPurple-Dark ZorinPurple-Light ZorinRed-Dark ZorinRed-Light

%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n icon-theme-$theme";\
        echo -e "Summary: $theme icon theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n icon-theme-$theme\n$theme icon theme.\n";\
        echo -e "%%files -n icon-theme-$theme\n%%_iconsdir/$theme/\n";\
    done\
)}

%prep
%setup
# Remove bad symlinks
find . -name mintwelcome.png -delete

%install
mkdir -p %buildroot%_iconsdir
cp -a Zorin* %buildroot%_iconsdir

%changelog
* Mon Feb 13 2023 Kirill Izmestev <felixz@altlinux.org> 2.9.12-alt1
- New version.

* Thu Jan 12 2023 Kirill Izmestev <felixz@altlinux.org> 2.9.11-alt1
- New version.

* Tue Sep 06 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.10-alt1
- New version.

* Wed Aug 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.9-alt1
- New version.

* Sun Jul 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.8-alt1
- New version.

* Thu Feb 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.7-alt1
- New version.

* Tue Jan 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.5-alt1
- New version.

* Mon Nov 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.9.4-alt1
- New version.

* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.9.3-alt1
- New version.

* Fri Nov 05 2021 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1
- New version.

* Mon Oct 11 2021 Andrey Cherepanov <cas@altlinux.org> 2.9-alt1
- New version.

* Fri Aug 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.11-alt1
- New version.

* Sat Aug 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.10-alt1
- New version.

* Wed Jul 28 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.8-alt1
- New version.

* Sat Jul 24 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.7-alt1
- New version.

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.5-alt1
- New version.

* Sat Jun 19 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1
- New version.

* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.3-alt1
- New version.

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version.

* Thu Apr 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version.

* Sun Apr 18 2021 Andrey Cherepanov <cas@altlinux.org> 2.7.9-alt1
- New version.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 2.4.5-alt1
- New version.

* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.10-alt1
- Initial build in Sisyphus.
