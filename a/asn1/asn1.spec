Name: asn1
Version: 0.3.3
Summary: Apache ASN.1 Tools
Epoch: 0
License: Apache 2.0 License
Url: http://directory.apache.org/subprojects/asn1/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: jakarta-commons-collections
Requires: jakarta-commons-lang
#Requires: jakarta-commons-primitives11
Requires: jpackage-utils
Requires: jpackage-utils
#Requires: mina0
Requires: nlog4j
Requires: regexp

BuildArch: noarch
Group: Development/Java
Release: alt0.4jpp
Source: asn1-0.3.3-2.jpp5.cpio

%description
The ASN.1 subproject attempts to isolate the ASN.1 libraries and tools
for encoding ASN.1 in BER/DER/CER/PER encodings. The LDAP and X.500
aspects of the directory project impose the need for ASN.1 and BER
codecs.  Kerberos requires DER.  Rather than implement highly
specific and britle code for these needs we decided to separate out
the APIs and implementations used for dealing with ASN.1 codecs for any
ASN.1 defined protocol.

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
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/asn1-%version 

%changelog
* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.3.3-alt0.4jpp
- removed jakarta-commons-primitives11 dependency due to apache migration

* Sun Dec 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.3-alt0.3jpp
- removed mina0 dependency

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.3-alt0.2jpp
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for asn1
  * postclean-05-filetriggers for spec file

* Sun Mar 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.3-alt0.1jpp
- bootstrap for activemq4

