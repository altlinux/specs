Name: python-module-byteplay
Summary: Python bytecode dis-/reassembler library.
Version: 0.3
Release: alt1.1
License: LGPL
Group: Development/Python
URL: https://github.com/svinota/byteplay

BuildArch: noarch
BuildPreReq: python-devel rpm-build-python

Source: %name-%version.tar

%description
byteplay lets you convert Python code objects into equivalent objects
which are easy to play with, and lets you convert those objects back
into living Python code objects. It's useful for applying crazy
transformations on Python functions, and is also useful in learning
Python byte code intricacies. It currently works with Python 2.4 and up.

%prep
%setup

%install
%{__python} setup.py install --root=%buildroot --install-lib=%{python_sitelibdir}

%files

%{python_sitelibdir}/byteplay*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Wed Aug 18 2011 Peter V. Saveliev <peet@altlinux.org> 0.3-alt1
- initial ALT Linux build
