%define _unpackaged_files_terminate_build 1
%define oname flufl.i18n

Name: python3-module-%oname
Version: 2.0.1
Release: alt2

Summary: A high level API for internationalization.
License: Apache-2.0
Group: Development/Python3
Url: https://gitlab.com/warsaw/flufl.i18n
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-atpublic

Requires: python3-module-atpublic
%add_python3_req_skip flufl


%description
This package provides a high level, convenient API for managing
internationalization translation contexts in Python application. There is a
simple API for single-context applications, such as command line scripts which
only need to translate into one language during the entire course of their
execution. There is a more flexible, but still convenient API for multi-context
applications, such as servers, which may need to switch language contexts for
different tasks.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.*
%python3_sitelibdir/*


%changelog
* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
