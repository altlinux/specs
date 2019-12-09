#ExclusiveArch: %{ix86} x86_64
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate ImageMagick-tools unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define pkgname		SweetHome3D
%define pkgmod		3DModels
%define pkgtextu	Textures
%define modelver	1.6.4
%define textuver	1.2
%define texturesver	1.6
%define furniturever	1.24

Name:		sweethome3d
Version:	6.1
Release:	alt1_2jpp8
Summary:	A free interior design application, with a 3D preview
License:	GPLv2
Group:		Graphics
URL:		http://www.sweethome3d.com/
Source0:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-source/SweetHome3D-%{version}-src/%{pkgname}-%{version}-src.zip
Source1:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Contributions-%{modelver}.zip
Source2:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-KatorLegaz-%{modelver}.zip
Source3:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-LucaPresidente-%{modelver}.zip
Source4:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Reallusion-%{modelver}.zip
Source5:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Scopia-%{modelver}.zip
Source6:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Trees-%{modelver}.zip
Source7:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-BlendSwap-CC-BY-%{modelver}.zip
Source8:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-BlendSwap-CC-0-%{modelver}.zip
Source9:	sweethome3d_128x128.png
Source10:	sweethome3d-4.6-script
Source11:	http://sourceforge.net/projects/%{name}/files/TexturesLibraryEditor-source/TexturesLibraryEditor-%{texturesver}-src.zip
Source12:	http://sourceforge.net/projects/%{name}/files/FurnitureLibraryEditor-source/FurnitureLibraryEditor-%{furniturever}-src.zip
Source13:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-textures/Textures-%{textuver}/%{pkgtextu}-Contributions-%{textuver}.zip
Source14:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-textures/Textures-%{textuver}/%{pkgtextu}-eTeksScopia-%{textuver}.zip
Patch0:		sweethome3d-6.1-nomacosx.patch
Patch1:		sweethome3d-6.0-build_xml.patch
Patch2:		sweethome3d-6.1-javadoc.patch
Patch3:		sweethome3d-6.0-disable_checkForUpdates.patch

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	batik
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	gnu-regexp
BuildRequires:	java-1.8.0-openjdk-javaws mozilla-plugin-java-1.8.0-openjdk
BuildRequires:	ImageMagick-tools
BuildRequires:	itext-core
BuildRequires:	java-javadoc
BuildRequires:	java3d
BuildRequires:	java3d-javadoc
BuildRequires:	jdepend
BuildRequires:	jdom
BuildRequires:	jiprof
BuildRequires:	junit
BuildRequires:	jpackage-utils
BuildRequires:	sunflow-sweethome3d
BuildRequires:	vecmath
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-apis

Requires:	batik
Requires:	bouncycastle-pkix
Requires:	java-1.8.0-openjdk-javaws mozilla-plugin-java-1.8.0-openjdk
Requires:	itext-core
Requires:	java3d
Requires:	jpackage-utils
Requires:	sunflow-sweethome3d
Requires:	vecmath
Source44: import.info


%description
Sweet Home 3D is a free interior design application that helps you place your
furniture on a house 2D plan, with a 3D preview.
Available at http://www.sweethome3d.eu/, this program is aimed at people who
want to design their interior quickly, whether they are moving or they just
want to redesign their existing home. Numerous visual guides help you draw the
plan of your home and layout furniture. You may draw the walls of your rooms
upon the image of an existing plan, and then, drag and drop furniture onto the
plan from a catalog organized by categories. Each change in the 2D plan is
simultaneously updated in the 3D view, to show you a realistic rendering of
your layout.

#-----------------------------------------------------------------------------

%package	3dmodels
Summary:	Some extra 3DModels for %{pkgname}
Group:		Graphics
BuildArch:	noarch
Requires:	%{name} >= %{version}-%{release}

%description	3dmodels
Some extra 3DModels for %{pkgname}.

This package contains:
* 3DModels Contributions %{modelver}
* 3DModels KatorLegaz %{modelver}
* 3DModels Scopia %{modelver}
* 3DModels Trees %{modelver}
* 3DModels LucaPresidente %{modelver}
* 3DModels Reallusion-%{modelver}
* 3DModels BlendSwap-CC-BY-%{modelver}
* 3DModels BlendSwap-CC-0-%{modelver}

#-----------------------------------------------------------------------------

%package	textures
Summary:	Some extra Textures for %{pkgname}
Group:		Graphics
BuildArch:	noarch
Requires:	%{name} >= %{version}-%{release}

%description	textures
Some extra Textures for %{pkgname}.

This package contains:
* Textures Contributions %{textuver}
* Textures eTeksScopia %{textuver}

#-----------------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for %{pkgname}
Group:		Development/Java
BuildArch:	noarch

%description	javadoc
Sweet Home 3D - An application for placing your furniture on a house 2D plan,
with a 3D preview

This package contains javadoc for %{pkgname}.

