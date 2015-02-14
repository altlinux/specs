%define cid            langpack-uk@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       uk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name: firefox-esr-uk
Version: 31.4.0
Release: alt1

Summary: Ukrainian (UA) Language Pack for Firefox
License: %gpl2plus
Group: Networking/WWW

URL: http://www.mozilla.org.ua
Source: uk.xpi

Packager: Alexey Gladkov <legion@altlinux.ru>

Requires: hunspell-uk
BuildArch: noarch

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires: unzip

Conflicts:	firefox-uk

%description
The Mozilla Firefox Ukrainian translation.

%prep
%setup -c -n firefox-uk-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

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
	        <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
	        <em:minVersion>%version</em:minVersion>
	        <em:maxVersion>%version.*</em:maxVersion>
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

%changelog
* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- uk localization for firefox-esr
