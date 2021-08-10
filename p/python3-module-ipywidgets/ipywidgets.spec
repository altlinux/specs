%define _unpackaged_files_terminate_build 1

%define oname ipywidgets

Name: python3-module-%oname
Version: 7.6.3
Release: alt1
Summary: Interactive Widgets for the Jupyter Notebook
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jupyter-widgets/ipywidgets

BuildArch: noarch

# https://github.com/jupyter-widgets/ipywidgets.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
ipywidgets, also known as jupyter-widgets or simply widgets,
are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

Notebooks come alive when interactive widgets are used.
Users gain control of their data and can visualize changes in the data.

Learning becomes an immersive, fun experience.
Researchers can easily see how changing inputs to a model impact the results.
We hope you will add ipywidgets to your notebooks,
and we're here to help you get started.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README.md CONTRIBUTING.md
%python3_sitelibdir/%oname-%version-py*.egg-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/widgets/tests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/widgets/tests

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.3-alt1
- Initial build for ALT.
