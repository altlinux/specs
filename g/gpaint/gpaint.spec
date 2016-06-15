Name: 	 gpaint
Version: 0.3.3
Release: alt2
Summary: GPaint Easy to use paint program for GNOME
Summary(ru_RU.UTF-8): Простая рисовалка на GTK


Group: Graphics
License: GPLv3
Url: http://www.gnu.org/software/gpaint/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.xpm
Source2: %name.svg
Source3: %name.1

Patch1:  01_drawing.diff
Patch2:  02_remove_menu_h_reference.diff
Patch3:  09_fix_menu_entry.diff
Patch4:  10_fix_crash_on_font_select.diff
Patch5:  11_fix_image_rotation.diff
Patch6:  20_fix_line_width_combo.diff
Patch7:  21_fix_crash_on_fill_button_click.diff
Patch8:  22_fix_not_printable_string.diff
Patch9:  23_add_accelerator_keys.diff
Patch10: 24_fix_crash_on_failed_write.diff
Patch11: 25_fix_color_selection.diff
Patch12: 26_fix_toolbar.diff
Patch13: 27_fix_missing_hdrs_libs.diff

BuildRequires: intltool gtk2-devel
BuildRequires: libglade-devel

%description
gpaint is a simple, easy to use paint program for GNOME.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

touch src/menu.h
subst "s,Icon=/usr/share/pixmaps/Clipboard.xpm,Icon=gpaint," %name.desktop

%build
%configure
%make_build

%install
%makeinstall_std
install -Dp -m0644 %name.desktop  %buildroot%_desktopdir/%name.desktop
install -Dp -m0644 %SOURCE1 %buildroot%_pixmapsdir/%name.xpm
install -Dp -m0644 %SOURCE2 %buildroot%_iconsdir/hicolor/scalable/%name.svg
install -Dp -m0644 %SOURCE3 %buildroot%_man1dir/%name.1

%find_lang %{name}-2 --output=%name.lang

%files -f %name.lang
%_bindir/gpaint-2
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.xpm
%_iconsdir/hicolor/scalable/%name.svg
%_man1dir/%name.1*

%changelog
* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt2
- Fix l10n detection

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version
- Apply patches from Debian
- Add SVG icon
- Add man page

* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Fix build in Sisyphus (missing libm in linked libs)

* Tue Aug 16 2011 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build in Sisyphus (thanks YYY) (closes: #26089)

