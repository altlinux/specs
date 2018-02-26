Name: axis2-saaj-1.1-api
Version: 1.2
Summary: SAAJ 1.1 API from axis2
Epoch: 0
License: Apache Software License
Url: http://ws.apache.org/axis2/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: saaj_1_1_api
Provides: saaj_api
Requires: /bin/sh
Requires: /bin/sh
Requires: axis2-poms
Requires: javamail_1_4_api
Requires: xml-commons-jaxp-1.3-apis

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: axis2-saaj-1.1-api-1.2-2jpp.cpio

%description
SAAJ 1.1 API from axis2.

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

%preun
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove saaj_1_1_api /usr/share/java/axis2-saaj-1.1-api.jar
    /usr/sbin/update-alternatives --remove saaj_api /usr/share/java/axis2-saaj-1.1-api.jar
fi

%post
/usr/sbin/update-alternatives --install /usr/share/java/saaj_1_1_api.jar saaj_1_1_api /usr/share/java/axis2-saaj-1.1-api.jar 10100
/usr/sbin/update-alternatives --install /usr/share/java/saaj_api.jar saaj_api /usr/share/java/axis2-saaj-1.1-api.jar 10100


%files -f %name-list

%changelog
* Wed Oct 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap

