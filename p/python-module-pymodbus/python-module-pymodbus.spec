%global sum A Modbus Protocol Stack in Python
%global desc Pymodbus is a full Modbus protocol implementation using twisted for its \
asynchronous communications core. \
\
The library currently supports the following: \
\
Client Features \
\
    * Full read/write protocol on discrete and register \
    * Most of the extended protocol (diagnostic/file/pipe/setting/information) \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Payload builder/decoder utilities \
\
Server Features \
\
    * Can function as a fully implemented Modbus server \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Full server control context (device information, counters, etc) \
    * A number of backing contexts (database, redis, a slave device)

Name: python-module-pymodbus
Version: 1.5.1
Release: alt1
Summary: %{sum}

Group: Development/Python
License: BSD
URL: https://github.com/bashwork/pymodbus
Source0: %name-%version.tar
# to avoid packaging ez_setup
Patch0: pymodbus-1.4.0-remove-ez_setup.patch
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
#Requires: python-twisted >= 12.2.0
#Requires: python-nose >= 1.2.1
#Requires: pyserial >= 2.6

%description
%{desc}


%package -n python3-module-pymodbus
Group: Development/Python3
Summary: %{sum}

BuildRequires: python3-devel
BuildRequires: python3-module-distribute
#Requires: python3-module-twisted-conch python3-module-twisted-conch-gui python3-module-twisted-core python3-module-twisted-core-test python3-module-twisted-logger python3-module-twisted-names python3-module-twisted-pair python3-module-twisted-positioning python3-module-twisted-runner python3-module-twisted-web python3-module-twisted-words
#Requires: python3-module-serial >= 2.6

%description -n python3-module-pymodbus
%{desc}

%prep
%setup
%patch0 -p1

%build
%python_build
%python3_build

%install
%python_install
%python3_install

rm -rf %buildroot%python_sitelibdir/test
rm -rf %buildroot%python3_sitelibdir/test

%files -n python-module-pymodbus
%doc doc/LICENSE
%python_sitelibdir/*

%files -n python3-module-pymodbus
%doc doc/LICENSE
%python3_sitelibdir/*

%changelog
* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1
- new version (based on 1.5.1-1.fc)
- python3 support

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt1
- Initial build for ALT (based on 1.2.0-5.fc26.src)

