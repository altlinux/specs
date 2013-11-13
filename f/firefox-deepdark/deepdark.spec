BuildRequires(pre): rpm-build-firefox

%define rname	deepdark
%define cid	\{77d2ed30-4cd2-11e0-b8af-0800200c9a66\}
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	9.2.2
Release:	alt1
Summary:	Dark theme for Firefox

License:	Free
Group:		Networking/WWW
URL:		https://addons.mozilla.org/RU/firefox/addon/ft-deepdark/

Source0:	%rname-%version.tar

BuildArch:	noarch

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description 
Bloomind FT DeepDark, dark theme for Firefox.

%prep
%setup

%install
install -d %buildroot/%ciddir
cp -fR * %buildroot/%ciddir

%files
%ciddir

%changelog
* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.2.2-alt1
- Version 9.2.2

* Sat Aug 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3.1-alt1
- Version 7.3.1

* Mon Dec 17 2012 Andrey Cherepanov <cas@altlinux.org> 5.4-alt1
- New version 5.4

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 2.4.4.1-alt2
- Rebuilt with firefox-9.0.1

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4.1-alt1
- Version 2.4.4.1

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 2.3.3-alt1
- Version 2.3.3

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1
- Version 1.3.7

* Mon Jan 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4.5-alt1
- Initial build for Sisyphus

