%define cid            langpack-ru@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-esr-ru
Version:	38.2.1
Release:	alt1
Summary:	Russian (RU) Language Pack for Firefox

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla-russia.org/products/firefox/
Packager:	Andey Cherepanov <cas@altlinux.org>

Source0:	ru-%version.xpi
Source1: 	bugzillaaltlinux.xml

Requires:	firefox >= %version
Requires:	hunspell-ru
Obsoletes:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary
Provides:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

Conflicts:	firefox-ru

%description
The Mozilla Firefox Russian translation and dictionary.

%prep
%setup -c -n firefox-ru-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries \
	%buildroot%firefox_prefix/distribution/searchplugins/locale/ru

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir
cp %buildroot/%cid_dir/browser/searchplugins/* %SOURCE1 \
   %buildroot%firefox_prefix/distribution/searchplugins/locale/ru
rm -rf %buildroot/%cid_dir/browser/searchplugins

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
%firefox_prefix/distribution/searchplugins/locale/ru

%changelog
* Fri Aug 28 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.1-alt1
- New version
- Use locale search engines settings
- Add search in ALT Linux Bugzilla

* Wed Aug 12 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.0-alt1
- New version

* Thu Jul 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.0-alt1
- New version

* Tue May 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.0.1-alt1
- New version

* Wed May 13 2015 Andrey Cherepanov <cas@altlinux.org> 38.0-alt1
- New version

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 31.6.0-alt1
- New version

* Wed Feb 25 2015 Andrey Cherepanov <cas@altlinux.org> 31.5.0-alt1
- New version

* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- ru localization for firefox-esr
