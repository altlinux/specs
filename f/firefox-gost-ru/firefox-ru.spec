%define cid            langpack-ru@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-gost-ru
Version:	38.7.0
Release:	alt1
Summary:	Russian (RU) Language Pack for Firefox GOST

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla-russia.org/products/firefox/
Packager:	Andrey Cherepanov <cas@altlinux.org>
BuildArch:	noarch

Source0:	ru-%version.xpi

Requires:	firefox-gost >= %version
Requires:	hunspell-ru
Obsoletes:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary
Provides:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

Conflicts:	firefox-ru
Conflicts:	firefox-esr-ru

%description
The Mozilla Firefox Russian translation and dictionary.

%prep
%setup -c -n firefox-ru-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

#sed -r -i \
#    -e 's,<em:maxVersion>4.0</em:maxVersion>,<em:maxVersion>4.*</em:maxVersion>,g' \
#    -e 's,<em:minVersion>4.0</em:minVersion>,<em:minVersion>4.0</em:minVersion>,g' \
#    %buildroot/%ciddir/install.rdf

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
	        <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
	        <em:minVersion>%version</em:minVersion>
	        <em:maxVersion>%version.*</em:maxVersion>
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

%changelog
* Fri May 20 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt1
- New package for firefox-gost
