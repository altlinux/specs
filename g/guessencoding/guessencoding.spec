# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             guessencoding
Version:          1.4
Release:          alt2_7jpp7
Summary:          Guess encoding of files and return configured reader
Group:            Development/Java
License:          ASL 2.0
URL:              http://docs.codehaus.org/display/GUESSENC/
# svn export http://svn.codehaus.org/guessencoding/tags/guessencoding-1.4/
# tar caf guessencoding-1.4.tar.gz guessencoding-1.4
Source0:          %{name}-%{version}.tar.gz
# Comment out wagon-webdav extension as it is not needed in Fedora
Patch0:           guessencoding-webdav.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apache-commons-io
BuildRequires:    junit

Requires:         jpackage-utils
Source44: import.info

%description
The purpose of this library is to "guess" the encoding of files, and retrieve
a reader that is properly configured to use the right encoding as guessed.
The library is able to recognize the various Unicode encoding variants:

    * UTF-8
    * UTF-16LE - Low Endian
    * UTF-16BE - Big Endian
    * UTF-32

If a Unicode encoding isn't recognized, it's an 8-bit encoding. If the 8-bit
encoding is not US-ASCII, the default platform 8-bit encoding is assumed
whatever it is. However, the library cannot guess between different 8-bit
encodings. Only statistical analysis, n-grams and similar techniques specific
to each language used in those files can help guessing the encoding, but this
is not supported by the library.


%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .webdav


%build
mvn-rpmbuild install javadoc:aggregate


%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version

