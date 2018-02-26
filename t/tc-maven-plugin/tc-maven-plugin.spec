Name: tc-maven-plugin
Version: 1.6.0
Summary: Terracotta Maven Plugin
Epoch: 0
License: Terracotta Public License
Url: http://forge.terracotta.org/releases/projects/tc-maven-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tc-maven-plugin-1.6.0-1.jpp6.cpio

%description
The Maven Plugin for Terracotta provides tight integration
between Terracotta DSO and Maven. It makes it really easy
to run and test applications with Terracotta.
For example, using the Maven Plugin, your project can define
the main class to launch, and using a simple maven command,
can easily launch all of the required Java VMs including the
Terracotta Server to run and test your clustered project.

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
* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt0.1jpp
- bootstrap for jetty6

