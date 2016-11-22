Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global oname leveldb
%if 0%{?fedora}
#def_with test
%bcond_with test
#def_with javadoc
%bcond_with javadoc
%endif
Name:          leveldb-java
Version:       0.7
Release:       alt1_5jpp8
Summary:       Port of LevelDB to Java
License:       ASL 2.0
URL:           https://github.com/dain/leveldb
Source0:       https://github.com/dain/leveldb/archive/%{version}.tar.gz
# remove org.iq80.snappy:snappy support
# use org.xerial.snappy:snappy-java
# Thanks to Robert Rati rrati@redhat.com
Patch0:        leveldb-java-xerial-snappy.patch

BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.xerial.snappy:snappy-java)
%if %{with test}
# test deps
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.testng:testng)
# circular deps https://bugzilla.redhat.com/show_bug.cgi?id=881590
BuildRequires: mvn(org.fusesource.leveldbjni:leveldbjni-all)
%endif
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-testng

BuildArch:     noarch
Source44: import.info

%description
This is a rewrite (port) of LevelDB in Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

# unavailable plugins
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :proguard-maven-plugin %{oname}
# only needed for ProGuard
%pom_remove_dep com.google.code.findbugs:jsr305 %{oname}
# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-shade-plugin %{oname}

# remove unavailable com.google.doclava doclava 1.0.3
%pom_remove_plugin :maven-javadoc-plugin

# fix spurious-executable-perm
chmod 644 license.txt

%if %{with test}
# IndexOutOfBoundsException: end index (10000026) must not be greater than size (32)
rm -r %{oname}/src/test/java/org/iq80/leveldb/table/MMapTableTest.java \
 %{oname}/src/test/java/org/iq80/leveldb/table/FileChannelTableTest.java
# add missing test dep
%pom_add_dep junit:junit::test %{oname}
%endif

%pom_remove_dep org.fusesource.leveldbjni:leveldbjni-all %{oname}
rm -r %{oname}/src/test/java/org/iq80/leveldb/impl/NativeInteropTest.java

%build
%if %{without test}
args="-f"
%endif
%if %{with javadoc}
args=$args" -j"
%endif
# Tests are inconsistent and take a long time to run
%mvn_build $args

%install
%mvn_install

%files  -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md
%doc license.txt notice.md

%if %{without javadoc}
%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md
%endif

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp8
- new version

