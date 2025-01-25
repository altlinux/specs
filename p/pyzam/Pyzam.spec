Name: pyzam
Version: 0.12.3
Release: alt1

Summary: Recognize and Visualise Songs in Your CLI
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/pyzam
Vcs: https://github.com/lukafilipxvic/Pyzam

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-climage

%description
Pyzam is a free CLI music recognition tool for audio and mixtapes in Python.

%package -n python3-module-%name
Group:  Development/Python3
Summary: Recognize and Visualise Songs in Your CLI

%description -n python3-module-%name
Pyzam is a free CLI music recognition tool for audio and mixtapes in Python.

%prep
%setup

subst "s|import climage|import climage.__main__|" pyzam/identify.py

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name

%files -n python3-module-%name
%doc LICENSE.txt *.md
%python3_sitelibdir/%name/
%python3_sitelibdir/pyzam-0.12.2.dist-info/

%changelog
* Sat Jan 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.12.3-alt1
- Initial build for Sisyphus.
