%define _unpackaged_files_terminate_build 1

Name: aiosmtpd
Version: 1.2.1
Release: alt1

Summary: A reimplementation of the Python stdlib smtpd.py based on asyncio.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/aio-libs/aiosmtpd
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel

Requires: python3-module-%name = %EVR


%description
This is a server for SMTP and related protocols, similar in utility to the
standard library's smtpd.py module, but rewritten to be based on asyncio
for Python 3.

%package -n python3-module-%name
Summary: A reimplementation of the Python stdlib smtpd.py based on asyncio.
Group: Development/Python3
BuildArch: noarch

BuildRequires: python3-module-atpublic

Requires: python3-module-atpublic

%description -n python3-module-%name
This is a server for SMTP and related protocols, similar in utility to the
standard library's smtpd.py module, but rewritten to be based on asyncio
for Python 3.

This package contain python modules for %name.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.* %name/docs examples
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/examples


%changelog
* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
