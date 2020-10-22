%define _unpackaged_files_terminate_build 1
%define oname vine

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: Python promises

License: BSD
Group: Development/Python3
Url: https://github.com/celery/vine

BuildArch: noarch

# https://github.com/celery/vine.git
# Source-url: https://github.com/celery/vine/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Promises, promises, promises.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Tue Oct 13 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Stopped Python2 package build(Python2 EOL).

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)
- switch to build from tarball

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1
- Initial build for ALT.
