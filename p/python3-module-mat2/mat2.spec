%define pypi_name mat2

Name:    python3-module-%pypi_name
Version: 0.13.5
Release: alt1.d61fb7f7

License: LGPL-3.0
Group:   Development/Python3
URL:	 https://pypi.org/project/mat2
VCS:	 https://0xacab.org/jvoisin/mat2.git

Summary: Metadata and privacy
Summary(ru_RU.UTF-8): Метаданные и конфиденциальность

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
This is precisely the job of mat2: getting rid, as much as possible, of
metadata.

%description -l ru_RU.UTF8
Основная задача mat2: избавиться, насколько это возможно, от метаданных.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%pypi_name
%_datadir/man/man1/%pypi_name.1.xz
%python3_sitelibdir/lib%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc *.md LICENSE

%changelog
* Sat Nov 23 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt1.d61fb7f7
- Initial build for Sisyphus.
