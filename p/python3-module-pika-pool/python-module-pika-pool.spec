%define oname pika-pool

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: Pika connection pooling
License: BSD
Group: Development/Python3
Url: https://github.com/bninja/pika-pool
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- python2 disabled

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- initial build
