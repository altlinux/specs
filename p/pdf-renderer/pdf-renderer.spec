Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%global with_gcj %{!?_without_gcj:1}%{?_without_gcj:0}
%global alternate_name PDFRenderer
%global cvs_version 2009_04_05
%global cvs_rel .%(echo %{cvs_version}|sed 's|_||g')cvs

Summary:        A 100% Java PDF renderer and viewer
Name:           pdf-renderer
Version:        0
Release:        alt3_0.5%{?cvs_rel}jpp5
License:        LGPLv2+
URL:            https://pdf-renderer.dev.java.net/
Group:          Development/Java
Source0:        https://pdf-renderer.dev.java.net/files/documents/6008/131974/%{alternate_name}-%{cvs_version}-src.zip
BuildRequires: ant
BuildRequires: ant-apache-regexp
BuildRequires: jpackage-utils
BuildRequires: urw-fonts
%if %{with_gcj}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
Requires: java-1.5.0-gcj
%else
BuildArch:      noarch
%endif
Requires: jpackage-utils >= 1.5
Requires: urw-fonts
Provides:       %{alternate_name} == %{version}-%{release}

%description
The PDF Renderer is just what the name implies: an open source,
all Java library which renders PDF documents to the screen using 
Java2D. Typically this means drawing into a Swing panel, but it 
could also draw to other Graphics2D implementations. It could be 
used to draw on top of PDFs, share them over a network, convert 
PDFs to PNG images, or maybe even project PDFs into a 3D scene.

%package javadoc
Summary:        Javadoc for %{alternate_name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for the %{alternate_name} package.

%prep
%setup -q -n %{alternate_name}-%{cvs_version}-src

# Remove preshipped binaries
find . -name "*.jar" -exec rm {} \;

# Fix encoding issues
find . -name "*.java" -exec native2ascii {} {} \;

# Remove preshipped fonts and ...
find . -name "*.pfb" -exec rm {} \;

# ... tell the program to use system-fonts instead.
# Script provided by Mamoru Tasaka:
# https://bugzilla.redhat.com/show_bug.cgi?id=466394#c4
# -------------------------------------------------------------
pushd src/com/sun/pdfview/font/res/
INPUT=BaseFonts.properties
OUTPUT=BaseFonts.properties.1
FONTDIR=%{_datadir}/fonts/default/Type1

rm -f $OUTPUT
cat $INPUT | while read line
 do
 newline=$line
 if echo $newline | grep -q 'file=.*pfb'
  then
  pfbname=$(echo $newline | sed -e 's|^.*file=||')
  newline=$(echo $newline | sed -e "s|file=|file=${FONTDIR}/|")
 elif echo $newline | grep -q 'length='
  then
  size=$(ls -al ${FONTDIR}/$pfbname | awk '{print $5}')
  newline=$(echo $newline | sed -e "s|length=.*|length=$size|")
 fi
 echo $newline >> $OUTPUT
done
mv -f $OUTPUT $INPUT
popd
# -------------------------------------------------------------

%build
%ant

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{alternate_name}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%if %{with_gcj}
 %{_bindir}/aot-compile-rpm
%endif

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# compat symlink
pushd %buildroot%_javadir
ln -s pdf-renderer.jar PDFRenderer.jar

%files
%doc demos
%{_javadir}/%{name}.jar
%if %{with_gcj}
%{_libdir}/gcj/%{name}
%endif
%_javadir/PDFRenderer.jar

%files javadoc
%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Mon May 25 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.5.20090405cvsjpp5
- added symlink for another jar name (PDFRenderer)

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.5.20090405cvsjpp5
- noarch javadoc

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.5.20090405cvsjpp5
- new version

