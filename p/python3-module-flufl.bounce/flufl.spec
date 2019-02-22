%define _unpackaged_files_terminate_build 1
%define oname flufl.bounce

Name: python3-module-%oname
Version: 3.0
Release: alt2

Summary: Email bounce detectors.
License: Apache-2.0
Group: Development/Python3
Url: https://gitlab.com/warsaw/flufl.bounce
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-atpublic
BuildRequires: python3-module-zope.interface

Requires: python3-module-atpublic
%add_python3_req_skip flufl


%description
The flufl.bounce library provides a set of heuristics and an API for detecting
the original bouncing email addresses from a bounce message. Many formats found
in the wild are supported, as are VERP and RFC 3464 (DSN).

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
* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0-alt2
- Broken dependencies fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0-alt1
- Initial build for Sisyphus
