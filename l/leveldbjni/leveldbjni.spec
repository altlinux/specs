Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: gcc-c++
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
%global debug_package %{nil}

# rpmbuild < 4.6 support
%if ! 0%{?__isa_bits}
%ifarch x86_64 ia64 ppc64 sparc64 s390x alpha ppc64le aarch64
%global __isa_bits 64
%else
%global __isa_bits 32
%endif
%endif

Name:          leveldbjni
Version:       1.8
Release:       alt1_13jpp8
Summary:       A Java Native Interface to LevelDB
License:       BSD
URL:           https://github.com/fusesource/leveldbjni/
Source0:       https://github.com/fusesource/leveldbjni/archive/%{name}-%{version}.tar.gz

BuildRequires: autoconf-common
BuildRequires: automake-common
BuildRequires: libtool-common
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-javadoc)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires: mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires: mvn(org.fusesource.hawtjni:maven-hawtjni-plugin)
BuildRequires: mvn(org.iq80.leveldb:leveldb-api)
# see https://bugzilla.redhat.com/show_bug.cgi?id=881608
BuildRequires: pkgconfig(leveldb) >= 1.7.0
BuildRequires: libsnappy-devel
Source44: import.info

%description
LevelDB JNI gives you a Java interface to the
LevelDB C++ library which is a fast key-value
storage library written at Google that provides
an ordered mapping from string keys to string
values.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :jxr-maven-plugin
%pom_remove_plugin :surefire-report-maven-plugin
# disable non linux module
%pom_remove_dep org.fusesource.%{name}:%{name}-osx %{name}-all
%pom_remove_dep org.fusesource.leveldbjni:leveldbjni-win32 %{name}-all
%pom_remove_dep org.fusesource.leveldbjni:leveldbjni-win64 %{name}-all

%pom_xpath_remove "pom:Private-Package" %{name}-all
%pom_xpath_remove "pom:Export-Package" %{name}-all
%pom_xpath_remove "pom:Import-Package" %{name}-all

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
<Import-Package>
 org.fusesource.hawtjni.runtime,
 org.iq80.leveldb*;version=${leveldb-api-version}
</Import-Package>' %{name}-all

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
<Export-Package>
 org.fusesource.leveldbjni*;version=${project.version}
</Export-Package>' %{name}-all

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
<Private-Package>
 org.fusesource.leveldbjni.internal*
</Private-Package>' %{name}-all

%pom_xpath_remove "pom:Bundle-NativeCode"  %{name}-all

%if %{__isa_bits} == 64

%pom_remove_dep org.fusesource.%{name}:%{name}-linux32 %{name}-all

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" "
<Bundle-NativeCode>
  META-INF/native/linux64/libleveldbjni.so;osname=Linux;processor=x86-64
</Bundle-NativeCode>" %{name}-all

%else

%pom_remove_dep org.fusesource.%{name}:%{name}-linux64 %{name}-all

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" "
<Bundle-NativeCode>
  META-INF/native/linux32/libleveldbjni.so;osname=Linux;processor=x86
</Bundle-NativeCode>" %{name}-all

%endif

rm -r %{name}/src/test/java/org/fusesource/%{name}/test/DBTest.java
# cp -f /usr/lib/rpm/config.{sub,guess} /usr/share/automake-*/compile leveldbjni/src/main/native-package/autotools/

%build

%ifarch ppc64
export MAVEN_OPTS='-Xms1024m -Xmx2048m -XX:MaxPermSize=384m'
%endif
%mvn_file :%{name}-all %{name}-all
%mvn_file :%{name}-linux%{__isa_bits} %{name}-linux
export JAVA_HOME=%{_jvmdir}/java LEVELDB_HOME=%{_prefix} SNAPPY_HOME=%{_prefix}
%mvn_build -- -Plinux%{__isa_bits},all -Dleveldb=%{_prefix} -Dsnappy=%{_prefix}

%install
%mvn_install

%files  -f .mfiles
%doc changelog.md readme.md releasing.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_11jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_8jpp8
- new version

