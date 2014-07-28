# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jBCrypt
Version:        0.3
Release:        alt1_8jpp7
Summary:        Strong password hashing for Java

Group:          Development/Java
License:        ISC
URL:            http://www.mindrot.org/projects/jBCrypt/
Source0:        http://www.mindrot.org/files/jBCrypt/jBCrypt-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       jpackage-utils
Source44: import.info

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 


%prep
%setup -q


%build
javac BCrypt.java
jar cvf jBCrypt.jar BCrypt.class

# compile test cases too
javac -encoding UTF-8 -cp %{_javadir}/junit.jar:jBCrypt.jar TestBCrypt.java
jar cvf jBCrypt-test.jar TestBCrypt.class


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp jBCrypt.jar $RPM_BUILD_ROOT%{_javadir}/jBCrypt.jar


%check
java -cp %{_javadir}/junit.jar:jBCrypt.jar:jBCrypt-test.jar TestBCrypt


%files
%doc LICENSE README
%{_javadir}/%{name}.jar


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7jpp7
- new version

