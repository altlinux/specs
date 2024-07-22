%define modulename pypdf

# Relies on a lot of network
%def_without check

Name: python3-module-%modulename
Version: 4.3.1
Release: alt1

Summary: A Pure-Python library built as a PDF toolkit

Group: Development/Python3
License: BSD-3-Clause
URL: https://pypi.org/project/pypdf
VCS: https://github.com/py-pdf/pypdf

BuildArch: noarch
Source: %name-%version.tar

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
* Mon Jul 22 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Automatically updated to 4.3.1.

* Mon Jul 15 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Automatically updated to 4.3.0.

* Mon Apr 08 2024 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.

* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Tue Feb 27 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Automatically updated to 4.0.2.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 3.17.4-alt1
- Automatically updated to 3.17.4.

* Mon Oct 30 2023 Grigory Ustinov <grenka@altlinux.org> 3.17.0-alt1
- Automatically updated to 3.17.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.16.4-alt1
- Automatically updated to 3.16.4.

* Mon Oct 02 2023 Grigory Ustinov <grenka@altlinux.org> 3.16.2-alt1
- Automatically updated to 3.16.2.

* Mon Sep 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.16.1-alt1
- Automatically updated to 3.16.1.

* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 3.16.0-alt1
- Automatically updated to 3.16.0.

* Mon Sep 04 2023 Grigory Ustinov <grenka@altlinux.org> 3.15.5-alt1
- Automatically updated to 3.15.5.

* Tue Aug 22 2023 Grigory Ustinov <grenka@altlinux.org> 3.15.2-alt1
- Automatically updated to 3.15.2.

* Tue Aug 01 2023 Grigory Ustinov <grenka@altlinux.org> 3.14.0-alt1
- Automatically updated to 3.14.0.

* Thu Jul 20 2023 Grigory Ustinov <grenka@altlinux.org> 3.12.2-alt1
- Automatically updated to 3.12.2.

* Wed Jul 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.12.1-alt1
- Automatically updated to 3.12.1.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 3.9.1-alt1
- Automatically updated to 3.9.1.

* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Automatically updated to 3.8.1.

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

