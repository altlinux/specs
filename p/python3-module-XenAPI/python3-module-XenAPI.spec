%define modulename XenAPI

%def_with check

Name: python3-module-%modulename
Summary: DXenAPI SDK
Version: 25.28.0
Release: alt1

License: LGPL-2.1
Group: Development/Python3
URL: https://xenproject.org/projects/xapi/
VCS: https://github.com/xapi-project/xen-api
BuildArch: noarch

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-build
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: pip

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-mock
BuildRequires: python3-module-wrapt
%endif

%description
XenAPI SDK, for communication with XenServer.

%prep
%setup
sed -i 's|python -m build --wheel|python3 -m build --wheel --no-isolation|g' python3/examples/Makefile
sed -i 's|python -m build --sdist|python3 -m build --sdist --no-isolation|g' python3/examples/Makefile
sed -i 's|readme = "README.markdown"|readme = "README.md"|g' pyproject.toml
mv README.markdown README.md

%build
echo "export XAPI_VERSION=%version" > config.mk
%make_build python

%install
cd python3/examples
pip3 install --root=%buildroot --no-deps dist/*.whl

%check
cd python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -m pytest -k "not it_creates_a_tracer and not test_usb_reset_mount_umount"

%files
%doc README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 25.28.0-alt1
- Version updated to 25.28.0

* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.127.1-alt1
- Version updated to 1.127.1
- porting on python3

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial build for ALT
