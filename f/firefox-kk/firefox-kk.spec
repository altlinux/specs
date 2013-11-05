%define cid            langpack-kk@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       kk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-kk
Version:	25.0
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
	               em:name="Kazakh (KZ) Dictionary"
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
ln -s %_datadir/myspell/kk_KZ.aff %buildroot/%cid_dict_dir/dictionaries/kk.aff
ln -s %_datadir/myspell/kk_KZ.dic %buildroot/%cid_dict_dir/dictionaries/kk.dic


%files
%cid_dir
%cid_dict_dir

%changelog
* Wed Nov 06 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New version (25.0).

* Fri Oct 25 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New version (24.0).

* Wed Aug 14 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New version (23.0).

* Mon Jul 01 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New version (22.0).

* Tue Jun 18 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt2
- Add dictionary extension (ALT#29063).

* Wed Jun 05 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New version (21.0)

* Mon Apr 15 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New version (20.0)

* Mon Mar 11 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New version (19.0.2)
- First build for ALT Linux.
