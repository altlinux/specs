%define _unpackaged_files_terminate_build 1

%define oname dropbox

%def_with check

Name: python3-module-%oname
Version: 11.36.1
Release: alt1

Summary: A Python SDK for integrating with the Dropbox API v2
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dropbox/
Vcs: https://github.com/dropbox/dropbox-sdk-python

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
BuildRequires: python3-module-stone
BuildRequires: python3-module-pytest-mock
%endif

%description
%summary.

%prep
%setup

sed -i "s/__version__ = '.*'/__version__ = '%version'/" dropbox/dropbox_client.py

sed -i '/pytest-runner/d' setup.py
sed -i 's/import mock/from unittest import mock/' test/unit/test_dropbox_unit.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -vv --ignore test/integration/

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info


%changelog
* Sat Apr 15 2023 Anton Vyatkin <toni@altlinux.org> 11.36.1-alt1
- new version 11.36.1

* Thu Feb 16 2023 Anton Vyatkin <toni@altlinux.org> 11.36.0-alt1
- new version 11.36.0 (Closes #44637).

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 9.4.0-alt2
- Build fixed.

* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 9.4.0-alt1
- Initial build.

