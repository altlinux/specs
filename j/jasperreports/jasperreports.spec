Epoch: 0
Name: jasperreports
Version: 4.0.2
Summary: Report-generating tool
License: LGPLv3+
Url: http://jasperforge.org/projects/jasperreports/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: apache-commons-beanutils
Requires: apache-commons-codec
Requires: apache-commons-collections
Requires: apache-commons-digester
Requires: apache-commons-javaflow
Requires: apache-commons-logging
Requires: batik
Requires: bcel
Requires: ecj
Requires: geronimo-saaj
Requires: hsqldb
Requires: iText
Requires: java
Requires: jcommon
Requires: jfreechart
Requires: jpackage-utils
#Requires: springframework
#Requires: springframework-beans
Requires: tomcat-servlet-3.0-api

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jasperreports-4.0.2-3.fc18.cpio

%description
JasperReports is a powerful open source
report-generating tool that has the ability
to deliver rich content onto the screen, to
the printer or into PDF, HTML, XLS, CSV and
XML files. It is entirely written in Java
and can be used in a variety of Java enabled
applications, including J2EE or Web
Its main purpose is to help creating page
oriented, ready to print documents in a
simple and flexible manner.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

