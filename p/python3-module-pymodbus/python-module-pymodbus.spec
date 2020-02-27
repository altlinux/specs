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

%define oname pymodbus

Name: python3-module-%oname
Version: 1.5.1
Release: alt2

Summary: %{sum}
License: BSD
Group: Development/Python3
URL: https://github.com/bashwork/pymodbus
BuildArch: noarch

Source0: %oname-%version.tar
# to avoid packaging ez_setup
Patch0: pymodbus-1.4.0-remove-ez_setup.patch

BuildRequires(pre): rpm-build-python3


%description
%{desc}

%prep
%setup -q -n %oname-%version
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/test

%files
%doc doc/LICENSE
%python3_sitelibdir/*


%changelog
* Thu Feb 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.1-alt2
- Build for python2 disabled.

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1
- new version (based on 1.5.1-1.fc)
- python3 support

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt1
- Initial build for ALT (based on 1.2.0-5.fc26.src)

