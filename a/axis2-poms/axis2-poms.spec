Name: axis2-poms
Version: 1.2
Summary: Poms and depmap frags for axis2
Epoch: 0
License: Apache Software License
Url: http://ws.apache.org/axis2/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: axis2-poms-1.2-2jpp.cpio

%description
Poms and depmap frags for axis2.

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
* Wed Oct 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap

