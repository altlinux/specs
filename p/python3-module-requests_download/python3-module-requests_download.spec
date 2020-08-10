%define _unpackaged_files_terminate_build 1

%define oname requests_download

Name: python3-module-%oname
Version: 0.1.2
Release: alt1
Summary: Download files using requests and save them to a target path
License: MIT
Group: Development/Python3
URL: https://www.github.com/takluyver/requests_download

BuildArch: noarch

# https://www.github.com/takluyver/requests_download.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%description
A convenient function to download to a file using requests.

%prep
%setup

%build
flit build

%install
pip%{_python3_version} install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Initial build for ALT.
