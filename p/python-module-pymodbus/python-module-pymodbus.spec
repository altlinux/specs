Name: python-module-pymodbus
Version: 1.2.0
Release: alt1
Summary: A Modbus Protocol Stack in Python

Group: Development/Python
License: BSD
URL: https://github.com/bashwork/pymodbus
Source0: %name-%version.tar
# reverse upstream patch c44bc2e3b71b37bf5e330f7ae7789a62f2c605cb
# to avoid packaging ez_setup
Patch0: 0001-Fixing-issue-60-on-google-code-including-ez_setup.patch
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
#Requires: python-twisted >= 12.2.0
#Requires: python-nose >= 1.2.1
#Requires: pyserial >= 2.6

%description
Pymodbus is a full Modbus protocol implementation using twisted for its
asynchronous communications core.

The library currently supports the following:

Client Features

    * Full read/write protocol on discrete and register
    * Most of the extended protocol (diagnostic/file/pipe/setting/information)
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary
    * asynchronous(powered by twisted) and synchronous versions
    * Payload builder/decoder utilities

Server Features

    * Can function as a fully implemented Modbus server
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary
    * asynchronous(powered by twisted) and synchronous versions
    * Full server control context (device information, counters, etc)
    * A number of backing contexts (database, redis, a slave device)

%prep
%setup
%patch0 -p1 -R

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/test

%files
%python_sitelibdir/*

%changelog
* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt1
- Initial build for ALT (based on 1.2.0-5.fc26.src)

