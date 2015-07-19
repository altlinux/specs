%define modulename transmissionrpc

Name: python3-module-%modulename
Version: 0.11
Release: alt1

Summary: Python module that implements the Transmission bittorent client RPC protocol

Group: Development/Python
License: MIT license
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/t/%modulename/%modulename-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

#setup_python3_module %modulename

# manually removed: python-module-google python-module-mwlib python-module-oslo.config python-module-oslo.serialization python3-module-Cython0.18 python3-module-chardet python3-module-nose python3-module-pycairo python3-module-pygobject3 python3-module-zmq ruby ruby-stdlibs
# Automatically added by buildreq on Sun Jul 19 2015
# optimized out: python-base python-module-distribute python-module-oslo.i18n python-module-oslo.utils python3 python3-base python3-module-greenlet python3-module-pycparser python3-module-setuptools
BuildRequires: libdb4-devel mailcap
# python-module-cmd2

BuildRequires: python3-module-setuptools python3-module-six

%description
This is transmissionrpc. This module helps using Python to connect to a Transmission JSON-RPC service.
transmissionrpc is compatible with Transmission 1.31 and later.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- new version 0.11 (with rpmrb script)

* Tue Oct 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for ALT Linux Sisyphus
