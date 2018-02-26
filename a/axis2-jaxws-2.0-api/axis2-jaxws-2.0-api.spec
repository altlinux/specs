Name: axis2-jaxws-2.0-api
Version: 1.2
Summary: JAX-WS 2.0 API from axis2
Epoch: 0
License: Apache Software License
Url: http://ws.apache.org/axis2/
Provides: jaxws_2_0_api
Provides: jaxws_api
Requires: /bin/sh
Requires: /bin/sh
Requires: axis2-poms
Requires: axis2-saaj-1.1-api
Requires: jakarta-commons-logging
Requires: jaxb_2_1_api

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: axis2-jaxws-2.0-api-1.2-2jpp.cpio

%description
JAX-WS 2.0 API from axis2.

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
    /usr/sbin/update-alternatives --remove jaxws_2_0_api /usr/share/java/axis2-jaxws-2.0-api.jar
    /usr/sbin/update-alternatives --remove jaxws_api /usr/share/java/axis2-jaxws-2.0-api.jar
fi

%post
/usr/sbin/update-alternatives --install /usr/share/java/jaxws_2_0_api.jar jaxws_2_0_api /usr/share/java/axis2-jaxws-2.0-api.jar 20000
/usr/sbin/update-alternatives --install /usr/share/java/jaxws_api.jar jaxws_api /usr/share/java/axis2-jaxws-2.0-api.jar 20000


%files -f %name-list

%changelog
* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap

