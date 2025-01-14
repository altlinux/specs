Name: climage
Version: 0.2.0
Release: alt1

Summary: Convert images to beautiful ANSI escape codes for display in command line interfaces.
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/climage/
Vcs: https://github.com/pnappa/CLImage

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires:  python3-module-setuptools python3-module-wheel

%add_python3_path %python3_sitelibdir/%name/

%description
%summary.

%package -n python3-module-%name
Group:  Development/Python3
Summary: Convert images to beautiful ANSI escape codes for display in command line interfaces.

%description -n python3-module-%name
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%name
%doc LICENSE *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Tue Jan 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.