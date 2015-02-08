%define cid            langpack-ru@thunderbird.mozilla.org
%define cid_dir        %tbird_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %tbird_noarch_extensionsdir/%cid_dict

Name:		thunderbird-esr-ru
Version:	31.4.0
Release:	alt1
Summary:	Russian (RU) Language Pack for Thunderbird

License:	GPL
Group:		Networking/Mail
URL:		http://www.mozilla-russia.org/products/thunderbird/
Packager:	Andrey Cherepanov <cas@altlinux.org>
BuildArch:	noarch

Source0:	ru-%version.xpi

Requires:	hunspell-ru
Conflicts:	thunderbird-ru

BuildRequires(pre):	rpm-build-thunderbird-esr
BuildRequires:		unzip

%description
The Mozilla Thunderbird in Russian.

%prep
%setup -c -n %name-%version/%cid

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
	               em:name="Russian (RU) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{3550f703-e582-4d05-9a08-453d09bdfdc6}</em:id>
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
* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- ru localization for thunderbird-esr
