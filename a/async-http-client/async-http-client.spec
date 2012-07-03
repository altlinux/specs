Name: async-http-client
Version: 1.6.1
Summary: Asynchronous Http Client for Java
License: ASL 2.0
Url: https://github.com/AsyncHttpClient/async-http-client
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils
Requires: netty

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: async-http-client-1.6.1-1.fc16.cpio

%description
Async Http Client library purpose is to allow Java applications to
easily execute HTTP requests and asynchronously process the HTTP
responses. The Async HTTP Client library is simple to use.

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

