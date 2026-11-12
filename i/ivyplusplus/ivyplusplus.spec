%define _unpackaged_files_terminate_build 1

Name: ivyplusplus
Version: 1.42
Release: alt2

Summary: Ant extensions used by Lombok build
License: MIT AND Apache-2.0
Group: Development/Java
URL: https://zwitserloot.com/ivyplusplus
VCS: https://github.com/rzwitserloot/ivyplusplus.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-system-dependencies.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: ant
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: ivy-local
BuildRequires: apache-ivy
BuildRequires: ecj
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local

%description
IvyPlusPlus extends Ant with additional tasks. It is required to build Lombok.

%prep
%setup
%autopatch -p1

# Use system ivy/ivy-local (XMvn) instead of bundled downloader/settings.
sed -i \
  -e '/<target name="download-ivy"/,/<\/target>/d' \
  -e 's#<target name="config-ivy" depends="download-ivy">#<target name="config-ivy">#' \
  -e '/<taskdef classpath="lib\/${ivy.lib}" resource="org\/apache\/ivy\/ant\/antlib.xml" uri="antlib:org.apache.ivy.ant" \/>/d' \
  -e 's#<ivy:configure file="buildScripts/ivysettings.xml" />#<ivy:configure />#' \
  -e 's#<javac #<javac encoding="UTF-8" #g' \
  -e '/build\/pack\/com\/zwitserloot\/ivyplusplus\/ssh\/internal/d' \
  build.xml

# Keep only tasks required for lombok build; drop publish/create helpers.
rm -rf src/com/zwitserloot/ivyplusplus/createProject \
       src/com/zwitserloot/ivyplusplus/ssh \
       src/com/zwitserloot/ivyplusplus/mavencentral

sed -i \
  -e '/create-artifact-bundle/d' \
  -e '/scpUpload/d' \
  -e '/sshExec/d' \
  src/com/zwitserloot/ivyplusplus/antlib.xml

sed -i \
  -e '/org.projectlombok.*jsch-ant-fixed/d' \
  -e '/com.zwitserloot.*cmdreader/d' \
  -e '/com.googlecode.jarjar.*jarjar/d' \
  -e '/com.hierynomus.*sshj/d' \
  buildScripts/ivy.xml

%build
%ant -Divy.mode=local dist

%install
%jar xf %_javadir/apache-ivy/ivy.jar META-INF/NOTICE
mv META-INF/NOTICE NOTICE.ivy
sed 's/@VERSION@/%version/g' buildScripts/maven-pom.xml > build/ivyplusplus-%version.pom
%mvn_file com.zwitserloot:ivyplusplus %name
%mvn_artifact build/ivyplusplus-%version.pom dist/ivyplusplus-%version.jar
%mvn_install
install -d %buildroot%_sysconfdir/ant.d
echo 'ivyplusplus apache-ivy/ivy ecj/ecj' > \
    %buildroot%_sysconfdir/ant.d/%name

%files -f .mfiles
%doc LICENSE NOTICE.ivy
%_sysconfdir/ant.d/%name

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.42-alt2
- Use system Ivy and ECJ and adapt to the current ECJ API.

* Fri Apr 10 2026 Ivan Khanas <xeno@altlinux.org> 1.42-alt1
- First build for ALT.
