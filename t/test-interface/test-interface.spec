Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global test_interface_version 1.0
%global build_with_sbt 0

Name:           test-interface
Version:        %{test_interface_version}
Release:        alt2_9jpp8
Summary:        Uniform interface to Scala and Java test frameworks

License:        BSD
URL:            https://github.com/sbt/test-interface
Source0:        https://github.com/sbt/test-interface/archive/v%{test_interface_version}.tar.gz
%if !%{build_with_sbt}
Source1:	http://mirrors.ibiblio.org/maven2/org/scala-sbt/%{name}/%{version}/%{name}-%{version}.pom
%endif

BuildArch:	noarch
%if %{build_with_sbt}
BuildRequires:  sbt
%else
BuildRequires:	java-devel
%endif
BuildRequires:	javapackages-local
Source44: import.info

%description

Uniform test interface to Scala/Java test frameworks (specs,
ScalaCheck, ScalaTest, JUnit and other)

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%mvn_file org.scala-sbt:test-interface %{name}

%if %{build_with_sbt}
sed -i -e 's/2[.]10[.]2/2.10.3/g' build.sbt
sed -i -e '/scalatest_2.10/d' build.sbt

sed -i -e 's/0[.]12[.]4/0.13.1/g' project/build.properties
rm project/plugins.sbt

cp -r /usr/share/java/sbt/ivy-local .
mkdir boot
%else # building without sbt

cp -p %{SOURCE1} pom.xml
# Remove unavailable test dep
%pom_remove_dep :scalatest_2.10

%endif

%build

%if %{build_with_sbt}
export SBT_BOOT_DIR=boot
export SBT_IVY_DIR=ivy-local
sbt package deliverLocal publishM2Configuration
%else # building without sbt
mkdir -p classes target/api
%javac -d classes $(find src/main/java -name "*.java")

(
cd classes
mkdir -p META-INF
cat > META-INF/MANIFEST.MF << 'EOF'
Manifest-Version: 1.0
Implementation-Vendor: org.scala-sbt
Implementation-Title: %{name}
Implementation-Version: %{version}
Implementation-Vendor-Id: org.scala-sbt
Specification-Vendor: org.scala-sbt
Specification-Title: %{name}
Specification-Version: %{version}
EOF
%jar -cMf ../target/%{name}.jar *
)

%javadoc -d target/api -classpath $PWD/target/%{name}.jar $(find src/main/java -name "*.java")

cp pom.xml target/%{name}-%{version}.pom

%mvn_artifact target/%{name}-%{version}.pom target/%{name}.jar

%endif

%install

%mvn_install -J target/api

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp8
- cleaned up req on javapackages

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp8
- new version

