BuildRequires: /proc
BuildRequires: jpackage-compat
%global jtidyversion r938

Name:             jtidy
Version:          1.0
Release:          alt1_0.10.20100930svn1125jpp6
Epoch:            3
Summary:          HTML syntax checker and pretty printer
Group:            Development/Java
License:          zlib
URL:              http://jtidy.sourceforge.net/
# svn export -r1125 https://jtidy.svn.sourceforge.net/svnroot/jtidy/trunk/jtidy/ jtidy
# tar caf jtidy.tar.xz jtidy
Source0:          %{name}.tar.xz
Source1:          %{name}.jtidy.script
BuildArch:        noarch
Patch: jtidy-1.0-alt-cleanup-pom-deps.patch

BuildRequires: jpackage-utils
BuildRequires: ant

Requires: jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

Obsoletes:        %{name}-scripts < 2:1.0-0.5
Source44: import.info

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty printer. 
Like its non-Java cousin, JTidy can be used as a tool for cleaning up malformed 
and faulty HTML. In addition, JTidy provides a DOM interface to the document 
that is being processed, which effectively makes you able to use JTidy as a DOM 
parser for real-world HTML.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch -p0

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -Dant.build.javac.source=1.4

%install

# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{jtidyversion}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap net.sf.jtidy %{name} %{version} JPP %{name}
%add_to_maven_depmap jtidy %{name} %{version} JPP %{name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# shell script
mkdir -p %{buildroot}%{_bindir}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# ant.d
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
jtidy
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*


%files
%doc LICENSE.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%attr(755, root, root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt1_0.10.20100930svn1125jpp6
- new version

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 2:8.0-alt1_0.813.1jpp5
- jpackage 5.0

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 2:1.0-alt2.2_0.2.r7dev.1jpp5
- rebuild with java 5

