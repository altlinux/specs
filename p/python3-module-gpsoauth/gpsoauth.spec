Name: python3-module-gpsoauth
Version: 1.0.0
Release: alt1

Summary: Python API for google play services oauth
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gpsoauth/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3(poetry)
BuildRequires: python3(requests) python3(Crypto) python3(pytest)

%description
%summary

%prep
%setup
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

%build
%python3_build

%install
%python3_install

%check
py.test3 tests/test_all.py 

%files
%python3_sitelibdir/gpsoauth
%python3_sitelibdir/gpsoauth-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- initial
