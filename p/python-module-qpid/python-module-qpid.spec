
Name: python-module-qpid
Version: 0.32
Release: alt1
Summary: Python client library for AMQP

License: ASL 2.0
Group: Development/Python
Url: http://qpid.apache.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
The Apache Qpid Python client library for AMQP.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE.txt NOTICE.txt README.txt examples
%python_sitelibdir/*
%_bindir/qpid-python-test
%exclude %python_sitelibdir/qpid/test*

%changelog
* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1
- 0.32

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.30-alt1
- 0.30

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.18-alt1
- Initial release for Sisyphus (based on Fedora)