#-----------------------------------------------------------------------------

%prep
%setup -q -n %{pkgname}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


for j in $(find . -name "*.jar"); do
  mv $j $j.no
done

rm -rf lib/windows
rm -rf lib/macosx
rm -rf lib/linux

pushd lib
  ln -sf $(build-classpath batik-all) batik-svgpathparser-1.7.jar
  ln -sf $(build-classpath itext) iText-2.1.7.jar
  ln -sf $(build-classpath java3d/j3dcore) j3dcore.jar
  ln -sf $(build-classpath java3d/j3dutils) j3dutils.jar
  ln -sf $(build-classpath sunflow-0.07.3i) sunflow-0.07.3i.jar
  ln -sf $(build-classpath vecmath) vecmath.jar
# FIXME for package jar that does not exist on Mageia
   mv jmf.jar.no jmf.jar
   mv freehep-vectorgraphics-svg-2.1.1b.jar.no freehep-vectorgraphics-svg-2.1.1b.jar
   mv jeksparser-calculator.jar.no jeksparser-calculator.jar
popd

# Abbot is not building in mga and sweethome3d build without so do add in mageia only if it builds OK
pushd libtest
  ln -sf $(build-classpath gnu-regexp) gnu-regexp-1.1.0.jar
  ln -sf $(build-classpath jdepend) jdepend-2.9.jar
  ln -sf $(build-classpath jdom) jdom-1.0.jar
  ln -sf /usr/share/icedtea-web/javaws.jar jnlp.jar
  ln -sf $(build-classpath jiprof/profile) profile.jar
popd

for c in $(find lib -name "*.class"); do
  rm -f $c
done

dos2unix  *.TXT
chmod 644 *.TXT

# for extra 3DModels
mkdir -p 3DModels-Contributions
pushd 3DModels-Contributions
    unzip -q %{SOURCE1}
    mv README.TXT README-3DModels-Contributions.txt
    mv LICENSE.TXT LICENSE-3DModels-Contributions.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-KatorLegaz
pushd 3DModels-KatorLegaz
    unzip -q %{SOURCE2}
    mv README.TXT README-3DModels-KatorLegaz.txt
    mv LICENSE.TXT LICENSE-3DModels-KatorLegaz.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-LucaPresidente
pushd 3DModels-LucaPresidente
    unzip -q %{SOURCE3}
    mv README.TXT README-3DModels-LucaPresidente.txt
    mv LICENSE.TXT LICENSE-3DModels-LucaPresidente.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Reallusion
pushd 3DModels-Reallusion
    unzip -q %{SOURCE4}
    mv README.TXT README-3DModels-Reallusion.txt
    mv LICENSE.TXT LICENSE-3DModels-Reallusion.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Scopia
pushd 3DModels-Scopia
    unzip -q %{SOURCE5}
    mv README.TXT README-3DModels-Scopia.txt
    mv LICENSE.TXT LICENSE-3DModels-Scopia.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Trees
pushd 3DModels-Trees
    unzip -q %{SOURCE6}
    mv README.TXT README-3DModels-Trees.txt
    mv LICENSE.TXT LICENSE-3DModels-Trees.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-BlendSwap-CC-BY
pushd 3DModels-BlendSwap-CC-BY
    unzip -q %{SOURCE7}
    mv README.TXT README-3DModels-BlendSwap-CC-BY.txt
    mv LICENSE.TXT LICENSE-3DModels-BlendSwap-CC-BY.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-BlendSwap-CC-0
pushd 3DModels-BlendSwap-CC-0
    unzip -q %{SOURCE8}
    mv README.TXT README-3DModels-BlendSwap-CC-0.txt
    mv LICENSE.TXT LICENSE-3DModels-BlendSwap-CC-0.txt
    sed -i 's/\r$//' *.txt
popd
# for extra Textures
mkdir -p Textures-Contributions
pushd Textures-Contributions
    unzip -q %{SOURCE13}
    mv README.TXT README-Textures-Contributions.txt
    mv LICENSE.TXT LICENSE-Textures-Contributions.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p Textures-eTeksScopia
pushd Textures-eTeksScopia
    unzip -q %{SOURCE14}
    mv README.TXT README-Textures-eTeksScopia.txt
    mv LICENSE.TXT LICENSE-Textures-eTeksScopia.txt
    sed -i 's/\r$//' *.txt
popd

%build
%ant application furniture textures help javadoc

%install
# .jar-repertory
mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 build/SweetHome3D.jar \
  %{buildroot}%{_javadir}/%{name}/%{pkgname}-%{version}.jar

