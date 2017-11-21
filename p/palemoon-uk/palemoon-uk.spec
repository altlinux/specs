%define cid            langpack-uk@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       uk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	27.3.99
%define max_version	27.*

%define bname		newmoon
%define sdir		searchplugins
%define newmoon_dir 	%_datadir/%bname-data/browser/
%define search_dir 	%newmoon_dir%sdir

Name: palemoon-uk

#commit f353aabc21603a0a919202c32010b4b9a9c7bc9c
#Author: JustOff <Off.Just.Off@gmail.com>
#Date:   Sun Nov 5 22:51:34 2017 +0200
#
#    Locales update (27.6.0 RC3)

Version: 27.6.0
Release: alt1

Summary: Ukrainian (UA) Language Pack for Pale Moon
License: MPL/GPL/LGPL

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: uk_palemoon_%version.xpi
Source2: searchplugins.tar

Requires: palemoon >= 27.6.0
Requires: hunspell-uk
BuildArch: noarch

BuildRequires(pre):	rpm-build-palemoon
# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: libdb4-devel unzip

%description
The Palemoon Ukrainian translation and dictionary.

%package palemoon-searchplugins
Summary: The Palemoon Russian translation and dictionary.
Group:   Networking/WWW
BuildArch: noarch
Conflicts:  palemoon-uk < 27.4.0

%description palemoon-searchplugins
The set of Ukrainian search plugins for Palemoon

%prep
%setup -c -n %name-%version/%cid

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
	               em:name="Ukrainian (UA) Dictionary"
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
ln -s %_datadir/myspell/uk_UA.aff %buildroot/%cid_dict_dir/dictionaries/uk.aff
ln -s %_datadir/myspell/uk_UA.dic %buildroot/%cid_dict_dir/dictionaries/uk.dic

%files
%cid_dir
%cid_dict_dir

%files palemoon-searchplugins
%search_dir

%changelog
* Tue Nov 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.6.0-alt1
- Update for release 27.6.0-RC3

* Sun Sep 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt4
- Update Translations

* Mon Aug 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt3
- Update Translations

* Sun Aug 20 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt2
- Update Translations

* Sun Aug 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt1
- Update for release 27.5.0_RC4

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt1
- initial build for ALT Linux Sisyphus
