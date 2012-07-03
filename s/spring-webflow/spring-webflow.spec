Name: spring-webflow
Version: 1.0.5
Summary: Spring Webflow
Epoch: 0
License: Apache License 2.0
Url: http://www.springsource.org/webflow
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: concurrent
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils
Requires: myfaces
Requires: portlet_1_0_api
Requires: spring2-beans
Requires: spring2-context
Requires: spring2-context-support
Requires: spring2-core
Requires: spring2-web
Requires: spring2-webmvc
Requires: spring2-webmvc-portlet
Requires: spring2-webmvc-struts
Requires: struts

BuildArch: noarch
Group: Development/Java
Release: alt4_0.1jpp
Source: spring-webflow-1.0.5-1.jpp5.cpio

%description
Spring Web Flow is the project in the Spring Portfolio that
focuses on providing the infrastructure for building and
running rich web applications. As a Spring project, Web
Flow builds on the Spring Web MVC framework to provide:
* A domain-specific-language for defining reusable controller modules called flows
* An advanced controller engine for managing conversational state
* First-class support for using Ajax to construct rich user interfaces
* First-class support for using JavaServerFaces with Spring

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

%post

echo -e "<dependencies>\n" > /etc/maven/maven2-depmap.xml
if [ -d /etc/maven/fragments ] && [ -n "`find /etc/maven/fragments -type f`" ]; then
cat /etc/maven/fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml

%postun

echo -e "<dependencies>\n" > /etc/maven/maven2-depmap.xml
if [ -d /etc/maven/fragments ] && [ -n "`find /etc/maven/fragments -type f`" ]; then
cat /etc/maven/fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml


%files -f %name-list

%changelog
* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt4_0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

