%define uuid weather@mockturtl

Summary: Weather applet for Cinnamon  
Name: cinnamon-weather
Version: 1.7.1
Release: alt2
License: GPLv3+
Group: Graphical desktop/GNOME
BuildArch: noarch
URL: http://cinnamon-spices.linuxmint.com/applets/view/17
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

Patch1: cinnamon-weather-1.7.1-alt-locale-dir.patch

Requires: cinnamon

BuildRequires: gettext

%description
A Cinnamon applet based on the Gnome Shell weather extension.

%install
install -m755 -pd %buildroot
tar xf %SOURCE0 --strip-components 1 -C %buildroot
pushd %buildroot/
patch -p2 <%PATCH1
%define bin_dir %buildroot/usr/bin
install -m755 -pd %bin_dir
cp cinnamon-weather-settings %bin_dir
%define install_dir %buildroot/usr/share/cinnamon/applets/%uuid
install -m755 -pd %install_dir
EXCLUDES='.md|.sh|.xml|po/'
COMMENTS='/^\s*#/'
cat manifest | sed -r ${COMMENTS}d | sed -r '\ .*('${EXCLUDES}')$ d' | xargs -i mv -f '{}' %install_dir
%define doc_dir %buildroot/usr/share/doc/cinnamon-weather/
install -m755 -pd %doc_dir
mv README.md %doc_dir

%define locale_dir %buildroot/usr/share/locale
LOCALES="$(cat po/LINGUAS)"
rm -f po/LINGUAS
for LOCALE in ${LOCALES}; do
    mkdir -p %locale_dir/${LOCALE}/LC_MESSAGES
    msgfmt -c po/${LOCALE}.po -o %locale_dir/${LOCALE}/LC_MESSAGES/%{uuid}.mo
    rm -f po/${LOCALE}.po
done
rm -f cleanup.sh
rm -f install.sh
rm -f uninstall.sh

%define schema_dir %buildroot/usr/share/glib-2.0/schemas/
install -m755 -pd %schema_dir
mv org.cinnamon.applets.%{uuid}.gschema.xml %schema_dir
rm -f po/%{uuid}.pot

popd


%find_lang %uuid

%files -f %uuid.lang
%_bindir/cinnamon-weather-settings
%_docdir/%name
%_datadir/cinnamon/applets/%uuid
%_datadir/glib-2.0/schemas/*.xml

%changelog
* Wed Dec 26 2012 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt2
- Fixed locale dir location

* Wed Dec 26 2012 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- Initial build