(
  cd %{buildroot}%{_javadir}/%{name}
  for jar in *-%{version}*; do
    ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`
  done
)

for i in Furniture Textures Help; do
    install -pm 644 build/$i.jar %{buildroot}%{_javadir}/%{name}
done

rm -rf lib/iText-2.1.7.jar
rm -rf lib/j3dcore.jar
rm -rf lib/j3dutils.jar
rm -rf lib/sunflow-0.07.3i.jar
rm -rf lib/vecmath.jar
rm -rf lib/Loader3DS1_2u.jar

# FIXME for package jar that does not exist on Mageia
install -pm 644 lib/jmf.jar %{buildroot}%{_javadir}/%{name}
install -pm 644 lib/freehep-vectorgraphics-svg-2.1.1b.jar %{buildroot}%{_javadir}/%{name}
install -pm 644 lib/jeksparser-calculator.jar %{buildroot}%{_javadir}/%{name}
# FIXME for display the sweethome3d splash screen
install -pm 644 libtest/jnlp.jar.no %{buildroot}%{_javadir}/%{name}/jnlp.jar

# 3Dmodels-repertory
mkdir -p %{buildroot}%{_datadir}/%{name}/%{pkgmod}
for i in Contributions KatorLegaz LucaPresidente Reallusion Scopia Trees BlendSwap-CC-BY BlendSwap-CC-0; do
    install -m 644 3DModels-$i/*.sh3f %{buildroot}%{_datadir}/%{name}/%{pkgmod}
done

# Textures-repertory
mkdir -p %{buildroot}%{_datadir}/%{name}/%{pkgtextu}
for i in Contributions eTeksScopia; do
    install -m 644 Textures-$i/*.sh3t %{buildroot}%{_datadir}/%{name}/%{pkgtextu}
done

# javadoc-repertory
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

# binary-repertory
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE10} %{buildroot}%{_bindir}/%{name}

# icons-repertory
mkdir -p %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_iconsdir} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/
cp -pr %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png
cp -pr %{SOURCE9} %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -pr deploy/%{pkgname}*.jpg %{buildroot}%{_iconsdir}
cp -pr deploy/%{pkgname}*.gif %{buildroot}%{_iconsdir}

for png in 64x64 32x32 22x22 16x16; do
  mkdir -p %{buildroot}%{_iconsdir}/hicolor/${png}/apps/
  convert -geometry $png %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/${png}/apps/%{name}.png
done

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Sweet Home 3D
Name[fr]=Sweet Home 3D
Name[pt]=Sweet Home 3D
Name[ru]=Милый дом 3D
GenericName=Sweet Home 3D
GenericName[fr]=Sweet Home 3D
GenericName[ru]=Проектирование домашнего интерьера в 3D
Comment=Design Application
Comment[fr]=Application de conception d'intérieur en 3D
Comment[pt]=Aplicativo de design de interiores
Comment[ru]=Программа проектирования домашнего интерьера в 3D
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
StartupWMClass=com-eteks-sweethome3d-SweetHome3D
Categories=Application;Graphics;2DGraphics;3DGraphics;
MimeType=application/vnd.sh3d;
EOF

desktop-file-install --mode=0644 --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

# mime-entry for sh3d files
mkdir -p %{buildroot}%{_datadir}/mime/packages
cat > %{buildroot}%{_datadir}/mime/packages/%{name}.xml <<EOF
<?xml version="1.0"?>
<mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
        <mime-type type="application/vnd.sh3d">
                <comment>SweetHome3D Project</comment>
                <glob pattern="*.sh3d"/>
        </mime-type>
</mime-info>
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING* LICENSE.TXT README.TXT
%{_bindir}/%{name}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/Furniture.jar
%{_javadir}/%{name}/Help.jar
%{_javadir}/%{name}/%{pkgname}-%{version}.jar
%{_javadir}/%{name}/%{pkgname}.jar
%{_javadir}/%{name}/Textures.jar
# FIXME for package jar that does not exist on Mageia
%{_javadir}/%{name}/jmf.jar
%{_javadir}/%{name}/freehep-vectorgraphics-svg-2.1.1b.jar
%{_javadir}/%{name}/jeksparser-calculator.jar
# FIXME for display the sweethome3d splash screen
%{_javadir}/%{name}/jnlp.jar
#
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/*.jpg
%{_iconsdir}/*.gif
%{_iconsdir}/hicolor/*x*/apps/%{name}.png

%files 3dmodels
%doc 3DModels-Contributions/*.txt 3DModels-KatorLegaz/*.txt 3DModels-Scopia/*.txt 3DModels-Trees/*.txt 3DModels-LucaPresidente/*.txt 3DModels-Reallusion/*.txt 3DModels-BlendSwap-CC-BY/*.txt 3DModels-BlendSwap-CC-0/*.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{pkgmod}
%{_datadir}/%{name}/%{pkgmod}/*.sh3f

%files textures
%doc Textures-Contributions/*.txt Textures-eTeksScopia/*.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{pkgtextu}
%{_datadir}/%{name}/%{pkgtextu}/*.sh3t

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*


%changelog
* Mon Dec 09 2019 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_2jpp8
- added obsoletes (closes: #37301)

