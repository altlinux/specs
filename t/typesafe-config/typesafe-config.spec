Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          typesafe-config
Version:       1.2.0
Release:       alt1_9jpp8
Summary:       Configuration library for JVM languages
License:       ASL 2.0
URL:           https://github.com/typesafehub/config/
Source0:       https://github.com/typesafehub/config/archive/v%{version}.tar.gz
Source1:       typesafe-config.bnd

BuildRequires: aqute-bnd
BuildRequires: javapackages-local
BuildRequires: sbt

BuildArch:     noarch
Source44: import.info

%description
Configuration library for JVM languages.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n config-%{version}

rm -f project/plugins.sbt

sed -i -e '/SbtOsgi/d' project/Build.scala
sed -i -e '/OsgiKeys/d' project/Build.scala
sed -i -e 's/osgiSettings [+][+]//g' project/Build.scala
sed -i -e '/override val settings/d' project/Build.scala

sed -i -e '/de.johoop/d' config/build.sbt
sed -i -e '/JacocoPlugin/d' config/build.sbt
sed -i -e '/findbugs/,+2d' config/build.sbt
sed -i -e '/jacoco/,+2d' config/build.sbt

sed -i -e '/% "test"$/,+2d' config/build.sbt

sed -i -e '/com.typesafe.sbt/d' build.sbt
sed -i -e '/SbtGit/,+2d' build.sbt
sed -i -e '/useGpg/,+2d' build.sbt
sed -i -e '/publishSigned/,+2d' build.sbt
sed -i -e '/publishLocalSigned/,+2d' build.sbt

sed -i -e 's/2[.]10[.][0-2]/2.10.4/' build.sbt

sed -i -e 's/Some("1[.]6")/Some("1.8")/' project/JavaVersionCheck.scala

for buildsbt in $(find . -name build.sbt) ; do
    (echo ; echo ; echo 'version := "%{version}"'; echo) >> $buildsbt
done

# missing test deps
rm -rf config/src/test

cp -r /usr/share/sbt/ivy-local .
mkdir boot

%mvn_file com.typesafe:config %{name}

%build
export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local

#sbt package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
sbt package makePom deliverLocal doc

bnd wrap -p %{SOURCE1} -o config/target/config.jar --version %{version} config/target/config-%{version}.jar

%install
%mvn_artifact config/target/config-%{version}.pom config/target/config.jar
%mvn_install -J config/target/api

%files -f .mfiles
%doc NEWS.md README.md
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_9jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_8jpp8
- new jpp release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_7jpp8
- new version

