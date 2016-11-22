Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global majorversion 2
Name:          metadata-extractor2
Version:       2.8.1
Release:       alt1_3jpp8
Summary:       Extracts EXIF, IPTC, XMP, ICC and other metadata from image files
License:       ASL 2.0
URL:           http://drewnoakes.com/code/exif/
Source0:       https://github.com/drewnoakes/metadata-extractor/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.adobe.xmp:xmpcore)
BuildRequires: mvn(junit:junit)

Provides:      mvn(com.drewnoakes:metadata-extractor) = %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Metadata Extractor is a straightforward Java library
for reading metadata from image files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metadata-extractor-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

# Unavailable plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
# Unwanted plugins
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# Unneeded task
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
# Fix manifest entries
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest/pom:addClasspath" false
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest" "<mainClass>com.drew.imaging.ImageMetadataReader</mainClass>"
# Use standard maven output directory
%pom_xpath_remove "pom:build/pom:directory"
%pom_xpath_remove "pom:build/pom:outputDirectory"

# Add OSGi support
%pom_xpath_set "pom:project/pom:packaging" bundle 
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

# Fix non ASCII chars
for s in Source/com/drew/lang/GeoLocation.java \
 Source/com/drew/metadata/icc/IccDescriptor.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

sed -i 's/\r//' LICENSE-2.0.txt README.md CONTRIBUTING.md Resources/javadoc-stylesheet.css

%mvn_file :metadata-extractor %{name}
%mvn_alias :metadata-extractor "drew:metadata-extractor"
%mvn_compat_version ":metadata-extractor" %{majorversion}

%build

%mvn_build

%install
%mvn_install

%jpackage_script com.drew.imaging.ImageMetadataReader "" "" %{name}-%{majorversion}:xmpcore %{name} true

%files -f .mfiles
%{_bindir}/*
%doc CONTRIBUTING.md README.md
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp8
- new version

