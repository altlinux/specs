%def_without python3
%define oname zerorpc-python

Name: python-module-zerorpc
Version: 0.6.1
Release: alt1

Summary: An easy to use, intuitive, and cross-language RPC

License: MIT
Group: Development/Python
Url: http://www.zerorpc.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/0rpc/zerorpc-python/archive/v%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-module-distribute

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

%if_with python3
%package -n python3-module-zerorpc
Summary: ZeroRPC for Python 3
Group: Development/Python

%description -n python3-module-zerorpc
Zerorpc is a light-weight, reliable and language-agnostic library
for distributed communication between server-side processes.
It builds on top of ZeroMQ and MessagePack.
Support for streamed responses - similar to python generators -
makes zerorpc more than a typical RPC engine. Built-in heartbeats
and timeouts detect and recover from failed requests. Introspective
capabilities, first-class exceptions and the command-line utility
make debugging easy.
%endif

%prep
%setup -n %oname-%version

%if_with python3
mkdir -p ../BUILD3
cp -fR . ../BUILD3
%endif

%build
%python_build_debug

%if_with python3
pushd ../BUILD3
%python3_build_debug
popd
%endif

%install
%python_install
rm -rf build

%if_with python3
pushd ../BUILD3
%python3_install
popd
%endif

%files
%doc LICENSE README* doc
%_bindir/zerorpc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-zerorpc
%doc LICENSE README* doc
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1

* Sun Oct 18 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu Aug 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
