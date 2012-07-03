%define cid	langpack-ru@seamonkey.mozilla.org
%define ciddir	%seamonkey_prefix/extensions/%cid

Name:		seamonkey-ru
Version:	2.8
Release:	alt1
Summary:	Russian (RU) Language Pack for Seamonkey

License:	MPL/NPL
Group:		Networking/WWW
URL:		http://mozilla-russia.org/products/seamonkey/
Packager:	Radik Usupov <radik@altlinux.org>

Source0:	ru-%version.xpi

Requires:	hunspell-ru
Requires:	seamonkey

BuildRequires(pre):	rpm-build-seamonkey
BuildRequires:		unzip

%description
The Mozilla Seamonkey Russian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

%__mkdir_p %buildroot/%ciddir/dictionaries

%__cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%ciddir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%ciddir/dictionaries/ru.dic

%files
%dir %seamonkey_prefix
%dir %seamonkey_prefix/extensions
%ciddir

%changelog
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
