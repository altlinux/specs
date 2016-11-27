# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install gcc-c++ perl(CGI.pm) perl(CGI/Carp.pm) perl(English.pm) perl(HTML/Parser.pm) perl(LWP.pm) perl(LWP/UserAgent.pm) unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global pkgdate 2015.10.13
# Build jsmol by default
%bcond_without jsmol

Name:        jmol
Version:     14.4.0
Release:     alt1_2.2015.10.13jpp8
Summary:     An open-source Java viewer for chemical structures in 3D
Group:       Engineering
# most is LGPLv2+, src/com/obrador is combination of IJG and BSD
# src/org@/jmol/export/image is partially 2 clause BSD
License:     LGPLv2+ and IJG and BSD
URL:         http://jmol.sourceforge.net
BuildArch:   noarch
Source0:     http://downloads.sourceforge.net/%{name}/Jmol-%{version}_%{pkgdate}-full.tar.gz
Source1:     http://wiki.jmol.org/images/1/1c/Jmol_icon13.png
# Patch to get Jmol to build in Fedora (location of JAR files)
Patch0:      jmol-14.2.12-fedorabuild.patch
# Don't try to sign jars
Patch1:      jmol-14.0.11-dontsign.patch


BuildRequires:    ant ant-contrib
BuildRequires:    desktop-file-utils
BuildRequires: gettext-tools libasprintf-devel
BuildRequires:    apache-commons-cli
BuildRequires:    java-devel >= 1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    jspecview >= 2
BuildRequires:    naga
# In newer releases some of the necessary Java classes are
# in the browser plugin package
BuildRequires: java-1.8.0-openjdk-javaws mozilla-plugin-java-1.8.0-openjdk
Requires: java-1.8.0-openjdk-javaws mozilla-plugin-java-1.8.0-openjdk
Requires:         java >= 1.6.0
Requires:         jpackage-utils
Requires:         apache-commons-cli
Requires:         jspecview >= 2
Requires:         naga
Source44: import.info

%description
Jmol is a free, open source molecule viewer for students, educators,
and researchers in chemistry and biochemistry.

%if %{with jsmol}
%package -n jsmol
Summary:     JavaScript-Based Molecular Viewer From Jmol
Group:       Engineering
Requires:    %{name} = %{version}
BuildRequires: web-assets-devel
Requires:    web-assets-filesystem

%description -n jsmol
JSmol is the extension of the Java-based molecular visualization
applet Jmol (jmol.sourceforge.net) as an HTML5 JavaScript-only
web app. It can be used in conjunction with the Java applet to
provide an alternative to Java when the platform does not support
that (iPhone/iPad) or does not support applets (Android). Used in
conjunction with the Jmol JavaScript Object
(http://wiki.jmol.org/index.php/Jmol_Javascript_Object ), JSmol
seamlessly offers alternatives to Java on these non-Applet platforms.

JSmol can read all the files that Jmol reads. You can do all the
scripting that Jmol does. You can create all the buttons and links
and such that you are used to creating for Jmol. All of the rendering
capability of the Jmol applet is there. JSmol has both a console and
a popup menu.

JSmol is integrated fully with JSME and JSpecView.

A "lite" version of JSmol provides minimal functionality
(balls and sticks only) for extremely small-bandwith apps.
%endif

%package javadoc
Summary:     Java docs for %{name}
Group:       Development/Java
Requires:    %{name} = %{version}
Requires:    jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package doc
Summary:     Documentation for %{name}
Group:       Development/Java
Requires:    %{name} = %{version}

%description doc
The documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}_%{pkgdate}
%patch0 -p1 -b .fedorabuild
%patch1 -p1 -b .nosign

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
# Need to be able to find netscape.javascript.*classes
PLUGIN_JAR=%{_datadir}/icedtea-web/plugin.jar
jar tf $PLUGIN_JAR | grep javascript/JSObject.class
ant --execdebug -lib $PLUGIN_JAR jar applet-jar doc

%install
install -D -p -m 644 build/Jmol.jar %{buildroot}%{_javadir}/Jmol.jar
install -D -p -m 644 build/JmolApplet.jar %{buildroot}%{_javadir}/JmolApplet.jar
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%jpackage_script org.openscience.jmol.app.Jmol "" "" Jmol:commons-cli:jspecview.app:jspecview.applet jmol true

# Install desktop file
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications jmol.desktop

# Javadoc files
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%if %{with jsmol}
pushd appletweb
    unzip jsmol.zip
    pushd jsmol
        mkdir -p %{buildroot}%{_jsdir}/jsmol
        cp -pr *.htm *.js j2s js %{buildroot}%{_jsdir}/jsmol
    popd
popd
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf

%files
%doc build/doc/* README.txt COPYRIGHT.txt LICENSE.txt ChangeLog.html CHANGES.txt
%{_bindir}/%{name}
%{_javadir}/Jmol.jar
%{_javadir}/JmolApplet.jar
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%config(noreplace,missingok) /etc/java/%name.conf

%if %{with jsmol}
%files -n jsmol
%{_jsdir}/jsmol
%endif

%files javadoc
%{_javadocdir}/%{name}/

%files doc
%doc build/doc/*

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 14.4.0-alt1_2.2015.10.13jpp8
- new version

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 14.2.12-alt2_3.2015.01.22jpp8
- rebuild with mozilla-plugin-java-1.8.0-openjdk

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 14.2.12-alt1_3.2015.01.22jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 13.2.4-alt1_1jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 12.0.48-alt1_8jpp7
- new version

