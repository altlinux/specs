%define cid	langpack-kk@firefox.mozilla.org
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		firefox-kk
Version:	19.0.2
Release:	alt1
Summary:	Kazakh (KZ) Language Pack for Firefox

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla-russia.org/products/firefox/
Packager:	Alexey Gladkov <legion@altlinux.ru>
BuildArch:	noarch

Source0:	kk-%version.xpi

Requires:	firefox >= %version
Requires:	hunspell-kk

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

%description
The Mozilla Firefox Kazakh translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

%__mkdir_p %buildroot/%ciddir/dictionaries

%__cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/kk_KZ.aff %buildroot/%ciddir/dictionaries/kk.aff
ln -s %_datadir/myspell/kk_KZ.dic %buildroot/%ciddir/dictionaries/kk.dic

#sed -r -i \
#    -e 's,<em:maxVersion>4.0</em:maxVersion>,<em:maxVersion>4.*</em:maxVersion>,g' \
#    -e 's,<em:minVersion>4.0</em:minVersion>,<em:minVersion>4.0</em:minVersion>,g' \
#    %buildroot/%ciddir/install.rdf

%files
%ciddir

%changelog
* Mon Mar 11 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New version (19.0.2)
- First build for ALT Linux.
