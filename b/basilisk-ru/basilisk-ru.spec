%define cid            langpack-ru@basilisk.browser
%define cid_dir        %basilisk_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %basilisk_noarch_extensionsdir/%cid_dict

%define min_version	52.9
%define max_version	52.*

%define bname		basilisk
%define sdir		searchplugins
%define newmoon_dir 	%basilisk_datadir/browser/
%define search_dir 	%newmoon_dir%sdir

Name: basilisk-ru

Version: 2025.02.22
Release: alt1

ExclusiveArch: x86_64 aarch64

Summary: Russian (RU) Language Pack for Pale Moon
License: MPL-2.0

Group: Networking/WWW
Url:   forum.ru-board.com
Vcs:   https://github.com/Enobarbous/basilisk-ru-langpack 

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  basilisk-ru-langpack_%version.xpi


Requires: basilisk >= 2024.08.16
Requires: hunspell-ru

Obsoletes: basilisk-ru_yo-dictionary basilisk-ru_ie-dictionary
Provides: basilisk-ru_yo-dictionary basilisk-ru_ie-dictionary

BuildRequires(pre):	rpm-build-basilisk 
# Automatically added by buildreq on Sat Oct 18 2025
# optimized out: libgpg-error sh5
BuildRequires: unzip

%description
The basilisk Russian translation and dictionary.

%prep
%setup -c -n %name-%version/%cid

%install

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

install -d -m 755 %buildroot/%newmoon_dir/

# Install translation
cp -r -- langpack-ru/* %buildroot/%cid_dir


cd -

#cp -r -- %sdir  %buildroot/%search_dir/


# Install dictionary

cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
<?xml version="1.0" encoding="utf-8"?>
<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:em="http://www.mozilla.org/2004/em-rdf#">
    <Description about="urn:mozilla:install-manifest">
        <em:id>langpack-ru@basilisk.browser</em:id>
        <em:name>Russian (RU) Language Pack</em:name>
        <em:version>22.02.2025</em:version>
        <em:type>8</em:type>
        <em:creator>altlinux.org</em:creator>
        <em:targetApplication>
            <Description>
                <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
                <em:minVersion>52.9</em:minVersion>
                <em:maxVersion>52.*</em:maxVersion>
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

#%files -n basilisk-searchplugins
#%search_dir

%changelog
* Sat Oct 18 2025 Hihin Ruslan <ruslandh@altlinux.ru> 2025.02.22-alt1
- Init Build

