%define _unpackaged_files_terminate_build 1

Name: ivyplusplus
Version: 1.42
Release: alt1

Summary: Ant extensions used by Lombok build
License: MIT
Group: Development/Java
Url: http://zwitserloot.com/ivyplusplus
Vcs: https://github.com/rzwitserloot/ivyplusplus
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: ant
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: ivy-local
BuildRequires: apache-ivy
BuildRequires: ecj
BuildRequires: jpackage-default
BuildRequires: maven-local

%description
IvyPlusPlus extends Ant with additional tasks. It is required to build Lombok.

%prep
%setup

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
sed 's/@VERSION@/%version/g' buildScripts/maven-pom.xml > build/ivyplusplus-%version.pom
%mvn_file com.zwitserloot:ivyplusplus %name
%mvn_artifact build/ivyplusplus-%version.pom dist/ivyplusplus-%version.jar
%mvn_install

%files -f .mfiles
%doc README.markdown LICENSE

%changelog
* Fri Apr 10 2026 Ivan Khanas <xeno@altlinux.org> 1.42-alt1
- First build for ALT.
