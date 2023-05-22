%global pypi_name jsonpatch
%global github_name python-json-patch

Name: python3-module-%pypi_name
Version: 1.32
Release: alt1

Summary: Applying JSON Patches in Python
License: BSD
Group: Development/Python3
Url: https://github.com/stefankoegl/%github_name
BuildArch: noarch

# Source0-url: https://github.com/stefankoegl/python-json-patch/archive/refs/tags/v%version.tar.gz
Source0: %pypi_name-%version.tar

BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-module-jsonpointer >= 1.9


%description
Library to apply JSON Patches according to RFC 6902.

%prep
%setup -q -n %pypi_name-%version

%build
export LC_ALL=en_US.UTF-8
%python3_build

%install
%python3_install

%check
%__python3 tests.py

%files
%doc README.md COPYING
%_bindir/jsondiff
%_bindir/jsonpatch
%python3_sitelibdir/*


%changelog
* Mon May 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt1
- new version 1.32 (with rpmrb script)

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.23-alt2
- Build for python2 disabled.

* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.23-alt1
- 1.23

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9-alt1.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-3.fc21.src)
