Name: python3-module-isal
Version: 1.7.1
Release: alt1

Summary: Python bindings for the ISA-L library
License: PSF-2.0
Group: Development/Python
Url: https://github.com/pycompression/python-isal

Source0: %name-%version-%release.tar

BuildRequires: libisal-devel
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(test)

%description
%summary

%prep
%setup
echo '__version__ = "%version"' > src/isal/_version.py
sed -ri -e '/import\s+versioningit/d' \
	-e '/^\s+version=/ s,=.+$,="%version"\,,' setup.py

%build
export PYTHON_ISAL_LINK_DYNAMIC=1
%pyproject_build

%install
%pyproject_install

%check
%ifarch aarch64 x86_64 ppc64le
%pyproject_run_pytest tests
%endif

%files
%python3_sitelibdir/isal
%python3_sitelibdir/isal-%version.dist-info

%changelog
* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.0-alt1
- 1.7.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.1-alt1
- 1.6.1 released
