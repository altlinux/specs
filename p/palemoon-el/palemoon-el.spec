%define cid            langpack-el@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       el@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	31.2.0
%define max_version	31.3.*

%define bname		newmoon
%define sdir		searchplugins
%define newmoon_dir 	%_datadir/%bname-data/browser/
%define search_dir 	%newmoon_dir%sdir

Name: palemoon-el


Version: 31.3.0
Release: alt1.1

Summary: Greek (EL) Language Pack for Pale Moon
License: MPL-2.0

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: el_palemoon_%version.xpi
Source2: searchplugins.tar

Requires: hunspell-el
Requires: palemoon >= 27.7.0

#BuildArch: noarch
ExcludeArch: %ix86 %arm

BuildRequires(pre):	rpm-build-palemoon
# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: libdb4-devel unzip

Requires: hunspell-el

%description
The Palemoon Greek translation and dictionary

%package palemoon-searchplugins
Summary: Greek (EL) Language Pack for Pale Moon
Group:   Networking/WWW
BuildArch: noarch
Conflicts:  palemoon-el < 27.7.0

%description palemoon-searchplugins
Greek (EL) Language Pack for Pale Moon

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
#ln -s %_datadir/myspell/el_GR.aff %buildroot/%cid_dict_dir/dictionaries/el.aff
#ln -s %_datadir/myspell/el_GR.dic %buildroot/%cid_dict_dir/dictionaries/el.dic

%files
%cid_dir
%cid_dict_dir

%files palemoon-searchplugins
%search_dir

%changelog
* Sun Oct 30 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1.1
- Fix Build

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1
- initial build for ALT Linux Sisyphus
