Name: normcap
Version: 0.6.0
Release: alt6

Summary: OCR powered screen-capture tool to capture information instead of images

License: GPLv3
Group: Other
URL: https://github.com/dynobo/normcap
VCS: https://github.com/dynobo/normcap

BuildArch: noarch

Source: %name-%version.tar
# https://bugzilla.altlinux.org/57353
Source1: com.github.dynobo.normcap.desktop
Source2: normcap.desktop
Source3: normcap
Source4: normcap2

Requires: tesseract xsel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel
BuildRequires: gettext-tools

Patch: menu_button-0.6.0-alt-fixes.patch
Patch1: tray-0.6.0-alt-fixes.patch
#
Patch2: do_not_try_gnome-screenshot_on_Gnome49.patch

%description
%summary.

%package -n python3-module-%name
Group:   Development/Python3
Summary: OCR powered screen-capture tool to capture information instead of images
%description -n python3-module-%name
%summary.

%prep
%setup
#remove update check
%autopatch -p0

%build
%pyproject_build
for locale in ca cs de_DE es_ES fr_FR hi_IN it_IT ja_JP pl_PL pt_BR pt_PT ru_RU sv_SE ta uk_UA zh_CN; do
 msgfmt %name/resources/locales/${locale}/LC_MESSAGES/messages.po -o \
 	%name/resources/locales/${locale}/LC_MESSAGES/messages.mo
 rm -v %name/resources/locales/${locale}/LC_MESSAGES/messages.po
done

%install
%pyproject_install
rm -v %buildroot%_bindir/%name
install -Dm 0644 %SOURCE1 %buildroot%_datadir/applications/com.github.dynobo.normcap.desktop
install -Dm 0644 %SOURCE2 %buildroot%_datadir/applications/%name.desktop
install -Dm0755 %SOURCE3 %buildroot%_bindir/%name
install -Dm0755 %SOURCE4 %buildroot%_bindir/normcap2

cp -f -r %name/resources/locales %buildroot%python3_sitelibdir/%name/resources

%files 
%doc *.md
%_bindir/%name
%_bindir/normcap2
%_datadir/applications/*.desktop

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Tue Dec 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt6
- fix: launch via application shortcut with permissions in Gnome 49 (ALT #57353)

* Mon Nov 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt5
- fix: launch via application shortcut in Gnome 49
- feat(screenshot): do not try gnome-screenshot on Gnome 49+

* Thu Sep 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt4
- remove update check

* Sat Sep 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt3
- add locales

* Thu Sep 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt2
- add requires xsel

* Tue Sep 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- Release: 0.6.0.

* Mon Sep 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt0.beta2
- Initial build for ALT Linux.
