# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           svnkit
Version:        1.7.6
Release:        alt2_7jpp7
Summary:        Pure java subversion client library

Group:          Development/Java
# License located at http://svnkit.com/license.html
License:        TMate
URL:            http://www.svnkit.com/
Source0:        http://www.svnkit.com/org.tmatesoft.svn_%{version}.src.zip
#Source1:       http://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit/1.7.6/svnkit-1.7.6.pom
# our pom has adjusted dependencies versions to Fedora platform:
Source1:        %{name}-%{version}.pom
Source2:        %{name}-build.xml
# just in SRPM due to nailgun comes included in svnkit upstream sources:
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source4:        https://www.apache.org/licenses/LICENSE-1.1.txt

# patch reported at http://issues.tmatesoft.com/_persistent/svnkit-jna-3.5.0.patch?file=67-134&v=0&c=true
Patch0:         svnkit-jna-3.5.0.patch
# Fix for current trilead-ssh2
Patch1:		svnkit-1.7.6-trilead-ssh2-215.patch

BuildArch:      noarch

BuildRequires:          jpackage-utils >= 0:1.6
BuildRequires:          ant
BuildRequires:          sequence-library
BuildRequires:          subversion-javahl >= 1.5
BuildRequires:          jna >= 3.0
BuildRequires:          trilead-ssh2 >= 215
BuildRequires:          sqljet >= 1.1.4
BuildRequires:          tomcat-servlet-3.0-api >= 7.0.0
Requires:               jpackage-utils >= 0:1.6
Requires:               subversion-javahl >= 1.5
Requires:               jna >= 3.0
Requires:               trilead-ssh2 >= 213
Requires:               sqljet >= 1.1.4
Requires:               sequence-library
Requires:               tomcat-servlet-3.0-api >= 7.0.0
Source44: import.info


%description
SVNKit is a pure java Subversion client library. You would like to use SVNKit
when you need to access or modify Subversion repository from your Java
application, as a standalone program and plugin or web application. Being a
pure java program, SVNKit doesn't need any additional configuration or native
binaries to work on any OS that runs java.

%package javahl
Summary:        Replacement for the native JavaHL API 
Group:          Development/Java
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       subversion-javahl >= 1.5

%description javahl
SVNKit provides a replacement for the native JavaHL API - the SVNClient  class 
that does not use any native bindings. This SVNClient  also implements 
SVNClientInterface (org.tigris.subversion.javahl) as the native one 
but uses only the SVNKit library API (written in pure Java!).
If you have code written with using the native SVNClient class, 
you may simply replace that class with the new one provided by SVNKit. 

%package cli
Summary:        Jsvn is a pure java Subversion client 
Group:          Development/Java
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cli
Includes jsvn, a pure java Subversion command line interface based on SVNKit.

%package javadoc
Summary:        Javadoc for SVNKit
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for SVNKit - Java Subversion client library.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1

# delete binary jars from upstream
rm -rf gradle gradlew gradlew.bat
rm -rf svnkit-test/nailgun/nailgun-0.7.1.jar

# check for forbidden artifacts 
WHITELIST="\(template.jar\)"
FORBIDDEN=""
for j in $(find . ! -regex ".*$WHITELIST.*" -and \( -name '*.jar' -or -name '*.class' \) ); do
        if [ ! -L $j ] ; then
        FORBIDDEN="$FORBIDDEN $j"
        fi
done
if [ ! -z "$FORBIDDEN" ] ; then
        echo "These files should be deleted and symlinked to system: $FORBIDDEN" 
        exit 1
fi
  

# this jars are not removed because are templates from upstream and have no binary contents: 
#      - svnkit/src/main/java/org/tmatesoft/svn/core/io/repository/template.jar
#      - svnkit/src/main/resources/org/tmatesoft/svn/core/io/repository/template.jar

cp %{SOURCE2} build.xml

cat > %{name}.build.properties <<EOF
svnkit.version.major=1
svnkit.version.minor=7
svnkit.version.micro=6
svnkit.version.build=local
EOF


%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  all


%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 %{name}/dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 %{name}-javahl16/dist/%{name}-javahl16.jar %{buildroot}%{_javadir}/%{name}-javahl.jar
install -p -m 644 %{name}-cli/dist/%{name}-cli.jar %{buildroot}%{_javadir}/%{name}-cli.jar

install -p -Dm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf


%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt CHANGES.txt
%config(noreplace,missingok) /etc/%{name}.conf

%files cli
%{_javadir}/%{name}-cli.jar

%files javahl
%{_javadir}/%{name}-javahl.jar

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_7jpp7
- new release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_6jpp7
- target 5 build

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_6jpp7
- replaced by fc package

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp5.0
- converted from JPackage by jppimport script

