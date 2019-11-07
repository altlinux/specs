%def_without python3
%define oname zerorpc-python

Name: python3-module-zerorpc
Version: 0.6.1
Release: alt2

Summary: An easy to use, intuitive, and cross-language RPC

License: MIT
Group: Development/Python3
Url: http://www.zerorpc.io/
# Source-url: https://github.com/0rpc/zerorpc-python/archive/v%version.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3


%description
Zerorpc is a light-weight, reliable and language-agnostic library
for distributed communication between server-side processes.
It builds on top of ZeroMQ and MessagePack.
Support for streamed responses - similar to python generators -
makes zerorpc more than a typical RPC engine. Built-in heartbeats
and timeouts detect and recover from failed requests. Introspective
capabilities, first-class exceptions and the command-line utility
make debugging easy.

%prep
%setup -n %oname-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -type f \( -name '*.py' -o -name 'zerorpc' \))

%build
%python3_build_debug

%install
%python3_install

%files
%doc LICENSE README* doc
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- disable python2

* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1

* Sun Oct 18 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu Aug 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
