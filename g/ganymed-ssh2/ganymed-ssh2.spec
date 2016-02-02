Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           ganymed-ssh2
Version:        210
Release:        alt1_16jpp8
Summary:        SSH-2 protocol implementation in pure Java

Group:          Development/Java
License:        BSD
URL:            http://www.ganymed.ethz.ch/ssh2/
Source0:        http://www.ganymed.ethz.ch/ssh2/ganymed-ssh2-build%{version}.zip
Source1:        build.xml

BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	coreutils
BuildRequires:  ant

BuildArch:		noarch
Source44: import.info

%description
Ganymed SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

%package javadoc
Summary:        Javadoc for ganymed-ssh2
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for ganymed-ssh2.

%prep
%setup -q -n %{name}-build%{version}

# delete the jars that are in the archive
rm %{name}-build%{version}.jar

cp %{SOURCE1} .

# fixing wrong-file-end-of-line-encoding warnings
sed -i 's/\r//' LICENSE.txt README.txt HISTORY.txt faq/FAQ.html
find examples -name \*.java -exec sed -i 's/\r//' {} \;

%build
ant

%install

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr javadoc/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc LICENSE.txt HISTORY.txt README.txt faq examples

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:210-alt1_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:210-alt1_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:210-alt1_13jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:210-alt1_12jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:250-alt1_1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:210-alt1_5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:210-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:210-alt1_2jpp1.7
- updated to new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:210-alt1_1jpp1.7
- converted from JPackage by jppimport script

