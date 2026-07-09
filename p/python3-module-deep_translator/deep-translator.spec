%define pypi_name deep_translator

Name:    python3-module-%pypi_name
Version: 1.11.4
Release: alt1

License: MIT
Group:   Development/Python3

URL:	 https://pypi.org/project/deep-translator
VCS:	 https://github.com/nidhaloff/deep-translator

Summary: Translation for humans

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core python3-module-wheel

%if_with check
BuildRequires: python3-module-requests python3(bs4)
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
A flexible FREE and UNLIMITED tool to translate between different
languages in a simple way using multiple translators.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc LICENSE

%changelog
* Thu Jul 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.11.4-alt1
- Initial build for ALT (git.fa67ada6c5)

