%filter_from_requires /^libjpeg.so.62.LIBJPEG_6.2/d
%set_verify_elf_method relaxed
Name: java-1.7.0-openjdk-bootstrap-aarch64
Version: 1.7.0.181
Summary: OpenJDK Runtime Environment
License: ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv1.1 and MPLv2.0 and Public Domain and W3C and zlib
Url: http://openjdk.java.net/
Packager: Igor Vlasenko <viy@altlinux.ru>
ExclusiveArch: aarch64
Group: Development/Java
Release: alt0.1jpp
Source: java-1.7.0-openjdk-aarch64.tar.xz

Provides: java = 1.7.0
Provides: java-1.7.0 = 1.7.0.001
Provides: java-1.7.0-openjdk = 1.7.0.001
Provides: java-fonts = 1.7.0.001
Provides: java-openjdk = 1.7.0.001
Provides: jre = 1.7.0
Provides: jre-1.7.0 = 1.7.0.001
Provides: jre-1.7.0-openjdk = 1.7.0.001
Provides: jre-openjdk = 1.7.0.001
Provides: java-1.7.0-devel = 1.7.0.001
Provides: java-1.7.0-openjdk-devel = 1.7.0.001
Provides: java-devel = 1.7.0
Provides: java-devel-openjdk = 1.7.0.001
Provides: java-sdk = 1.7.0
Provides: java-sdk-1.7.0 = 1.7.0.001
Provides: java-sdk-1.7.0-openjdk = 1.7.0.001
Provides: java-sdk-openjdk = 1.7.0.001
Provides: java-1.7.0-headless = 1.7.0.001
Provides: java-1.7.0-openjdk-headless = 1.7.0.001
Provides: java-headless = 1.7.0
Provides: java-openjdk-headless = 1.7.0.001
Provides: jre-1.7.0-headless = 1.7.0.001
Provides: jre-1.7.0-openjdk-headless = 1.7.0.001
Provides: jre-headless = 1.7.0
Provides: jre-openjdk-headless = 1.7.0.001

BuildRequires: chrpath patchelf 
BuildRequires: libcups-devel fontconfig-devel libfreetype-devel libgio-devel libGConf-devel libpng-devel libX11-devel libXext-devel libjpeg-devel libgif-devel libpcsclite-devel libalsa-devel libXrender-devel  libXcomposite-devel libXtst-devel libXi-devel libkrb5-devel libcairo-devel libpango-devel libgtk+2-devel libatk-devel libnss-devel


Requires: ca-certificates-java
Requires: jpackage-utils
Requires: libjpeg
Requires: tzdata-java



%description
The OpenJDK runtime environment.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
tar xJf %{SOURCE0}

%build
tar tJf %{SOURCE0} | sed -e 's,^\.,,' > %name-list

for i in \
    usr/lib/jvm/java-*.aarch64/jre/bin/* \
    usr/lib/jvm/java-*.aarch64/jre-abrt/bin/* \
    usr/lib/jvm/java-*.aarch64/bin/* \
    usr/lib/jvm/java-*.aarch64/lib/jexec \
    usr/lib/jvm/java-*.aarch64/jre/lib/jexec \
	; do
    case `file $i` in
	*ELF*)
	    patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 $i
	    ;;
    esac
done

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done

%files -f %name-list

%changelog
* Sun Jun 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0.181-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

