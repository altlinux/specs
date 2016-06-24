Name: pdfsam
Version: 2.2.2e
Release: alt1

Summary: PDF Split And Merge

Group: Publishing
License: GPLv2
Url: http://www.pdfsam.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://sourceforge.net/projects/pdfsam/files/pdfsam-enhanced/%version/pdfsam-%version-out-src.tar

BuildArch: noarch
BuildRequires: ant
BuildRequires: unzip
BuildRequires: jpackage-utils
BuildRequires: dos2unix
BuildRequires: java-1.8.0-openjdk-devel
#Requires: jre-openjdk >= 1.7.0
# Requires:	jpackage-utils

%description
A Java based free open source tool to split and merge PDF documents.

%prep
%setup -c %name-%version
# extract all individual source zip files
for FILE in *.zip; do
    unzip -q -o "$FILE" ; rm -f "$FILE"
done
# fix line endings
for FILE in pdfsam-maine/doc/licenses/*/*.txt; do
    dos2unix -k -o "$FILE"
done
dos2unix -k -o pdfsam-maine/doc/enhanced/readme.txt
dos2unix -k -o pdfsam-maine/doc/enhanced/changelog-enhanced.txt

%build
cd pdfsam-maine/ant/
ant -Dpdfsam.deploy.dir="%_datadir/%name" \
    -Dworkspace.dir="../" \
    -Dbuild.dir="../build"

%install
# create start script
install -d -m 755 %buildroot%_bindir
cat << EOF > %buildroot%_bindir/pdfsam
#!/bin/bash
cd %_datadir/%name
java -jar %_datadir/%name/pdfsam.jar
cd -
EOF
chmod 755 %buildroot%_bindir/pdfsam

# create application dir and populate it
install -d -m 755 %buildroot%_datadir/%name
for i in ext lib plugins pdfsam-%version.jar pdfsam-config.xml; do
    mv build/pdfsam-maine/release/dist/pdfsam-enhanced/$i %buildroot%_datadir/%name/
done
ln -s pdfsam-%version.jar %buildroot%_datadir/%name/pdfsam.jar

### MENU ITEM ###
install -d -m 755 %buildroot%_pixmapsdir
cp build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/icons/*.??g %buildroot%_pixmapsdir

install -d -m 755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=PDFSam
Name[ru]=PDFSam
Comment=%summary
Comment[ru]=Разбивка и слияние PDF-файлов
Exec=%_bindir/%name
Icon=%_pixmapsdir/%{name}_basic.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Office;Java;Viewer;TextTools;
EOF

%files
%doc build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/changelog-enhanced.txt
%doc build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/pdfsam-1.5.0e-tutorial.pdf
%doc build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/readme.txt
%doc build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/license/
%_bindir/pdfsam
%_datadir/%name/
%_desktopdir/pdfsam.desktop
%_pixmapsdir/pdfsam*.png
%_pixmapsdir/pdfsam*.svg

%changelog
* Thu Jun 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2.2e-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.2.2e-3
+ Revision: 0c0fd58
- MassBuild#464: Increase release tag


