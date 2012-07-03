# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global genericname gdata

Name:           %{genericname}-java
Version:        1.45.0
Release:        alt1_3jpp7
Summary:        Client libraries to write Google Data API client applications in Java
Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/gdata-java-client/
Source0:        http://gdata-java-client.googlecode.com/files/%{genericname}-src.java-%{version}.zip
Source1:        %{genericname}-core-%{version}-pom.xml
BuildArch:      noarch

BuildRequires:     jpackage-utils
BuildRequires:     ant
BuildRequires:     javamail servlet25
BuildRequires:     guava jsr-305
Requires:          jpackage-utils
Source44: import.info

%description
The client library provides tools and an abstraction layer, letting you
easily construct queries and use response data without having to create
HTTP requests or process HTTP responses by hand. Each client library
provides classes that correspond to the elements and data types used by
the Google Data APIs. Each client library also provides extensions for
specific Google services that have Data APIs.


%package javadoc
Summary:           Javadocs for gdata
Group:             Development/Java
Requires:          %name = %{version}-%{release}
Requires:          jpackage-utils
BuildArch: noarch

%description javadoc
gdata development documentation.


%prep
%setup -q -n gdata
pushd java

rm -rf lib/* gdata/java/deps/* classes doc

properties=build-src/build.properties
for jars in \
  "servlet servlet" \
  "mail javamail/mail" \
  "activation activation" \
  "guava jsr-305"
do
  f=`echo $jars | gawk '{print $1;}'`
  g=`echo $jars | gawk '{print $2;}'`
  %{__sed} -i -e "/^${f}/s|=.*$|=`build-classpath ${g}`|" $properties
done

for i in $(ls manifest/*.manifest); do
  %{__sed} -i '/class-path/I d' $i
  echo "Export-Package: $(grep '^Name' $i | sed -e 's|^Name: *||' -e 's|/|.|g' -e 's|.$||');version=\"%{version}\"" >> $i
done

popd


%build
pushd java
ant -lib lib/%{genericname}-core-1.0.jar:lib/%{genericname}-client-1.0.jar -buildfile build-src.xml clean build

find src -name '*.java' |xargs javadoc -classpath \
  `build-classpath javamail guava jsr-305`:/etc/alternatives/java_sdk_openjdk/lib/tools.jar -d doc
popd


%install
#jars
pushd java
pushd lib
install -d $RPM_BUILD_ROOT%{_javadir}/%{genericname}
install -m644 *.jar $RPM_BUILD_ROOT%{_javadir}/%{genericname}
for i in `ls *.jar`; do
  x=`echo $i | tr -d [:digit:]`
  ln -s $i $RPM_BUILD_ROOT%{_javadir}/%{genericname}/${x%%-\.\.jar}.jar
done
popd

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{genericname}
cp -rp doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{genericname}
popd

# pom dir
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# pom
# Only gdata-core included for now, feel free to add more artifacts to pom file if you need
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{genericname}-%{genericname}-core.pom

# depmap
%add_maven_depmap JPP.%{genericname}-%{genericname}-core.pom %{genericname}/%{genericname}-core.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc COPYING
%dir %{_javadir}/%{genericname}
%{_javadir}/%{genericname}/%{genericname}-*.jar

%files javadoc
%dir %{_javadocdir}/%{genericname}
%{_javadocdir}/%{genericname}/*


%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.45.0-alt1_3jpp7
- new version

