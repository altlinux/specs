Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           apache-ivy
Version:        2.3.0
Release:        alt1_1jpp7
Summary:        Java-based dependency manager

Group:          Development/Java
License:        ASL 2.0
URL:            http://ant.apache.org/ivy/
Source0:        http://www.apache.org/dist/ant/ivy/%{version}/%{name}-%{version}-src.tar.gz
BuildArch:      noarch

Provides:       ivy = %{version}-%{release}

BuildRequires:  ant
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  jsch
BuildRequires:  jakarta-oro
BuildRequires:  jpackage-utils
Requires:       jpackage-utils
Requires:       jakarta-oro
Requires:       jsch
Requires:       ant
Requires:       jakarta-commons-httpclient
Source44: import.info
AutoReqProv: yes,noosgi
Obsoletes: ivy < 2
Source45: ivy-2.2.0.pom

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%package javadoc
Summary:        API Documentation for ivy
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q

# Fix messed-up encodings
for F in RELEASE_NOTES README LICENSE NOTICE CHANGES.txt
do
        sed 's/\r//' $F |iconv -f iso8859-1 -t utf8 >$F.utf8
        touch -r $F $F.utf8
        mv $F.utf8 $F
done
rm -fr src/java/org/apache/ivy/plugins/signer/bouncycastle

%build
# Remove prebuilt documentation
rm -rf doc build/doc

# How to properly disable a plugin?
# we disable vfs plugin since commons-vfs is not available
rm -rf src/java/org/apache/ivy/plugins/repository/vfs \
        src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
sed '/vfs.*=.*org.apache.ivy.plugins.resolver.VfsResolver/d' -i \
        src/java/org/apache/ivy/core/settings/typedef.properties

# Craft class path
mkdir -p lib
build-jar-repository lib ant jakarta-commons-httpclient jakarta-oro jsch 

# Build
ant /localivy /offline -Dtarget.ivy.bundle.version=%{version} -Dtarget.ivy.bundle.version.qualifier= -Dtarget.ivy.version=%{version} jar javadoc


%install
# Code
install -d $RPM_BUILD_ROOT%{_javadir}
install -p -m644 build/artifact/jars/ivy.jar $RPM_BUILD_ROOT%{_javadir}/ivy.jar

# API Documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/doc/reports/api/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "ivy" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}
# poms
mkdir -p %{buildroot}%_mavenpomdir
cp -p %{SOURCE45} %{buildroot}%_mavenpomdir/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ivy ivy %{version} JPP %{name}
# jpp symlink
ln -s ivy.jar %buildroot%_javadir/%{name}.jar


%files
%{_javadir}/*
%{_sysconfdir}/ant.d/%{name}
%doc RELEASE_NOTES CHANGES.txt LICENSE NOTICE README
# jpp compat
%_mavenpomdir/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%_javadir/%{name}.jar


%files javadoc
%{_javadocdir}/*
%doc LICENSE

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_5jpp7
- fc release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_1jpp6
- build with new commons-vfs2

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_1jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

