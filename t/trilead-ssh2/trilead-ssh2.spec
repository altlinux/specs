Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           trilead-ssh2
Version:        215
Release:        alt1_1jpp7
Summary:        SSH-2 protocol implementation in pure Java

Group:          Development/Java
License:        BSD
URL:            http://www.trilead.com/Products/Trilead_SSH_for_Java/
# Not working anymore...
#http://www.trilead.com/DesktopModules/Releases/download_file.aspx?ReleaseId=4102
Source0:        trilead-ssh2-build%{version}.zip
Source1:        build.xml
Source2:        http://repo1.maven.org/maven2/com/trilead/trilead-ssh2/1.0.0-build%{version}/trilead-ssh2-1.0.0-build%{version}.pom

BuildRequires:  jpackage-utils
BuildRequires:  ant
Requires:       jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# javadoc is gone in 215
Provides:	%{name}-javadoc = %{version}-%{release}
Obsoletes:	%{name}-javadoc <= 213-11

BuildArch:      noarch
Source44: import.info

#Obsoletes:              ganymed-ssh2 <= 210


%description
Trilead SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for trilead-ssh2.

%prep
%setup -q -n %{name}-build%{version}
cp %{SOURCE1} .

# change file encoding
iconv -f ISO-8859-1 -t UTF-8 -o HISTORY.txt HISTORY.txt

# delete the jars that are in the archive
find . -name '*.jar' -delete

# fixing wrong-file-end-of-line-encoding warnings
sed -i 's/\r//' LICENSE.txt README.txt HISTORY.txt

%build
ant


%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.tmatesoft.svnkit %{name} %{version} JPP %{name}

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/*
%doc LICENSE.txt HISTORY.txt README.txt


%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:215-alt1_1jpp7
- update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_10_redhat_1jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_5jpp6
- added pom

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 213-alt1_6jpp6
- new version

