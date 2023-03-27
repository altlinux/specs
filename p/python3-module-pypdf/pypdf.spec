%define modulename pypdf

# Relies on a lot of network
%def_without check

Name: python3-module-%modulename
Version: 3.7.0
Release: alt1

Summary: A Pure-Python library built as a PDF toolkit

Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/pypdf

BuildArch: noarch
Source: %name-%version.tar
Vcs: https://github.com/py-pdf/pypdf

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%description
A Pure-Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encrypting and decrypting PDF files.

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Mon Mar 27 2023 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0.

* Mon Mar 20 2023 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.

* Mon Mar 13 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.2-alt1
- Automatically updated to 3.5.2.

* Tue Mar 07 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.1-alt1
- Automatically updated to 3.5.1.

* Mon Feb 27 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Mon Feb 13 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt1
- Automatically updated to 3.4.1.

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.12-alt1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.12-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt1
- Initial build for Sisyphus

