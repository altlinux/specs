%define _unpackaged_files_terminate_build 1
%define oname pkgconfig

%def_with check

Name: python3-module-%oname
Version: 1.5.5
Release: alt1

Summary: Interface Python with pkg-config
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pkgconfig/
BuildArch: noarch

# https://github.com/matze/pkgconfig.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry.core)

%if_with check
BuildRequires: /usr/bin/pkg-config
# cat data/fake-openssl.pc | grep Requires
BuildRequires: libssl-devel

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
%oname is a Python module to interface with the pkg-config command line tool
for Python.

%prep
%setup

%build
# generate setup.py for legacy builder
%__python3 - <<-'EOF'
from pathlib import Path

from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder


poetry = Factory().create_poetry(Path(".").resolve(), with_dev=False)
builder = SdistBuilder(poetry)

setup = builder.build_setup()

with open("setup.py", "wb") as f:
    f.write(setup)
EOF
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false --develop

%files
%doc *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 25 2022 Stanislav Levin <slev@altlinux.org> 1.5.5-alt1
- 1.2.2 -> 1.5.5.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141212
- Initial build for Sisyphus

