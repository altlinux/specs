Name:           python-module-pyeclib
Version:        1.0.8
Release:        alt1
Summary:        Python interface to erasure codes
Group:          Development/Python

License:        BSD
URL:            https://bitbucket.org/kmgreen2/pyeclib/
Source0:        %name-%version.tar

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  liberasurecode-devel >= 1.0.7

Requires:       liberasurecode >= 1.0.7

%description
This library provides a simple Python interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README License.txt
%python_sitelibdir/*

%changelog
* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT
