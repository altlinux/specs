%define oname seamicroclient

Name: python3-module-%oname
Version: 0.1.0
Release: alt3

Summary: Python client for consuming SeaMicro REST API v2.0
License: ASL 2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-seamicroclient/

BuildArch: noarch

Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%description
Python client for consuming SeaMicro REST API v2.0

%prep
%setup -q -n %oname-%version

# Remove bundled egg-info
rm -rf python_seamicroclient.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt3
- Build for python2 disabled.

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.1.0-alt1
- First build for ALT

