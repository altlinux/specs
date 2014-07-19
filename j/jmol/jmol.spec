# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ perl(CGI.pm) perl(CGI/Carp.pm) perl(English.pm) perl(HTML/Parser.pm) perl(LWP.pm) perl(LWP/UserAgent.pm)
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:        jmol
Version:     13.2.4
Release:     alt1_1jpp7
Summary:     An open-source Java viewer for chemical structures in 3D
Group:       Engineering
# most is LGPLv2+, src/com/obrador is combination of IJG and BSD
# src/org@/jmol/export/image is partially 2 clause BSD
License:     LGPLv2+ and IJG and BSD
URL:         http://jmol.sourceforge.net
BuildArch:   noarch
Source0:     http://downloads.sourceforge.net/%{name}/Jmol-%{version}-full.tar.gz
# Image available at "http://wiki.jmol.org:81/index.php/Image:Jmol_icon_128.png"
Source1:     Jmol_icon_128.png
# Patch to get Jmol to build in Fedora (location of JAR files)
Patch0:      jmol-13.2.3-fedorabuild.patch
# Unbundle bundled classes from jars
Patch1:      jmol-13.2.3-unbundle.patch
# Don't try to sign jars
Patch2:      jmol-13.2.3-dontsign.patch
# Don't ignore the system classpath
Patch3:      jmol-12.0.48-classpath.patch



BuildRequires:    ant ant-contrib
BuildRequires:    desktop-file-utils
BuildRequires:    gettext-devel
BuildRequires:    itext
BuildRequires:    apache-commons-cli
BuildRequires:    jpackage-utils
BuildRequires:	  jspecview
BuildRequires:	  naga

%if 0%{?fedora} > 14
# In newer releases some of the necessary Java classes are
# in the browser plugin package
BuildRequires:    mozilla-plugin-java-1.7.0-openjdk
Requires:    mozilla-plugin-java-1.7.0-openjdk
%endif

Requires:    jpackage-utils
Requires:   itext
Requires:   vecmath
Requires:   apache-commons-cli
Source44: import.info

%description
Jmol is a free, open source molecule viewer for students, educators,
and researchers in chemistry and biochemistry.


%package javadoc
Summary:    Java docs for %{name}
Group:        Development/Java
Requires:    %{name} = %{version}-%{release}
Requires:    jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package doc
Summary:    Documentation for %{name}
Group:        Development/Java
Requires:    %{name} = %{version}-%{release}

%description doc
The documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .fedorabuild
%patch1 -p1 -b .unbundle
%patch2 -p1 -b .nosign
%patch3 -p1 -b .classpath

# Remove binaries
find -name '*.class' -exec rm -f '{}' \;
find -name '*.exe' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
rm -f jars/*

# Remove executable permissions from documentation
find -name "*.txt" -exec chmod 644 {} \;
# Fix EOL encoding
for doc in README.txt COPYRIGHT.txt LICENSE.txt CHANGES.txt; do
sed "s|\r||g" $doc > $doc.new && \
touch -r $doc $doc.new && \
mv $doc.new $doc
done


# Make desktop file
cat > jmol.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Jmol
Comment=An open-source Java viewer for chemical structures in 3D
Exec=jmol
Icon=jmol
Terminal=false
Type=Application
Categories=Education;Science;Chemistry;Physics;DataVisualization;
EOF

%build
export ANT_OPTS="-Dfile.encoding=utf-8"
%if 0%{?fedora} > 15
# Need to be able to find netscape.javascript.*classes
PLUGIN_JAR=%{_datadir}/icedtea-web/plugin.jar
jar tf $PLUGIN_JAR | grep javascript/JSObject.class
#ant --execdebug -lib $PLUGIN_JAR doc jar applet-jar

ant --execdebug -lib $PLUGIN_JAR jar
ant --execdebug -lib $PLUGIN_JAR applet-jar
ant --execdebug -lib $PLUGIN_JAR doc
%else
ant --execdebug doc jar applet-jar
%endif

%install
install -D -p -m 644 build/JmolUnsigned.jar %{buildroot}%{_javadir}/Jmol.jar
install -D -p -m 644 build/JmolApplet.jar %{buildroot}%{_javadir}/JmolApplet.jar
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%jpackage_script org.openscience.jmol.app.Jmol "" "" Jmol:commons-cli:vecmath:itext jmol true

# Install desktop file
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
%if (0%{?fedora} && 0%{?fedora} < 19) || ( 0%{?rhel} && 0%{?rhel} < 7)
--vendor=fedora \
%endif
jmol.desktop

# Javadoc files
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf

%files
%doc build/doc/* README.txt COPYRIGHT.txt LICENSE.txt ChangeLog.html CHANGES.txt
%{_bindir}/%{name}
%{_javadir}/Jmol.jar
%{_javadir}/JmolApplet.jar
%{_datadir}/pixmaps/%{name}.png
%if (0%{?fedora} && 0%{?fedora} < 19) || ( 0%{?rhel} && 0%{?rhel} < 7)
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%config(noreplace,missingok) /etc/java/%name.conf

%files javadoc
%{_javadocdir}/%{name}/

%files doc
%doc build/doc/*

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 13.2.4-alt1_1jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 12.0.48-alt1_8jpp7
- new version

