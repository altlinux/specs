%define modulename progressbar

Name: python-module-progressbar
Version: 2.2
Release: alt1.1

Summary: Text progressbar library for python

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://pypi.python.org/packages/source/t/%modulename/%modulename-%version.tar

%setup_python_module %modulename

# Automatically added by buildreq on Thu Mar 11 2010
BuildRequires: python-devel

%description
This library provides a text mode progress bar. This is typically used to
display the progress of a long running operation, providing a visual clue that
processing is under way.

The progressbar module is very easy to use, yet very powerful. And
automatically supports features like auto-resizing when available.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install
chmod 0755 %buildroot%python_sitelibdir/progressbar.py

%files
%doc README
%python_sitelibdir/%modulename.*
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1
- Rebuild with Python-2.7

* Thu Mar 11 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
