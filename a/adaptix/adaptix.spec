Name:  adaptix
Version: 3.0.0
Release: alt1

Summary: An extremely flexible and configurable data model conversion library.
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/adaptix/
Vcs: https://github.com/reagento/adaptix

BuildArch: noarch

Source0: %name-%version.tar
Source1: release_data.tar

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires:  python3-module-setuptools python3-module-wheel

%add_python3_path %python3_sitelibdir/%name/

%description
%summary.

%package -n python3-module-%name
Group:  Development/Python3
Summary: An extremely flexible and configurable data model conversion library.

%description -n python3-module-%name
%summary.

%prep
%setup
tar -xf %SOURCE1 -C benchmarks/

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%name
%doc LICENSE *.md
%python3_sitelibdir/%name/
#%python3_sitelibdir/%{pyproject_distinfo %name}
%python3_sitelibdir/adaptix-3.0.0b9.dist-info/

%changelog
* Tue Jan 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt1
- Initial build (version 3.0.0b9).