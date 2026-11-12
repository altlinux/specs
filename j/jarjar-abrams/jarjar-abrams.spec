%define _unpackaged_files_terminate_build 1

Name: jarjar-abrams
Version: 1.18.1
Release: alt1

Summary: Java and Scala library shading tools
License: Apache-2.0
Group: Development/Java
URL: https://github.com/eed3si9n/jarjar-abrams
VCS: https://github.com/eed3si9n/jarjar-abrams.git

Source0: %name-%version.tar
Source1: build.sh
Source2: jarjar.pom
Source3: jarjar-abrams-core_2.13.pom
Source4: ant-jarjar.pom
Source5: maven-jarjar.pom

Patch: %name-test-fixtures.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: scala
BuildRequires: scala-library
BuildRequires: scala-reflect
BuildRequires: scala-parallel-collections
BuildRequires: objectweb-asm
BuildRequires: ant
BuildRequires: maven
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.ant:ant-junit)

%description
Jar Jar Abrams relocates Java and Scala classes and rewrites Scala signatures.
Includes the Java engine, Scala 2.13 library, Ant adapter and Maven adapter.

%prep
%setup
%autopatch -p1
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 .
%mvn_file com.eed3si9n.jarjar:jarjar %name/jarjar
%mvn_file :jarjar-abrams-core_2.13 %name/core
%mvn_file :ant-jarjar %name/ant
%mvn_file :maven-jarjar %name/maven

%build
# Upstream includes the generated Contraband sources. Avoid the sbt release
# plugin chain and compile those sources with the installed Scala compiler.
bash build.sh %_jvmdir/java-17-openjdk
%mvn_artifact jarjar.pom target/jarjar.jar
%mvn_artifact jarjar-abrams-core_2.13.pom target/jarjar-abrams-core_2.13.jar
%mvn_artifact ant-jarjar.pom target/ant-jarjar.jar
%mvn_artifact maven-jarjar.pom target/maven-jarjar.jar

%install
%mvn_install

%check
# The Scala core suite requires unavailable Verify; the Argonaut-only Java
# case uses a fixture availability assumption. Keep all other upstream tests.
test_cp="$(build-classpath junit hamcrest apache-commons-lang3 objectweb-asm/asm objectweb-asm/asm-commons)"
mkdir -p target/test-classes target/test-results
find jarjar/src/test/java integration/src/test/java -name '*.java' | sort >target/test.sources
%_jvmdir/java-17-openjdk/bin/javac -encoding UTF-8 --release 8 \
    -cp "target/jarjar.jar:$test_cp" -d target/test-classes @target/test.sources
cat >target/test-build.xml <<'EOF'
<project name="jarjar-upstream-tests" default="check" basedir="..">
  <target name="check">
    <junit fork="true" forkmode="once" printsummary="yes" haltonfailure="true"
           jvm="%_jvmdir/java-17-openjdk/bin/java" dir="${basedir}">
      <classpath>
        <pathelement path="${test.classpath}"/>
        <pathelement location="target/test-classes"/>
        <pathelement location="jarjar/src/test/resources"/>
      </classpath>
      <env key="JARJAR_CLASSPATH" value="${jarjar.classpath}"/>
      <formatter type="xml"/>
      <batchtest todir="target/test-results">
        <fileset dir="target/test-classes" includes="**/*Test.class"/>
      </batchtest>
    </junit>
  </target>
</project>
EOF
ant -f target/test-build.xml \
    -Dtest.classpath="$(pwd)/target/jarjar.jar:$test_cp" \
    -Djarjar.classpath="$(pwd)/target/jarjar.jar:$(build-classpath objectweb-asm/asm objectweb-asm/asm-commons)"

%files -f .mfiles
%doc jarjar/LICENSE jarjar/COPYING

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.18.1-alt1
- Initial build for ALT.
