%define _unpackaged_files_terminate_build 1
%define oname babelfish

%def_with check

Name: python3-module-%oname
Version: 0.6.0
Release: alt1

Summary: A module to work with countries and languages
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/babelfish/

BuildArch: noarch

# https://github.com/Diaoul/babelfish.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry.core)

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
BabelFish is a Python library to work with countries and languages.

%prep
%setup
%autopatch -p1

%build
# generate legacy setup.py, PEP517 builds are not currently supported
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
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc *.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.5 -> 0.6.0.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.5-alt4
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.5-alt3
- Updated to upstream release version 0.5.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt2.dev.git20150124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt2.dev.git20150124
- Delete unnecessary dependens

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

