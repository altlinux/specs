%define cid	langpack-ru@seamonkey.mozilla.org
%define ciddir	%sm_prefix/extensions/%cid

Name:		seamonkey-ru
Version:	2.23
Release:	alt1
Summary:	Russian (RU) Language Pack for Seamonkey

License:	MPL/NPL
Group:		Networking/WWW
URL:		http://mozilla-russia.org/products/seamonkey/
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	ru-%version.xpi

Requires:	hunspell-ru
Requires:	seamonkey >= %version

BuildRequires(pre):	rpm-build-seamonkey
BuildRequires:		unzip

%description
The Mozilla Seamonkey Russian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

mkdir -p %buildroot/%ciddir/dictionaries

cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%ciddir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%ciddir/dictionaries/ru.dic

%files
%dir %sm_prefix
%dir %sm_prefix/extensions
%ciddir

%changelog
* Tue Feb 18 2014 Andrey Cherepanov <cas@altlinux.org> 2.23-alt1
- New version

* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 2.21-alt1
- Localization for version 2.21 of Seamonkey

* Thu Aug 08 2013 Andrey Cherepanov <cas@altlinux.org> 2.20-alt1
- Localization for version 2.20 of Seamonkey

* Thu Jul 11 2013 Andrey Cherepanov <cas@altlinux.org> 2.19-alt1
- Localization for new version 2.19 of Seamonkey

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 2.17.1-alt1
- Localization for new version 2.17.1 of Seamonkey

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.15.2-alt1
- Localization for new version 2.15.2 of Seamonkey

* Thu Feb 28 2013 Andrey Cherepanov <cas@altlinux.org> 2.15.2-alt0.M60P.1
- New version 2.15.2

* Tue Nov 13 2012 Radik Usupov <radik@altlinux.org> 2.13.2-alt0.M60P.1
- Backport to p6

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 2.13.2-alt1
- New version (2.13.2)

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 2.8-alt1
- New version (2.8b3)

* Thu Feb 09 2012 Radik Usupov <radik@altlinux.org> 2.7-alt1
- New version (2.7)

* Thu Nov 24 2011 Radik Usupov <radik@altlinux.org> 2.5-alt1
- New version (2.5)

* Sun Oct 02 2011 Radik Usupov <radik@altlinux.org> 2.4.1-alt1
- New version (2.4.1)

* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 2.3.3-alt1
- New version (2.3.3)

* Fri Sep 02 2011 Radik Usupov <radik@altlinux.org> 2.3.2-alt1
- Rebuild from new version sm

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 2.3.1-alt1
- New version (2.3.1)

* Wed Aug 17 2011 Radik Usupov <radik@altlinux.org> 2.3-alt1
- New version (2.3)

* Wed Aug 03 2011 Radik Usupov <radik@altlinux.org> 2.2-alt1
- New version (2.2)

* Tue May 10 2011 Radik Usupov <radik@altlinux.org> 2.0.14-alt1
- New version (2.0.14)
- New packager

* Thu Jan 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.1-alt1
- Updated translation to 1.1
