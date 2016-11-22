# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global checkout 20130104cvs
Name:           rachota
Version:        2.3
Release:        alt1_11.20130104cvsjpp8
Summary:        Straightforward timetracking

Group:          Development/Java
License:        CDDL
URL:            http://rachota.sourceforge.net/en/index.html
## Upstream does not provide any source tarball.
## We have to check them out via cvs.
# cvs -z3 -d:pserver:anonymous@rachota.cvs.sourceforge.net:/cvsroot/rachota co -r release23 -D 2012-01-10 -P rachota
# tar caf rachota.tar.gz rachota
Source0:        %{name}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png

# Fix doclint issues that make the build fail with java 8
Patch0:         doclint.patch

BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java


BuildRequires:  ant

BuildRequires:  desktop-file-utils

Requires: javapackages-tools rpm-build-java

Source44: import.info

%description
Rachota is a portable application for timetracking different projects. It runs
everywhere. It displays time data in diagram form, creates customized reports
and invoices or analyses measured data and suggests hints to improve user's
time usage. The totally portable yet personal timetracker. 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
ANT_OPTS="-Dfile.encoding=UTF-8" ant

%install

install -D dist/Rachota.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/Rachota.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%jpackage_script org.cesilko.rachota.gui.MainWindow "" "" %{name} %{name} true

install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf



%files
%{_javadir}/*.jar
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_11.20130104cvsjpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_10.20130104cvsjpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_7.20130104cvsjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_6.20130104cvsjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5.20130104cvsjpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_4.20120110cvsjpp7
- new version

