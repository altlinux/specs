%def_without check

Name:    pdfminersix
Version: 20240706
Release: alt1

Summary: Community maintained fork of pdfminer - we fathom PDF
License: MIT
Group:   Other
URL:     https://github.com/pdfminer/pdfminer.six

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Pdfminer.six is a community maintained fork of the original PDFMiner. It is a
tool for extracting information from PDF documents. It focuses on getting and
analyzing text data. Pdfminer.six extracts the text from a page directly from
the sourcecode of the PDF. It can also be used to get the exact location, font
or color of the text.

%prep
%setup
subst 's/__VERSION__/%version/' pdfminer/__init__.py

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/*.py
%python3_sitelibdir/pdfminer
%python3_sitelibdir/*.dist-info

%changelog
* Sun Jul 07 2024 Andrey Cherepanov <cas@altlinux.org> 20240706-alt1
- New version.

* Fri Dec 29 2023 Andrey Cherepanov <cas@altlinux.org> 20231228-alt1
- New version.

* Tue May 09 2023 Andrey Cherepanov <cas@altlinux.org> 20221105-alt1
- Initial build for Sisyphus.
