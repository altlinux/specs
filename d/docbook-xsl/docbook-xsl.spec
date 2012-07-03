Name: docbook-xsl
Version: 1.75.2
Summary: XSL stylesheets for transforming DocBook XML document instances
Epoch: 0
License: LGPLv2+
Url: http://www.jboss.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: docbook-maven

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: docbook-xsl-1.75.2-2.jpp6.cpio

%description
These are XSL stylesheets for transforming DocBook XML document instances into
various output formats.

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
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.75.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

