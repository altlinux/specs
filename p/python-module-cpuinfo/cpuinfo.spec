%define _unpackaged_files_terminate_build 1
%define oname cpuinfo

Name: python-module-%oname
Version: 7.0.0
Release: alt1

Summary: Get CPU info with pure Python 2 & 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/py-cpuinfo
BuildArch: noarch

Source: py-%oname-%version.tar

BuildRequires: python-devel python-module-setuptools
# /proc is needed for tests
BuildRequires: /proc


%description
Py-cpuinfo gets CPU info with pure Python.
Py-cpuinfo should work without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.

%prep
%setup -n py-%oname-%version

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test

%files
%doc README.md
%exclude %_bindir/*
%python_sitelibdir/*


%changelog
* Wed Aug 12 2020 Ivan A. Melnikov <iv@altlinux.org> 7.0.0-alt1
- 7.0.0

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt3
- Binary file excluded (conflict with module on py3).

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt2
- Rebuild with new setuptools
- removal python3 build.

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
