Name:           translate-shell
Version:        0.9.6.11
Release:        alt1
Summary:        A command-line online translator

License:        Public Domain
Group:          System/Internationalization
URL:            https://github.com/soimort/translate-shell
Source0:        %name-%version.tar

Patch0:         translate-shell-no-builtin-man.patch

Requires:       gawk
Requires:       curl
Requires:       rlwrap
Requires:       fribidi

BuildArch:      noarch

%description
Translate Shell (formerly Google Translate CLI) is a command-line
translator powered by Google Translate (default), Bing Translator,
Yandex.Translate and Apertium.

%prep
%setup -q
%patch0 -p1

#https://github.com/soimort/translate-shell/issues/180
sed -i 's|install: build|install:|' Makefile

%build
%make_build
sed -i 's|/usr/bin/env bash|/bin/bash|' build/trans

%install
%make_install install \
	DESTDIR=%buildroot \
	PREFIX=%_prefix

%files
%doc LICENSE
%_bindir/trans
%_man1dir/trans.1*

%changelog
* Thu Jan 16 2020 Alexey Gladkov <legion@altlinux.ru> 0.9.6.11-alt1
- New version (0.9.6.11).

* Thu Jun 27 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.6.10-alt1
- First build for ALT Linux.

* Tue Apr 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.10-1
- Update to 0.9.6.10

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.9-1
- Update to 0.9.6.9

* Tue Aug 14 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.8-1
- Update to 0.9.6.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.7-1
- Update to 0.9.6.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.6-1
- Update to 0.9.6.6

* Mon Oct 16 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.5-1
- Update to 0.9.6.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-3
- Clean spec to pass review

* Fri Jun 02 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-2
- Clean spec

* Thu Jun 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-1
- Update to 0.9.6.4

* Wed May 31 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.3-1
- Initial packaging
