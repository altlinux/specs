Name: docbook-maven
Version: 5.0
Summary: Java support for Docbook
Epoch: 0
License: LGPLv2+
Url: http://www.jboss.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: docbook-maven-5.0-2.jpp6.cpio

%description
Java support for Docbook.

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
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

