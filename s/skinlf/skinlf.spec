Name: skinlf
Version: 6.7
Release: alt2
Summary: Skin look and feel Skinning library for java

Group: Development/Java
License: ASL 2.0 and zlib and ASL 1.1
Url: http://skinlf.dev.java.net/

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-clean.tar.gz
# Original Source# Contains code that we cannot ship.
# Download the upstream tarball and invoke this script while in the
# tarball's directory
# ./skinlf-generate-tarball.sh 6.7-20060722
Source1: %name-generate-tarball.sh

BuildArch: noarch

#See http://bollin.googlecode.com/svn/libskinlf-java/trunk
#for patchset maintained by Scilab developer, Sylvestre Ledru.
# These patches have been modified.
Patch: skinlf-nosun-jimi-patch.patch
#Release file does not contain building tools. thats CVS only. Don't know which CVS revision to check out for release CVS.
Patch1: skinlf-build-xml-patch.patch
#Create common.xml as release omits building tools
Patch2: skinlf-common-xml-patch.patch
#org.apache.xpath has been removed from JDK1.5 and above
#patch to use com.sun.org.apache.xpath.internal.XPathAPI instead
Patch3: skinlf-sun-jdk1.5-xpath-patch.patch

BuildRequires: laf-plugin ant ant-nodeps rpm-build-java dos2unix

%description
Skin Look And Feel is a java framework that is  able to read GTK (The
Gimp ToolKit) and KDE (The K Desktop Environment) skins to enhance
your application.
SkinLF supports GUI controls such as Buttons, Checks, Radios, Scrollbars,
Progress Bar, Lists,  Tables, Internal Frames, Colors, Background
Textures, Regular Windows.

%prep
%setup -q
%patch0

#building patches
%patch1
%patch2
#Code fixing
%patch3

#dos2unix Doc files
for i in "CHANGES README LICENSE LICENSE_nanoxml" ;
do
	dos2unix -d2u $i;
done

#Remove jar files
rm -f ./lib/examples.jar
rm -f ./lib/nativeskin.jar
rm -f ./lib/skinlf.jar

#rm due to dubious license
rm -f ./src/examples/Clock.java

#Sanitise package -- disallow jar files
JAR_files=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
	JAR_files="$JAR_files $j"
	fi
done

if [ ! -z "$JAR_files" ] ; then
	echo "These JAR files should be deleted and symlinked to system JAR files: $JAR_files"
	#Uncomment this line before accepting package
	exit 1
fi

%build
ant
#Construct-a-jar Dont use ant jar as it tries to unpack laf-plugin
pushd build/classes
jar cf %name-%version.jar .
popd

%install
mkdir -p %buildroot/%_javadir
install -m644 ./build/classes/%name-%version.jar -D %buildroot%_javadir/%name-%version.jar
cd %buildroot%_javadir/
ln -s %name-%version.jar %name.jar

%files
%doc CHANGES README LICENSE  LICENSE_nanoxml
%_javadir/%name.jar
%_javadir/%name-%version.jar

%changelog
* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 6.7-alt2
- Fix BuildRequires (ALT #21520)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 6.7-alt1
- Initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

*Sat Dec 06 2008  <mycae(a!t)yahoo.com> 6.7-6
- Fixed jar dir
- Changed primary jar to name-version.jar, & linked.
- Added clean tarball generator

* Wed Dec 03 2008  <mycae(a!t)yahoo.com> 6.7-5
- Added LICENSE_nanoxml
- Updated licence spec line to include ASL 1.1 & zlib
- removed Clock.java due to incompatible license

* Sat Nov 29 2008 <mycae(a!t)yahoo.com> 6.7-4
- Updated BuildRequires to inlcude laf-plugin
- Silence several rpmlint errors
	- ASL 2.0 vs Apache Source Licence 2.0
	- Fix arch
	- Fix EOL on docs.

* Sun Nov 23 2008 <mycae(a!t)yahoo.com> 6.7-3
- Modify description field

* Sun Nov 16 2008 <mycae(a!t)yahoo.com> 6.7-2
- Fix version numbering
- Fix top level dir when building jar

* Sat Nov 01 2008 <mycae(a!t)yahoo.com> 6.7-1
- Create spec file

