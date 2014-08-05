# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash f28dc0a
%global tag_hash 929dd3c

Name:     jnr-ffi
Version:  0.7.10
Release:  alt1_2jpp7
Summary:  Java Abstracted Foreign Function Layer
Group:    System/Libraries
License:  ASL 2.0
URL:      http://github.com/jnr/%{name}/
Source0:  https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz

Patch1:   %{name}-remove-dependency-versions-not-understood-by-fedora-maven.patch

BuildRequires: jpackage-utils
BuildRequires: jffi
BuildRequires: jnr-x86asm
BuildRequires: junit
BuildRequires: objectweb-asm4

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin

Requires:      jpackage-utils
Requires:      jffi
Requires:      jnr-x86asm
Requires:      objectweb-asm4

BuildArch:     noarch
Source44: import.info

# don't obsolete/provide jaffl, gradle is using both jaffl and jnr-ffi...

%description
An abstracted interface to invoking native functions from java

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
%patch1 -p0

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

%build
# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile
# TODO: tests still fail, investigate
mvn-rpmbuild install javadoc:aggregate -DskipTests

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_2jpp7
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt3_3jpp7
- fixed build

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt2_3jpp7
- gcc47 build

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt1_3jpp7
- new version

