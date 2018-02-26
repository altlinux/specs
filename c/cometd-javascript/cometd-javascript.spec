Name: cometd-javascript
Version: 1.0.1
Summary: CometD Javascript
Epoch: 0
License: Apache Software License 2.0
Url: http://www.cometd.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: cometd-java-api
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: cometd-javascript-1.0.1-2.jpp6.cpio

%description
Cometd is a scalable HTTP-based event routing bus that uses
a Ajax Push technology pattern known as Comet. The term
'Comet' was coined by Alex Russell in his post Comet: Low
Latency Data for the Browser.
The JavaScript implementation of the Bayeux specification
and API has been totally rewritten starting from CometD
version 1.0.beta8, and further refactored since 1.0.beta9.
What is available now is a portable JavaScript
implementation with bindings for the major JavaScript
toolkits, currently Dojo and jQuery.
What this means is that the CometD Bayeux JavaScript
implementation is written in pure JavaScript with no
dependencies on the toolkits, and that the toolkit
bindings add the syntactic sugar that makes the Bayeux
APIs feel like they are native to the toolkit.

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
* Sun Oct 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt0.1jpp
- bootstrap for jetty6

