%define modulename pypdf

Name: python-module-%modulename
Version: 1.12
Release: alt1.1
Summary: A Pure-Python library built as a PDF toolkit
%setup_python_module %modulename

Group: Development/Python
License: modified BSD
Url: http://pybrary.net/pyPdf/
Packager: Michael A. Kangin <prividen@altlinux.org>

BuildArch: noarch
Source: %name-%version.tar


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
%python_build

%install
%python_install


%files
%python_sitelibdir/pyPdf/
%python_sitelibdir/*.egg-info




%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12-alt1.1
- Rebuild with Python-2.7

* Wed Jun 16 2010 Michael A. Kangin <prividen@altlinux.org> 1.12-alt1
- Initial release for Sisyphus

