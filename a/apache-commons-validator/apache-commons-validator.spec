Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       validator
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.3.1
Release:          alt1_9jpp7
Summary:          Apache Commons Validator
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:           commons-validator-1.3.1-crosslink.patch
# https://issues.apache.org/jira/browse/VALIDATOR-303
Patch1:           commons-validator-1.3.1-srcencoding.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    jakarta-oro
BuildRequires:    junit
Requires:         apache-commons-beanutils
Requires:         apache-commons-digester
Requires:         apache-commons-logging
Requires:         jakarta-oro
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# This should go away with F-17 after maven-shared-reporting-impl is fixed.
Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:1.3.1-2
Source44: import.info

%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
BuildRequires:    java-javadoc
Requires:         java-javadoc
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# use textui instead of awtui (not available in junit4+)
sed -i 's:junit.awtui.TestRunner.main:junit.textui.TestRunner.main:g' \
        src/test/org/apache/commons/validator/*java

%build
# TODO: Use Maven for building as soon as upstream provides proper build.xml.
#       Currently upstream build.xml uses antrun plugin to build, so downloads
#       during build process can't be prohibited.

export CLASSPATH=$(build-classpath \
                   apache-commons-logging \
                   apache-commons-digester \
                   apache-commons-beanutils \
                   junit \
                   jakarta-oro )

ant -Dskip.download=true -Dbuild.sysclasspath=first dist

%check
export CLASSPATH=$(build-classpath \
                   apache-commons-logging \
                   apache-commons-digester \
                   apache-commons-beanutils \
                   junit \
                   jakarta-oro )

ant -Dskip.download=true -Dbuild.sysclasspath=first test

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api*/* %{buildroot}%{_javadocdir}/%{name}/

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*%{short_name}.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_9jpp7
- fc update

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_0.r832761.5jpp6
- marked oro as essential dependency due to maven-site-plugin

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_0.r832761.5jpp6
- new version

