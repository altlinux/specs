Name: deepin-gettext-tools
Version: 1.0.11
Release: alt2

Summary: Deepin Gettext Tools

License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-gettext-tools

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildArch: noarch

BuildRequires: python3-devel perl-Config-Tiny perl-Exporter-Tiny perl-XML-LibXML perl-XML-LibXML-PrettyPrint

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
sed -i '1s|env perl|perl|' src/desktop_ts_convert.pl
# fix syntax
sed -i '/source_dirs/s|re.split(|re.split(r|' src/update_pot.py

sed -i 's|sudo cp|cp|g' src/generate_mo.py

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
* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt2
- Removed obsoleted requires.
- Fixed python3 syntax.

* Wed Apr 03 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- New version.

* Wed Jun 22 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- Fixed version.

* Sat Mar 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt2.gitc913e2d
- Built from commit c913e2d7f9ea6ee394e3640dfca807d802806607.
- Update license tag.

* Wed Mar 04 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
