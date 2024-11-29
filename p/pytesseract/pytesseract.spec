%define _unpackaged_files_terminate_build 1

%def_with check

Name: pytesseract
Version: 0.3.13
Release: alt1

Summary: An optical character recognition (OCR) tool for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/pytesseract
Vcs: https://github.com/madmaze/pytesseract

Source: %name-%version.tar
Patch0: pytesseract-0.3.10-skip-gif.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3(PIL)
BuildRequires: python3(pytest)
BuildRequires: python3(numpy)
BuildRequires: python3(pandas)
BuildRequires: python3-module-pandas-tests
BuildRequires: tesseract
BuildRequires: tesseract-langpack-fr
BuildRequires: tesseract-langpack-osd
%endif

Requires: tesseract
Requires: python3-module-%name = %version-%release

BuildArch: noarch

%description
Python-tesseract is an optical character recognition (OCR) tool for
Python. That is, it will recognize and "read" the text embedded in
images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine.
It is also useful as a stand-alone invocation script to tesseract,
as it can read all image types supported by the Pillow and Leptonica
imaging libraries, including jpeg, png, gif, bmp, tiff, and others.
Additionally, if used as a script, Python-tesseract will print the
recognized text instead of writing it to a file.

%package -n python3-module-%name
Summary: An optical character recognition (OCR) tool for Python
Group: Development/Python3

%description -n python3-module-%name
Python-tesseract is an optical character recognition (OCR) tool for
Python. That is, it will recognize and "read" the text embedded in
images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine.
It is also useful as a stand-alone invocation script to tesseract,
as it can read all image types supported by the Pillow and Leptonica
imaging libraries, including jpeg, png, gif, bmp, tiff, and others.
Additionally, if used as a script, Python-tesseract will print the
recognized text instead of writing it to a file.

%prep
%setup
%patch0 -p2

%build
%pyproject_build

%install
%pyproject_install

%check
# test_get_languages coredumps tessaract with invalid input
%pyproject_run_pytest -k 'not test_get_languages'

%files
%_bindir/%name

%files -n python3-module-%name
%doc *.rst
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info

%changelog
* Tue Nov 19 2024 Anton Vyatkin <toni@altlinux.org> 0.3.13-alt1
- New version 0.3.13.
- Migrate to pyproject macroses.

* Fri Dec 22 2023 Anton Vyatkin <toni@altlinux.org> 0.3.10-alt1.1
- NMU: fixed FTBFS (added BR pandas-tests).

* Wed Jun 15 2022 Paul Wolneykien <manowar@altlinux.org> 0.3.10-alt1
- Initial version 0.3.10.
