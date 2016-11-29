Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          mongo-java-driver2
Version:       2.14.1
Release:       alt1_3jpp8
Summary:       MongoDB Java Driver
# BSD-3-clause: src/main/org/bson/io/UTF8Encoding.java
# CC-BY-SA-3.0: src/main/org/bson/util/annotations/*
License:       ASL 2.0 and BSD and CC-BY-SA
URL:           http://docs.mongodb.org/ecosystem/drivers/java/
Source0:       https://github.com/mongodb/mongo-java-driver/archive/r%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)
# Those files are modifications of code included in:
# src/main/com/mongodb/util/Base64Codec.java
Provides:      bundled(apache-commons-codec)
# src/main/org/bson/util/annotations/*
Provides:      bundled(jcip-annotations)
# src/main/org/bson/io/UTF8Encoding.java
Provides:      bundled(postgresql-jdbc) = 9.0-801

BuildArch:     noarch
Source44: import.info

%description
Java library to connect to the MongoDB document database.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n mongo-java-driver-r%{version}
# Cleanup
find -name '*.class' -delete
find -name '*.jar' -print -delete

# Unwanted task
%pom_remove_plugin :maven-source-plugin

%mvn_compat_version org.mongodb:mongo-java-driver %{version} 2
%mvn_file org.mongodb:mongo-java-driver mongo-java-driver %{name}

%build

# Test suite disabled; require web connection
# java.net.ConnectException: Connection refused
# com.mongodb.MongoTimeoutException: Timed out after 10000 ms while waiting to connect.
# Client view of cluster state is {type=Unknown, servers=[{address=127.0.0.1:27017,
# type=Unknown, state=Connecting, exception={com.mongodb.MongoException$Network:
# Exception opening the socket}, caused by {java.net.ConnectException: Connection refused}}]
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc History.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.14.1-alt1_3jpp8
- new version

