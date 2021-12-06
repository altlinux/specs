Name: python3-module-sagenb-export
Version: 3.3
Release: alt1.gitcb591d4

Summary: Python interface for convert SageNB Notebooks
Group: Development/Python3
License: GPL-3.0+
Url: https://github.com/vbraun/ExportSageNB.git

Source: %url/archive/%version/ExportSageNB-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildRequires: python3-module-nbformat python3-module-notebook

%description
This is a tool to convert SageNB notebooks to other formats,
in particular IPython/Jupyter notebooks.

%package tests
Summary: Tests for sagenb_export
Group: Development/Python3

%description tests
This is a tool to convert SageNB notebooks to other formats,
in particular IPython/Jupyter notebooks.

This package contains tests.

%prep
%setup -n ExportSageNB-%version

%build
%python3_build

%install
%python3_install

mv -f %buildroot%python3_sitelibdir_noarch/test/ %buildroot%python3_sitelibdir_noarch/sagenb_export/

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch/sagenb_export/test/
%__python3 setup.py test

%files
%doc README.md LICENSE
%_bindir/sagenb-export
%python3_sitelibdir_noarch/sagenb_export*
%exclude %python3_sitelibdir_noarch/sagenb_export/test/

%files tests
%python3_sitelibdir_noarch/sagenb_export/test/

%changelog
* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 3.3-alt1.gitcb591d4
- Initial build for ALT Sisyphus.
- Built as require for sagemath.

