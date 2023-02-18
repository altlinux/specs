%define _unpackaged_files_terminate_build 1

%define oname mdit-plugins
%define mname mdit_py_plugins

Name: python3-module-%oname
Version: 0.3.4
Release: alt1
Summary: Collection of core plugins for markdown-it-py 
License: MIT
Group: Development/Python3
Url: https://mdit-py-plugins.readthedocs.io/

BuildArch: noarch

# https://github.com/executablebooks/mdit-py-plugins
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit
BuildRequires: /usr/bin/py.test3
BuildRequires: python3(markdown_it)
BuildRequires: python3-module-pytest-regressions
BuildRequires: python3-module-pytest-datadir

%description
Collection of core plugins for markdown-it-py.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv \
	--deselect=tests/test_amsmath.py::test_plugin_parse \
	--deselect=tests/test_colon_fence.py::test_plugin_parse \
	--deselect=tests/test_container.py::test_plugin_parse \
	--deselect=tests/test_container.py::test_no_new_line_issue \
	--deselect=tests/test_deflist.py::test_plugin_parse \
	--deselect=tests/test_dollarmath.py::test_plugin_parse \
	--deselect=tests/test_substitution.py::test_tokens \
	--deselect=tests/test_tasklists.py::test_plugin_parse \
	--deselect=tests/test_texmath.py::test_plugin_parse \
	%nil

%files
%doc LICENSE
%doc README.md
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version.dist-info

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.4-alt1
- Automatically updated to 0.3.4.

* Fri Dec 09 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1
- Automatically updated to 0.3.3.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Automatically updated to 0.3.1.

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Automatically updated to 0.3.0.

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.8-alt1
- Initial build for ALT.
