%define cid            langpack-ru@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	33.4.0
%define max_version	34.5.*

%define bname		newmoon
%define sdir		searchplugins
%define newmoon_dir 	%palemoon_datadir/browser/
%define search_dir 	%newmoon_dir%sdir

Name: palemoon-ru

Version: 33.4.0
Release: alt1

ExclusiveArch: x86_64 aarch64

Summary: Russian (RU) Language Pack for Pale Moon
License: MPL-2.0

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml
# BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  ru_palemoon_%version.xpi
Source2: searchplugins.tar

Patch:   %name-31.1.0-search.patch
#Patch2:	 %name-27.3.0-advanced.patch

Requires: palemoon >= 33.4.0
Requires: hunspell-ru
Requires: palemoon-searchplugins

Obsoletes: palemoon-ru_yo-dictionary palemoon-ru_ie-dictionary
Provides: palemoon-ru_yo-dictionary palemoon-ru_ie-dictionary

BuildRequires(pre):	rpm-build-palemoon 
# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: libdb4-devel unzip

%description
The Palemoon Russian translation and dictionary.

%package -n palemoon-searchplugins
Summary: The Palemoon Russian translation and dictionary.
Group:   Networking/WWW
#BuildArch: noarch

Conflicts:  palemoon-ru < 27.7.0

%description -n palemoon-searchplugins
The set of search plugins for Palemoon

%description -n palemoon-searchplugins -l ru_RU.UTF8
Набор Поисковых плагинов для Palemoon

%prep
%setup -c -n %name-%version/%cid

%patch -p2

#patch2 -p2

tar -xf %SOURCE2


%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

install -d -m 755 %buildroot/%newmoon_dir/

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir


cd -

cp -r -- %sdir  %buildroot/%search_dir/


#sed -r -i \
#    -e 's,<em:maxVersion>4.0</em:maxVersion>,<em:maxVersion>4.*</em:maxVersion>,g' \
#    -e 's,<em:minVersion>4.0</em:minVersion>,<em:minVersion>4.0</em:minVersion>,g' \
#    %buildroot/%cid_dir/install.rdf

# Install dictionary
cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
	<?xml version="1.0"?>
	<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
	  <Description about="urn:mozilla:install-manifest"
	               em:id="%cid_dict"
	               em:name="Russian (RU) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4}</em:id>
	        <em:minVersion>%min_version</em:minVersion>
	        <em:maxVersion>%max_version.*</em:maxVersion>
	      </Description>
	    </em:targetApplication>
	  </Description>
	</RDF>
EOF
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%cid_dict_dir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%cid_dict_dir/dictionaries/ru.dic


%files
%cid_dir
%cid_dict_dir

%files -n palemoon-searchplugins
%search_dir

%changelog
* Sat Oct 12 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.4.0-alt1
- Version 33.4.0

* Thu Aug 15 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.3.0-alt1
- Version 33.3.0

* Thu Jul 18 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.2.0-alt1
- Version 33.2.0

* Mon May 06 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.1.0-alt1
- Version 33.1.0

* Sun Feb 04 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.0.0-alt1
- Version 33.0.0

* Sun Nov 19 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.5.0-alt1
- Version 32.5.0

* Wed Sep 20 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.4.0-alt2
- Version 32.4.0

* Fri Sep 15 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.0.0-alt1.1
- Add ExcludeArch ppc64le arch

* Tue Jan 31 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.0.0-alt1
- Version 32.0.0

* Mon Nov 28 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.4.0-alt1
- Version 31.4.0

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1
- Uppdate to release 31.3.0

* Fri Aug 12 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.2.0-alt1
- Uppdate to release 31.1.0

* Thu Jul 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.1.0-alt2
- Specifying the license version

* Tue Jul 19 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.1.0-alt1
- Uppdate to release 31.1.0

* Sun Apr 15 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.9.0-alt1
- Update for release 27.7.9-RC3

* Mon Mar 12 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.8.0-alt1
- Update from https://github.com/JustOff/pale-moon-localization.git
  commit db3903541364659a9299cae4016a1210b5f5fbd2

* Wed Jan 17 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.7.0-alt1
- Update for release 27.7.0-RC6

* Tue Nov 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.6.0-alt1
- Update for release 27.6.0-RC3

* Tue Sep 26 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt6
- Update from https://github.com/JustOff/pale-moon-localization.git
    commit 254c3de4aab82f14bef063a1c3a633e1f1fa5258
    Author: wolfbeast <mcwerewolf@gmail.com>

* Sun Sep 24 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt5
- Fix tranlation

* Mon Sep 04 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt4.1
- Fix trasnlations

* Sun Sep 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt4
- Update trasnlations

* Sun Sep 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt3
- Update browser.propertios

* Sun Aug 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt2
- Update for release 27.5.0_RC4

* Sat Jul 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt1
- Update for release 27.5-RC2

* Tue Jul 11 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.4.0-alt3
- Update for release 27.4

* Sat Jun 17 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.4.0-alt2
- Version 27.4.0-RC5

* Sun May 07 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.4.0-alt1
- Version 27.4.0-RC1

* Sun Apr 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.3.0-alt1
- Version 27.3.0-RC1

* Thu Apr 13 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.2.0-alt3
- Add search plugins alt-linux-wiki-ru and  search_altlinux

* Mon Apr 10 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.2.0-alt2
- Add the set of search plugins for Palemoon

* Sat Mar 18 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.2.0-alt1
- Version 27.2.0-RC1

* Fri Feb 24 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt2.RC1
- Fix searchplugins

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt1.RC1
- Add Russian searchplugins

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt0.RC1
- Version 27.1.1-RC1

* Mon Feb 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.0-alt0.RC1
- Version 27.1.0-RC1

* Sat Jan 14 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.3-alt2
- Update from https://github.com/JustOff/pale-moon-localization.git

* Fri Dec 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.3-alt1
- Version 27.0.3 (ALT #32932)

* Thu Dec 01 2016 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.0-alt1
- Version 27.0.0

* Thu Feb 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0.1-alt5
- Fix Translate

* Fri Feb 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0.1-alt4.1
- Fix Version

* Wed Jan 27 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt4
- Fix install.rdf

* Sun Jan 24 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt3
- Add translats

* Fri Jan 15 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt2
- Add translats

* Sun Jan 10 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt1
- New Version

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6-alt1
- New Version

* Tue Sep 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt2
- Fix search

* Thu Jul 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt1
- initial build for ALT Linux Sisyphus



