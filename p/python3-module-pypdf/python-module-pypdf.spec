%define modulename pypdf

Name: python3-module-%modulename
Version: 1.12
Release: alt1.1
Summary: A Pure-Python library built as a PDF toolkit

Group: Development/Python3
License: modified BSD
Url: http://pybrary.net/pyPdf/

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel

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
%python3_build

%install
%python3_install


%files
%python3_sitelibdir/pyPdf/
%python3_sitelibdir/*.egg-info


%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.12-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt1
- Initial build for Sisyphus

