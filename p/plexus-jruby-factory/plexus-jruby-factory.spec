Name: plexus-jruby-factory
Version: 1.0
Summary: Plexus JRuby Creator
Epoch: 0
License: Apache Software License
Url: http://plexus.codehaus.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: jpackage-utils
Requires: jpackage-utils
Requires: jruby
Requires: plexus-classworlds

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: plexus-jruby-factory-1.0-0.b3.1jpp.cpio

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

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
* Sat Mar 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2jpp
bootstrap; see deps.notes for details

