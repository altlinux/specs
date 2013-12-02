
Summary: Python bindings for the libvirt library
Name: python-module-libvirt
Version: 1.2.0
Release: alt1
Url: http://libvirt.org/python.html
#http://libvirt.org/git/?p=libvirt-python.git
Source: %name-%version.tar
License: LGPLv2+
Group: Development/Python

Requires: libvirt-client
BuildRequires: libvirt-devel >= 0.9.11
BuildRequires: python-devel python-module-distribute

Obsoletes: libvirt-python < %version-%release
Provides: libvirt-python = %version-%release

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/libvirt*
%doc  NEWS README COPYING COPYING.LESSER examples

%changelog
* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- initial build; split off from main libvirt package
