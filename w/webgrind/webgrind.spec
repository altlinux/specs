Name: webgrind
Version: 1.9.3
Release: alt1

Summary: Xdebug Profiling Web Frontend in PHP
License: BSD License
Group: System/Servers
Url: https://github.com/jokkedk/webgrind

BuildArch: noarch

# Source-url: https://github.com/jokkedk/webgrind/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-apache2 rpm-macros-webserver-common rpm-build-python3
BuildRequires: python-tools-2to3

AutoReq:yes,nomingw32,nomingw64

Requires: graphviz


%description
Webgrind is a Xdebug profiling web frontend in PHP.
It implements a subset of the features of kcachegrind and installs in seconds and works on all platforms.

%package preprocessor
Summary: binary preprocessor for Xdebug Profiling Web Frontend in PHP
Group: System/Servers
Requires: %name = %EVR

%description preprocessor
Binary version of the preprocessor (for faster preprocessing)
for Xdebug Profiling Web Frontend in PHP.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%if 0
# TODO arch subpackage
%make_build
%endif

%install
mkdir -p %buildroot%webserver_webappsdir
cp -a . %buildroot%webserver_webappsdir/%name
rm -v %buildroot%webserver_webappsdir/%name/{.gitattributes,.github/workflows/docker-image.yml}

%files
%doc README.md
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*

%if 0
%files preprocessor
%webserver_webappsdir/%name/bin/
%endif


%changelog
* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- new version 1.9.3 (with rpmrb script)

* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0-alt2
- Porting to python3.

* Fri Dec 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus

