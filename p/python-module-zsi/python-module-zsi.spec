Name:           python-module-zsi
Version:        2.0
Release:        alt1
Summary:        The Zolera SOAP Infrastructure

License:        PSF
Group:          Development/Python
URL:            http://pywebsvcs.sourceforge.net/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        ZSI-%{version}.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  python-module-twisted
Provides:	    zsi = %version

%description
ZSI, the Zolera SOAP Infrastructure, is a pure-Python module that
provides an implementation of SOAP messaging, as described in SOAP 1.1
Specification (see http://www.w3.org/TR/soap).  It can also be used to
build applications using SOAP Messages with Attachments (see
http://www.w3.org/TR/SOAP-attachments).  ZSI is intended to make it
easier to write web services in Python.


%prep
%setup -q -n ZSI-%version

%build
%python_build

%install
%python_install

%files
%doc README
%_bindir/wsdl2*
%dir %python_sitelibdir/ZSI
%python_sitelibdir/ZSI/*
%python_sitelibdir/ZSI-*.egg-info

%changelog
* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Initial build in Sisyphus
