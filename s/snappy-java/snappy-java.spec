Name:           snappy-java
Version:        1.1.10.7
Release:        alt1

Summary:        Snappy compressor/decompressor for Java
License:        Apache-2.0
Group:          Development/Java
URL:            http://xerial.org/snappy-java/
VCS:            https://github.com/xerial/snappy-java

Source0:        %name-%version.tar
Source1:        %name-%version.pom

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
snappy-java is a Java port of the snappy, a fast C++ compresser/decompresser
developed by Google.

%javadoc_package

%prep
%setup

cp %SOURCE1 pom.xml

%pom_add_plugin org.apache.felix:maven-bundle-plugin \
'<extensions>true</extensions>
<configuration>
	<instructions>
		<Bundle-ActivationPolicy>lazy</Bundle-ActivationPolicy>
		<Bundle-Activator>org.xerial.snappy.SnappyBundleActivator</Bundle-Activator>
		<Bundle-DocURL>http://www.xerial.org/</Bundle-DocURL>
		<Bundle-License>http://www.apache.org/licenses/LICENSE-2.0.txt</Bundle-License>
		<Bundle-Name>snappy-java: A fast compression/decompression library</Bundle-Name>
		<Bundle-SymbolicName>org.xerial.snappy.snappy-java</Bundle-SymbolicName>
		<Bundle-Vendor>xerial.org</Bundle-Vendor>
		<Implementation-Title>%name</Implementation-Title>
		<Implementation-URL>%url</Implementation-URL>
		<Implementation-Vendor-Id>org.xerial.snappy</Implementation-Vendor-Id>
		<Implementation-Vendor>xerial.org</Implementation-Vendor>
		<Implementation-Version>%version</Implementation-Version>
		<Specification-Title>snappy-java</Specification-Title>
		<Specification-Vendor>xerial.org</Specification-Vendor>
		<Specification-Version>%version</Specification-Version>
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

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Thu Jul 02 2026 Evgeniy Serov <scala@altlinux.org> 1.1.10.7-alt1
- Updated to 1.1.10.7.
- Returned to Sisyphus.

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2.4-alt2_19jpp11
- fc update

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2.4-alt2_18jpp11
- fc update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2.4-alt2_14jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_11jpp8
- explicit build with java8

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_6jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_2jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_6jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt3_5jpp7
- fixed build

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt1_3jpp7
- new version

