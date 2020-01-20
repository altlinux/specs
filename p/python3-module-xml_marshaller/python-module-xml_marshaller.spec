%define oname xml_marshaller

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: Converting Python objects to XML and back again
License: Python License
Group: Development/Python3
URL: http://www.python.org/community/sigs/current/xml-sig/
BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libxml2-devel


%description
This module allows one to marshal simple Python data types into a custom XML format.
The Marshaller and Unmarshaller classes can be subclassed in order
to implement marshalling into a different XML DTD.
Original Authors are XML-SIG (xml-sig@python.org).

Fully compatible with PyXML implementation, enables namespace support for XML Input/Output.

Implemented with lxml

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/doc


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- Porting on Python3.

* Thu Aug 08 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1
- Initial build for ALT
