#%%def_disable check

Name: python3-module-hsluv
Version: 5.0.3
Release: alt1
Summary: Human-friendly HSL
License: MIT
Group: Development/Python3
URL: https://www.hsluv.org
# Source-url: https://files.pythonhosted.org/packages/source/h/hsluv/hsluv-%version.tar.gz
Source: hsluv-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_disabled check
%else
BuildRequires: pytest3
%endif

%description
%summary.

%prep
%setup -n hsluv-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%doc README.md
%python3_sitelibdir/hsluv.py
%python3_sitelibdir/__pycache__/hsluv*.pyc
%python3_sitelibdir/hsluv-%version.dist-info

%changelog
* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 5.0.3-alt1
- initial build
