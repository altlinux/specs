%define _unpackaged_files_terminate_build 1

Name: pytesseract
Version: 0.3.10
Release: alt1.1

Summary: An optical character recognition (OCR) tool for Python
License: Apache-2.0
Group: Development/Python
Url: https://github.com/madmaze/pytesseract

Source: %name-%version.tar

Patch0: pytesseract-0.3.10-skip-gif.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pre_commit)
BuildRequires: python3(nodeenv)
BuildRequires: python3(PIL)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(numpy)
BuildRequires: python3(pandas)
BuildRequires: python3-module-pandas-tests
BuildRequires: tesseract tesseract-langpack-fr tesseract-langpack-osd
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
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages --skip-pkg-install -p auto -o -v

%files
%_bindir/%name

%files -n python3-module-%name
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Dec 22 2023 Anton Vyatkin <toni@altlinux.org> 0.3.10-alt1.1
- NMU: fixed FTBFS (added BR pandas-tests).

* Wed Jun 15 2022 Paul Wolneykien <manowar@altlinux.org> 0.3.10-alt1
- Initial version 0.3.10.
