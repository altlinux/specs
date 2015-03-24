%add_python_lib_path %_datadir/qpid-tools/python

Name: qpid-tools
Version: 0.32
Release: alt1
Summary: Management and diagostic tools for Apache Qpid
License: ASL 2.0
Group: Networking/Other
Url: http://qpid.apache.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
Management and diagnostic tools for Apache Qpid brokers and clients.

%package -n python-module-qpidtoollibs
Summary: Management and diagostic tools for Apache Qpid
Group: Development/Python

%description  -n python-module-qpidtoollibs
Management and diagostic tools for Apache Qpid

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*
%_prefix/libexec/qpid-qls-analyze

%files -n python-module-qpidtoollibs
%python_sitelibdir/*
%_datadir/qpid-tools/python/qlslibs

%changelog
* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1
- Initial release for Sisyphus
