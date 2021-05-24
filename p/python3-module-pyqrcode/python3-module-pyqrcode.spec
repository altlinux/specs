%define  modulename pyqrcode

Name:    python3-module-%modulename
Version: 1.2.1
Release: alt2

Summary: Python module to generate QR Codes
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mnooner256/pyqrcode

Packager: Anton Midyukov <antohami@altlinux.org>

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

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt2
- rename srpm to python3-module-pyqrcode
- cleanup spec

* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
