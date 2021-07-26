%define _unpackaged_files_terminate_build 1
%define modname cloudant

Name: python3-module-%modname
Version: 2.9.0
Release: alt2

Summary: A Python library for Cloudant and CouchDB
License: Apache-2.0
Group: Development/Python3
URL: https://github.com/cloudant/python-cloudant
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
A Python library for Cloudant and CouchDB.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-py*.egg-info

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt2
- Drop python2 support.

* Wed Dec 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build
