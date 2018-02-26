%define rname	ru
%define cid	langpack-ru@sunbird.mozilla.org
%define ciddir 	%sunbird_noarch_extensionsdir/%cid

Name:		%sunbird_name-%rname
Version:	0.9.0
Release:	alt2
Summary:	Russian (RU) Language Pack for Sunbird

License:	GPL
Group:		Office
URL:		http://www.mozilla-russia.org/projects/calendar/sunbird/
BuildArch:	noarch

Source0:	ru-%version.xpi

BuildRequires(pre):	rpm-build-sunbird
BuildRequires:		unzip

Requires:	hunspell-ru

%description
The Mozilla Sunbird in Russian.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..
%__mkdir_p %buildroot/%ciddir/dictionaries

%__cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%ciddir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%ciddir/dictionaries/ru.dic

sed -r -i \
    -e 's,<em:maxVersion>0.9</em:maxVersion>,<em:maxVersion>0.9*</em:maxVersion>,g' \
    -e 's,<em:minVersion>3.0</em:minVersion>,<em:minVersion>3.0</em:minVersion>,g' \
    %buildroot/%ciddir/install.rdf

%files
%ciddir

%changelog
* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt2
- Change arch.

* Fri Sep 12 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt1
- New version.

* Tue Nov 13 2007 Alexey Gladkov <legion@altlinux.ru> 0.7.0-alt2
- First build for ALT Linux.
