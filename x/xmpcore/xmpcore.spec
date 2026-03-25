Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xmpcore
Version:       6.1.10
Release:       alt1
Summary:       Java XMP Library
License:       BSD
URL:           https://www.adobe.com/devnet/xmp.html
Source0:       https://repo1.maven.org/maven2/com/adobe/xmp/%{name}/%{version}/%{name}-%{version}-sources.jar
# from https://repo1.maven.org/maven2/com/adobe/xmp/xmpcore/6.1.10/xmpcore-6.1.10.pom
# customized:
# fix compiler,javadoc-plugin configuration
# fix manifest entries
Source1:       %{name}-%{version}.pom
# from http://download.macromedia.com/pub/developer/xmp/sdk/XMP-Toolkit-SDK-5.1.2.zip
Source2:       %{name}-BSD-License.txt
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
The XMP Library for Java is based on the
C++ XMPCore library and the API is similar.

%prep
%setup -q -c

mkdir java
mv com java/
rm -r META-INF

cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} BSD-License.txt
sed -i 's/\r//' BSD-License.txt

#Add necessary plugins
%pom_xpath_inject "pom:project" "
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>"

%pom_xpath_inject "pom:project" "
 <build>
    <directory>target</directory>
    <sourceDirectory>java</sourceDirectory>
    <outputDirectory>target/classes</outputDirectory>

    <plugins>

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.0</version>
            <configuration>
                <source>11</source>
                <target>11</target>
            </configuration>
        </plugin>

        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>buildnumber-maven-plugin</artifactId>
            <version>1.2</version>
            <executions>
                <execution>
                    <phase>validate</phase>
                    <goals>
                        <goal>create-timestamp</goal>
                    </goals>
                </execution>
            </executions>
            <configuration>
                <timestampFormat>yyyy MMM dd HH:mm:ss-z</timestampFormat>
                <timestampPropertyName>timestamp</timestampPropertyName>
            </configuration>
        </plugin>

    </plugins>

  </build>"

%mvn_file : %{name}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference BSD-License.txt

%changelog
* Wed Mar 25 2026 Anton Meleshnikov <alton@altlinux.org> 6.1.10-alt1
- new version (disable javadoc)

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 5.1.2-alt1_16jpp11
- jvm11 build, added unzip BR

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_13jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_11jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_4jpp8
- new version

