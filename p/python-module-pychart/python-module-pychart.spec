%define oname PyChart
%define module pychart
%define _python_egg_info %python_sitelibdir/%oname-%version-py%__python_version.egg-info

Name: python-module-pychart
Version: 1.39
Release: alt1.1.1

Summary: A Python library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts

License: BSD like
Url: http://home.gna.org/pychart/
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.gna.org/pychart/%oname-%version.tar.bz2

BuildArch: noarch

BuildPreReq: rpm-build-compat >= 1.2

# Automatically added by buildreq on Sun Jan 04 2009
BuildRequires: python-devel

%description
PyChart is a Python library for creating high quality Encapsulated
Postscript, PDF, PNG, or SVG charts. It currently supports line plots,
bar plots, range-fill plots, and pie charts. Because it is based on
Python, you can make full use of Python's scripting power

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/%module/
%_python_egg_info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.39-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt1.1
- Rebuilt with python 2.6

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 1.39-alt1
- initial build for ALT Linux Sisyphus

