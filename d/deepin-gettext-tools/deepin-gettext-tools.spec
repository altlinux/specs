Name: deepin-gettext-tools
Version: 1.0.8
Release: alt2.gitc913e2d
Summary: Deepin Gettext Tools
License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-gettext-tools
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildArch: noarch
BuildRequires: python3-devel perl-Config-Tiny perl-Exporter-Tiny perl-XML-LibXML perl-XML-LibXML-PrettyPrint
Requires: gettext-tools qt5-linguist perl-Config-Tiny perl-Exporter-Tiny perl-XML-LibXML perl-XML-LibXML-PrettyPrint

%description
The tools of gettext function wrapper.

desktop-ts-convert - handling desktop file translations.
policy-ts-convert - convert PolicyKit Policy file to the ts file.
update-pot - scan msgid and generate pot file according to the ini file.
generate-mo - scan po files and generate mo files according to the ini file.

%prep
%setup

# fix shebang
find -iname "*.py" | xargs sed -i '1s|.*|#!%__python3|'
%__subst '1s|.*|#!%__perl|' src/desktop_ts_convert.pl

%__subst 's|sudo cp|cp|' src/generate_mo.py
%__subst 's|lconvert|lconvert-qt5|; s|deepin-lupdate|lupdate-qt5|' src/update_pot.py

%build
%install
install -d %buildroot%_bindir
install -m755 src/desktop_ts_convert.pl %buildroot%_bindir/deepin-desktop-ts-convert
install -m755 src/policy_ts_convert.py %buildroot%_bindir/deepin-policy-ts-convert
install -m755 src/generate_mo.py %buildroot%_bindir/deepin-generate-mo
install -m755 src/update_pot.py %buildroot%_bindir/deepin-update-pot

%check
%_bindir/perl src/desktop_ts_convert.pl --help
%_bindir/python3 src/generate_mo.py --help
%_bindir/python3 src/update_pot.py --help

%files
%doc README.md
%doc LICENSE
%_bindir/deepin-desktop-ts-convert
%_bindir/deepin-policy-ts-convert
%_bindir/deepin-update-pot
%_bindir/deepin-generate-mo

%changelog
* Sat Mar 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt2.gitc913e2d
- Built from commit c913e2d7f9ea6ee394e3640dfca807d802806607.
- Update license tag.

* Wed Mar 04 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
