%define modulename xml_marshaller

Name: python-module-%modulename
Summary: Converting Python objects to XML and back again
Version: 1.0.2
Release: alt1
Group: Development/Python
License: Python License
URL: http://www.python.org/community/sigs/current/xml-sig/
Source: %modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: libxml2-devel

%description
This module allows one to marshal simple Python data types into a custom XML format.
The Marshaller and Unmarshaller classes can be subclassed in order
to implement marshalling into a different XML DTD.
Original Authors are XML-SIG (xml-sig@python.org).

Fully compatible with PyXML implementation, enables namespace support for XML Input/Output.

Implemented with lxml

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/doc

%changelog
* Thu Aug 08 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1
- Initial build for ALT
