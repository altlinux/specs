%define  modulename m2r2

%def_with check

Name:    python3-module-%modulename
Version: 0.3.2
Release: alt1

Summary: Markdown to reStructuredText converter

License: MIT
Group:   Development/Python3
URL:     https://github.com/CrossNox/m2r2

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pygments
BuildRequires: python3-module-six
BuildRequires: python3-module-docutils
BuildRequires: python3-module-mistune
%endif

BuildArch: noarch

Source:  %name-%version.tar

# https://github.com/CrossNox/m2r2/pull/22
# https://github.com/CrossNox/m2r2/issues/38
Patch: 37832c0254a2413ee666a42b6906361289b50202.patch

%description
%summary

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__/%{modulename}*
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.2-alt1
- Automatically updated to 0.3.2.
- Build with check.

* Mon Jul 19 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Automatically updated to 0.3.1.

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Automatically updated to 0.2.8.

* Fri Apr 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus.
