%define _unpackaged_files_terminate_build 1

Name: aiosmtpd
Version: 1.4.2
Release: alt1

Summary: A reimplementation of the Python stdlib smtpd.py based on asyncio.

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/aio-libs/aiosmtpd


# Source-url: https://github.com/aio-libs/aiosmtpd/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

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
%python3_prune
rm -rfv %buildroot/%python3_sitelibdir/%name/{qa,testing,docs}

%files
%doc README.* %name/docs
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Thu Apr 07 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version (1.4.2) with rpmgs script (ALT bug 42360)

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
