%define  modulename pyqrcode

%python_req_hier

Name:    python-module-%modulename
Version: 1.2.1
Release: alt1

Summary: Python module to generate QR Codes
License: BSD-3-Clause
Group:   Development/Python
URL:     https://github.com/mnooner256/pyqrcode

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
The pyqrcode module is a QR code generator that is simple to use
and written in pure python. The module can automates most of the
building process for creating QR codes. Most codes can be created
using only two lines of code!

Unlike other generators, all of the helpers can be controlled
manually. You are free to set any or all of the properties of
your QR code.

QR codes can be saved as SVG, XBM, EPS, PNG (by using the pypng
module), or plain text. They can also be displayed directly in
most Linux terminal emulators and Tkinter. PIL is not used to
render the image files.

The pyqrcode module attempts to follow the QR code standard as
closely as possible. The terminology and the encodings used in
pyqrcode come directly from the standard. This module also follows
the algorithm laid out in the standard.

%package -n python3-module-%modulename
Summary: Python 3 module to generate QR Codes
Group: Development/Python3

%description -n python3-module-%modulename
The pyqrcode module is a QR code generator that is simple to use
and written in pure python. The module can automates most of the
building process for creating QR codes. Most codes can be created
using only two lines of code!

Unlike other generators, all of the helpers can be controlled
manually. You are free to set any or all of the properties of
your QR code.

QR codes can be saved as SVG, XBM, EPS, PNG (by using the pypng
module), or plain text. They can also be displayed directly in
most Linux terminal emulators and Tkinter. PIL is not used to
render the image files.

The pyqrcode module attempts to follow the QR code standard as
closely as possible. The terminology and the encodings used in
pyqrcode come directly from the standard. This module also follows
the algorithm laid out in the standard.

Python 3 version.

%prep
%setup -n %modulename-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
