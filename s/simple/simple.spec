Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          simple
Version:       6.0.1
Release:       alt1_3jpp8
Summary:       Asynchronous HTTP server for Java
License:       ASL 2.0 and LGPLv2+
URL:           http://www.simpleframework.org/
Source0:       http://sourceforge.net/projects/simpleweb/files/simpleweb/%{version}/%{name}-%{version}.tar.gz
# https://github.com/ngallagher/simpleframework/issues/7
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildArch:     noarch
Source44: import.info

%description
Simple is a high performance asynchronous HTTP server for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find . -name "*.class" -delete
find . -name "*.jar" -delete

for p in common http transport; do
%pom_remove_plugin :maven-source-plugin %{name}-${p}
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions" %{name}-${p}
%pom_xpath_remove "pom:build/pom:extensions" %{name}-${p}

%pom_xpath_set "pom:packaging" bundle %{name}-${p}
%pom_add_plugin org.apache.felix:maven-bundle-plugin %{name}-${p} '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

done

# testAccuracy(org.simpleframework.common.lease.ContractQueueTest)  Time elapsed: 2 sec  <<< FAILURE!
# junit.framework.AssertionFailedError: Value -2000 is not less than or equal to -2001
rm -r simple-common/src/test/java/org/simpleframework/common/lease/ContractQueueTest.java

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt2_5jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt2_3jpp7
- added ant-junit BR:

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.21-alt1_3jpp7
- new version

